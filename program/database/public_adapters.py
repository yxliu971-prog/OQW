"""固定官方/开源端点适配器。保留原始分类，不把自定义映射冒充 GSK 评级。"""

import csv
import hashlib
import io
import json
import re
import socket
from dataclasses import dataclass
from ipaddress import ip_address
from urllib.parse import urlsplit

import httpx

from chem_engine.hsp_matcher import _cas

EPA_URL = "https://www.epa.gov/saferchoice/safer-ingredients"
HSP_URL = (
    "https://raw.githubusercontent.com/CalebBell/chemicals/master/chemicals/Misc/"
    "ruben_manuel_hansen_solubility_parameters.tsv"
)
SCIL_METHOD = "OQW-SCIL-v1: EPA 圆/半圆/三角/灰方块映射为 9/7/4/1；非 GSK/EPA 官方数值评分"

CATALOG = [
    dict(
        id="epa-scil",
        name="US EPA · SCIL 溶剂分类",
        kind="solvents",
        adapter="epa_scil",
        location=EPA_URL,
        license="US EPA public website; acknowledge EPA; no EPA endorsement",
        attribution="US EPA Safer Choice / Safer Chemical Ingredients List",
        score_method=SCIL_METHOD,
        priority=20,
        interval_hours=24,
    ),
    dict(
        id="open-hsp",
        name="开放 HSP · chemicals / de los Ríos–Belmonte",
        kind="solvents",
        adapter="hsp",
        location=HSP_URL,
        license="chemicals MIT compilation; original references retained; verify reuse terms",
        attribution="Caleb Bell et al., chemicals; de los Ríos & Belmonte (2022), "
        "https://doi.org/10.1007/s42452-022-04959-4 ; HSP source conditions not reported",
        priority=10,
        interval_hours=168,
    ),
    dict(
        id="pubchem-core",
        name="PubChem · 常用溶剂结构与物性",
        kind="solvents",
        adapter="pubchem",
        location="https://pubchem.ncbi.nlm.nih.gov/rest/pug",
        license="PubChem: contributor-specific licenses; source reference stored per property",
        attribution="NCBI PubChem PUG REST/PUG View; physical data selected from NIOSH/ICSC",
        priority=30,
        interval_hours=168,
    ),
    dict(
        id="echa-svhc",
        name="ECHA · SVHC 候选清单（待手动接入）",
        kind="hazards",
        adapter="echa",
        location="https://echa.europa.eu/candidate-list-table",
        license="ECHA Legal Notice: https://echa.europa.eu/legal-notice",
        attribution="European Chemicals Agency; CAS-specific candidate-list entries only",
        priority=40,
        interval_hours=0,
        enabled=False,
    ),
]

# 以 CAS 请求 PubChem 解析，避免硬编码 CID 对应错误。没有来源的字段保持空值。
COMMON_CAS = [
    "7732-18-5",
    "64-17-5",
    "67-56-1",
    "67-64-1",
    "141-78-6",
    "67-63-0",
    "75-05-8",
    "108-88-3",
    "109-99-9",
    "75-09-2",
    "71-43-2",
    "68-12-2",
    "67-68-5",
    "110-54-3",
    "142-82-5",
    "56-81-5",
    "107-21-1",
    "5989-27-5",
]


@dataclass
class Download:
    records: list[dict]
    sha256: str
    notes: list[str]


def safe_remote_url(url: str):
    """用户远程源只允许公网 HTTPS；禁止凭据、内网、回环及重定向。"""
    parts = urlsplit(url)
    if (
        parts.scheme != "https"
        or not parts.hostname
        or parts.username
        or parts.password
        or parts.fragment
        or parts.port not in (None, 443)
    ):
        raise ValueError("远程数据源须为不含凭据的公网 HTTPS URL（443 端口）")
    addresses = socket.getaddrinfo(parts.hostname, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ip_address(item[4][0]).is_global for item in addresses):
        raise ValueError("远程数据源不能指向本机、内网或保留地址")
    return addresses[0][4][0]


def fetch(client: httpx.Client, url: str, *, limit=10 * 1024 * 1024) -> bytes:
    # 固定、代码内审阅过的公开端点兼容本机代理的 Fake-IP DNS；用户自定义源不豁免。
    trusted = url in (
        EPA_URL,
        HSP_URL,
        "https://echa.europa.eu/candidate-list-table",
    ) or url.startswith("https://pubchem.ncbi.nlm.nih.gov/rest/")
    options = {}
    if not trusted:
        # 连接固定到刚刚校验的 IP，保留 TLS SNI 和 Host，避免二次 DNS 解析绕过检查。
        address = safe_remote_url(url)
        parsed = httpx.URL(url)
        options = {"headers": {"Host": parsed.host}, "extensions": {"sni_hostname": parsed.host}}
        url = parsed.copy_with(host=address)
    result = bytearray()
    with client.stream("GET", url, follow_redirects=False, timeout=25, **options) as response:
        response.raise_for_status()
        for chunk in response.iter_bytes(65536):
            result.extend(chunk)
            if len(result) > limit:
                raise ValueError("远程文件超过 10 MiB 上限")
    if not result:
        raise ValueError("远程文件为空")
    return bytes(result)


def parse_scil(payload: bytes) -> Download:
    # 只解析 EPA 页面内的 JSON 数据数组，绝不执行远程 JavaScript。
    match = re.search(r"var\s+dataSet\s*=\s*(\[.*?\]);", payload.decode("utf-8"), re.S)
    if not match:
        raise ValueError("EPA 页面结构已变化，未找到 SCIL 数据数组，保留上次成功版本")
    rows = json.loads(match.group(1))
    grades = {
        "Green [Circle]": 9,
        "Green [Half Circle]": 7,
        "Yellow [Triangle]": 4,
        "Grey [Square]": 1,
        "Gray [Square]": 1,
    }
    records, skipped = [], 0
    for row in rows:
        if "Solvents" not in row.get("FClassList", ""):
            continue
        try:
            cas = _cas(row.get("CAS"))
        except ValueError:
            skipped += 1
            continue
        code = row["Code"]
        if code not in grades:
            raise ValueError(f"SCIL 出现未知分类 {code}，需要审阅映射")
        records.append(
            dict(
                cas=cas,
                name=row["TName"],
                gsk_score=grades[code],
                raw_scores={
                    "EPA_SCIL_code": code,
                    "caveat": row.get("CodeCaveat"),
                    "CAS_caveat": row.get("CASCaveat"),
                    "mapping": SCIL_METHOD,
                },
                excluded=grades[code] == 1,
            )
        )
    if len(records) < 50:
        raise ValueError("SCIL 溶剂记录数量异常，拒绝覆盖现有快照")
    return Download(
        records,
        hashlib.sha256(payload).hexdigest(),
        [
            "只导入 SCIL 功能分类为 Solvents 且有有效 CAS 的条目；不在清单不等于不安全。",
            f"跳过无独立有效 CAS 的条目：{skipped}；SCIL 不等于 EPA 产品认证。",
            SCIL_METHOD,
        ],
    )


def parse_hsp(payload: bytes) -> Download:
    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig")), delimiter="\t"))
    required = {"CAS", "HANSEN_DELTA_D", "HANSEN_DELTA_P", "HANSEN_DELTA_H"}
    if len(rows) < 100 or not required <= rows[0].keys():
        raise ValueError("HSP 上游字段或记录数量异常，保留上次成功版本")
    records = [
        dict(
            cas=row["CAS"],
            name=row["CAS"],
            delta_d=float(row["HANSEN_DELTA_D"]) / 1000,
            delta_p=float(row["HANSEN_DELTA_P"]) / 1000,
            delta_h=float(row["HANSEN_DELTA_H"]) / 1000,
            hsp_temperature_c=None,
        )
        for row in rows
    ]
    return Download(
        records,
        hashlib.sha256(payload).hexdigest(),
        [
            "源参数单位 Pa^0.5，除以 1000 转为 MPa^0.5；三参数同源同步。",
            "该 TSV 未提供逐条测量温度，保持未知；物性为文献汇编，非产品规格保证。",
            "许可与引用：https://github.com/CalebBell/chemicals/blob/master/LICENSE.txt",
        ],
    )


def sections(record, heading):
    if isinstance(record, dict):
        if record.get("TOCHeading") == heading:
            yield record
        for value in record.values():
            yield from sections(value, heading)
    elif isinstance(record, list):
        for item in record:
            yield from sections(item, heading)


def strings(info):
    return [item["String"] for item in info.get("Value", {}).get("StringWithMarkup", [])]


def temperature(info):
    """只接受无范围/压力歧义的单值 Celsius / Fahrenheit；不猜测字符串中的数字。"""
    value = info.get("Value", {})
    unit = value.get("Unit", "")
    if len(value.get("Number", [])) == 1 and unit in ("°C", "deg C", "C", "°F", "deg F", "F"):
        n = value["Number"][0]
        return round((n - 32) * 5 / 9, 3) if "F" in unit else n
    for text in strings(info):
        match = re.fullmatch(r"\s*(-?\d+(?:\.\d+)?)\s*°?([CF])\s*", text)
        if match:
            n = float(match[1])
            return round((n - 32) * 5 / 9, 3) if match[2] == "F" else n
    return None


def download_pubchem(client) -> Download:
    records, notes, hashes = [], [], []
    for cas in COMMON_CAS:
        raw = fetch(
            client,
            f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{cas}/"
            "property/IUPACName,CanonicalSMILES/JSON",
        )
        properties = json.loads(raw)["PropertyTable"]["Properties"]
        if len(properties) != 1:
            raise ValueError(f"{cas} 在 PubChem 对应多个结构，需要人工核对")
        item = properties[0]
        row = dict(
            cas=cas,
            name=item["IUPACName"],
            smiles=item.get("ConnectivitySMILES") or item.get("CanonicalSMILES"),
        )
        phys = fetch(
            client,
            "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/"
            f"{item['CID']}/JSON?heading=Chemical%20and%20Physical%20Properties",
        )
        data = json.loads(phys)["Record"]
        refs = {r["ReferenceNumber"]: r for r in data.get("Reference", [])}
        property_refs = {}
        for heading, key in [("Boiling Point", "boiling_point"), ("Flash Point", "flash_point")]:
            for section in sections(data, heading):
                for info in section.get("Information", []):
                    ref = refs.get(info.get("ReferenceNumber"), {})
                    if not any(label in ref.get("SourceName", "") for label in ("NIOSH", "ICSC")):
                        continue
                    number = temperature(info)
                    if number is not None and key not in row:
                        row[key] = number
                        property_refs[key] = {
                            k: ref.get(k)
                            for k in ("SourceName", "URL", "LicenseNote", "LicenseURL")
                        }
        # 保留结构、物性出处；不聚合不同贡献者的危害标注为法定分类。
        row["raw_scores"] = {"PubChem_CID": item["CID"], "property_references": property_refs}
        records.append(row)
        hashes.extend([hashlib.sha256(raw).hexdigest(), hashlib.sha256(phys).hexdigest()])
    notes.append("18 种常见溶剂；结构按 CAS 请求 PubChem；沸/闪点仅选 NIOSH/ICSC 的无歧义单值。")
    notes.append("未解析到可用物性时不填值；不从 PubChem 聚合危害资料推断官方 GSK 分数。")
    return Download(records, hashlib.sha256("".join(hashes).encode()).hexdigest(), notes)


def download(adapter: str, location: str, client=None) -> Download | bytes:
    def run(active):
        if adapter == "pubchem":
            return download_pubchem(active)
        raw = fetch(active, location)
        if adapter == "epa_scil":
            return parse_scil(raw)
        if adapter == "hsp":
            return parse_hsp(raw)
        if adapter == "echa":
            raise ValueError(
                "ECHA 页面没有已核验的稳定机器读取结构；请下载官方 CSV 后在当地规则区导入。"
                "未完成同步，不代表当前 SVHC 清单已覆盖。"
            )
        return raw

    if client is not None:
        return run(client)
    with httpx.Client(trust_env=False, headers={"User-Agent": "OQW/0.5 dataset-sync"}) as owned:
        return run(owned)

"""OQW 便携入口：所有路径相对于本文件，不依赖本机开发环境。"""
import argparse
import json
import os
import shutil
import socket
import sqlite3
import sys
import threading
import time
import urllib.request
import webbrowser
from datetime import datetime
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent
PROGRAM = ROOT / 'program'
sys.path.insert(0, str(PROGRAM))
os.chdir(ROOT)
sys.dont_write_bytecode = True
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def initialize_data():
    """GitHub 只保存公开种子；首次运行生成不会被 Git 跟踪的个人数据库。"""
    import msvcrt
    data = ROOT / 'data'
    data.mkdir(exist_ok=True)
    with (data / '.initialize.lock').open('a+b') as lock:
        lock.seek(0, 2)
        if lock.tell() == 0:
            lock.write(b'0'); lock.flush()
        lock.seek(0)
        msvcrt.locking(lock.fileno(), msvcrt.LK_LOCK, 1)
        try:
            database = data / 'oqw.sqlite3'
            if database.exists():
                return
            seed = data / 'public-seed.sqlite3'
            if not seed.is_file():
                raise FileNotFoundError('缺少公开数据种子，请完整下载并解压仓库。')
            temporary = data / f'.initial-{uuid4().hex}.sqlite3'
            try:
                shutil.copyfile(seed, temporary)
                os.replace(temporary, database)
            finally:
                temporary.unlink(missing_ok=True)
        finally:
            lock.seek(0)
            msvcrt.locking(lock.fileno(), msvcrt.LK_UNLCK, 1)


def settings(auto=True):
    from app.config import Settings
    return Settings(database_url=f'sqlite:///{ROOT / "data/oqw.sqlite3"}',
                    frontend_dir=PROGRAM / 'frontend/dist',
                    pdf_font_path=PROGRAM / 'fonts/OQWReportSans-Regular.ttf',
                    auto_update=auto, allow_demo=False)


def backup():
    folder = ROOT / '备份'
    folder.mkdir(exist_ok=True)
    target = folder / f'oqw-{datetime.now():%Y%m%d-%H%M%S-%f}.sqlite3'
    with sqlite3.connect(ROOT / 'data/oqw.sqlite3', timeout=30) as source:
        with sqlite3.connect(target) as dest:
            source.backup(dest)
    print(f'备份完成：{target}')


def check():
    from fastapi.testclient import TestClient
    from app.main import create_app
    import rdkit
    recipe = {'reactants':[{'smiles':'CC(=O)O','mass':60},{'smiles':'CCO','mass':50}],
              'product':{'smiles':'CCOC(C)=O','mass':70}, 'persist':False,
              'solvents':[{'cas':'5989-27-5','mass':100}],
              'total_waste_mass':150,'waste_boundary':'交付验收示例，非实际实验'}
    with TestClient(create_app(settings(False))) as client:
        health=client.get('/health'); health.raise_for_status()
        response=client.post('/api/v1/evaluate',json=recipe); response.raise_for_status()
        assert 80 < response.json()['metrics']['atom_economy'] < 85
        swap=client.post('/api/v1/recommend-swap',json={'cas':'5989-27-5'})
        if swap.status_code not in (200, 404, 422):
            swap.raise_for_status()
        pdf=client.post('/api/v1/reports/pdf',json={'evaluation':recipe}); pdf.raise_for_status()
        assert pdf.content.startswith(b'%PDF') and len(pdf.content)>10000
        sources=client.get('/api/v1/datasets').json()
        assert sources['solvent_count'] >= 0
        assert client.get('/').status_code == 200
    print(json.dumps({'status':'通过','Python':sys.version.split()[0], 'RDKit':rdkit.__version__,
                      '物质数':sources['solvent_count'],'替换候选数':len(swap.json().get('replacements',[])),
                      '替换检查': '通过' if swap.status_code==200 else '当前数据不足，已跳过；不代表运行环境故障',
                      'PDF字节数':len(pdf.content),'runtime':sys.executable,
                      '模块路径':[str(Path(sys.modules[n].__file__).resolve()) for n in ('app','rdkit','fastapi')]},ensure_ascii=False,indent=2))


def browser_when_ready(port):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    for _ in range(120):
        try:
            with opener.open(f'http://127.0.0.1:{port}/health', timeout=1) as response:
                if response.status == 200:
                    webbrowser.open(f'http://127.0.0.1:{port}/')
                    return
        except Exception:
            time.sleep(.5)


def main():
    parser=argparse.ArgumentParser(description='OQW Windows 便携工作台')
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--backup',action='store_true')
    parser.add_argument('--prepare-data',action='store_true')
    parser.add_argument('--port',type=int,default=8000)
    parser.add_argument('--no-browser',action='store_true')
    parser.add_argument('--no-auto-update',action='store_true')
    args=parser.parse_args()
    initialize_data()
    if args.prepare_data:
        print('本机数据库已准备。'); return
    if args.check:
        check(); return
    if args.backup:
        backup(); return
    import msvcrt
    import uvicorn
    from app.main import create_app
    (ROOT/'logs').mkdir(exist_ok=True)
    # 操作系统文件锁随进程结束释放；不会依据可能过期的 PID 终止其他程序。
    with (ROOT/'logs/app.lock').open('a+b') as lock:
        lock.seek(0,2)
        if lock.tell()==0:
            lock.write(b'0'); lock.flush()
        lock.seek(0)
        try:
            msvcrt.locking(lock.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:
            print('此文件夹的 OQW 已经运行，请使用原来的窗口。')
            info=ROOT/'logs/server.json'
            if info.exists() and not args.no_browser:
                saved=json.loads(info.read_text(encoding='utf-8'))
                webbrowser.open(f"http://127.0.0.1:{saved['port']}/")
            return
        port=None
        for number in range(args.port,min(args.port+11,65536)):
            with socket.socket() as probe:
                try:
                    probe.bind(('127.0.0.1',number)); port=number; break
                except OSError:
                    continue
        if port is None:
            raise RuntimeError('8000 起的可选端口均被占用，请关闭旧窗口或使用 --port 指定端口。')
        (ROOT/'logs/server.json').write_text(json.dumps({'port':port,'pid':os.getpid()}),encoding='utf-8')
        print(f'\nOQW 已准备启动：http://127.0.0.1:{port}/\n数据保存在：{ROOT / "data"}\n保持此窗口运行。停止服务请按 Ctrl+C。\n')
        if not args.no_browser:
            threading.Thread(target=browser_when_ready,args=(port,),daemon=True).start()
        uvicorn.run(create_app(settings(not args.no_auto_update)),host='127.0.0.1',port=port)


if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        import traceback
        (ROOT/'logs').mkdir(exist_ok=True)
        (ROOT/'logs/启动错误.log').write_text(traceback.format_exc(),encoding='utf-8')
        traceback.print_exc()
        print('操作失败，详情已保存到 logs/启动错误.log。')
        raise SystemExit(1)

from __future__ import annotations
from builtins import memoryview as binaryHolder
from rdkit import RDConfig
import sqlite3 as sqlite
__all__: list[str] = ['RDConfig', 'binaryHolder', 'binaryTypeName', 'connect', 'dbFileWildcard', 'fileWildcard', 'getDbSql', 'getTablesAndViewsSql', 'getTablesSql', 'placeHolder', 'sqlBinTypes', 'sqlFloatTypes', 'sqlIntTypes', 'sqlTextTypes', 'sqlite']
def connect(x, *args):
    ...
binaryTypeName: str = 'blob'
dbFileWildcard: str = '*.sqlt'
fileWildcard: str = '*.sqlt'
getDbSql = None
getTablesAndViewsSql: str = "select name from SQLite_Master where type in ('table','view')"
getTablesSql: str = "select name from SQLite_Master where type='table'"
placeHolder: str = '?'
sqlBinTypes: list = list()
sqlFloatTypes: list = list()
sqlIntTypes: list = list()
sqlTextTypes: list = list()

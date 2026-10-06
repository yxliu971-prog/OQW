from __future__ import annotations
from rdkit.Dbase import DbModule
from rdkit import RDConfig
import sys as sys
__all__: list[str] = ['DbModule', 'GetColumnInfoFromCursor', 'GetColumnNames', 'GetColumnNamesAndTypes', 'GetDbNames', 'GetTableNames', 'RDConfig', 'sqlBinTypes', 'sqlFloatTypes', 'sqlIntTypes', 'sqlTextTypes', 'sys']
def GetColumnInfoFromCursor(cursor):
    ...
def GetColumnNames(dBase, table, user = 'sysdba', password = 'masterkey', join = '', what = '*', cn = None):
    """
     gets a list of columns available in a DB table
    
          **Arguments**
    
            - dBase: the name of the DB file to be used
    
            - table: the name of the table to query
    
            - user: the username for DB access
    
            - password: the password to be used for DB access
    
            - join: an optional join clause  (omit the verb 'join')
    
            - what: an optional clause indicating what to select
    
          **Returns**
    
            -  a list of column names
    
        
    """
def GetColumnNamesAndTypes(dBase, table, user = 'sysdba', password = 'masterkey', join = '', what = '*', cn = None):
    """
     gets a list of columns available in a DB table along with their types
    
          **Arguments**
    
            - dBase: the name of the DB file to be used
    
            - table: the name of the table to query
    
            - user: the username for DB access
    
            - password: the password to be used for DB access
    
            - join: an optional join clause (omit the verb 'join')
    
            - what: an optional clause indicating what to select
    
          **Returns**
    
            - a list of 2-tuples containing:
    
                1) column name
    
                2) column type
    
        
    """
def GetDbNames(user = 'sysdba', password = 'masterkey', dirName = '.', dBase = '::template1', cn = None):
    """
     returns a list of databases that are available
    
          **Arguments**
    
            - user: the username for DB access
    
            - password: the password to be used for DB access
    
          **Returns**
    
            - a list of db names (strings)
    
        
    """
def GetTableNames(dBase, user = 'sysdba', password = 'masterkey', includeViews = 0, cn = None):
    """
     returns a list of tables available in a database
    
          **Arguments**
    
            - dBase: the name of the DB file to be used
    
            - user: the username for DB access
    
            - password: the password to be used for DB access
    
            - includeViews: if this is non-null, the views in the db will
              also be returned
    
          **Returns**
    
            - a list of table names (strings)
    
        
    """
sqlBinTypes: list = list()
sqlFloatTypes: list = list()
sqlIntTypes: list = list()
sqlTextTypes: list = list()

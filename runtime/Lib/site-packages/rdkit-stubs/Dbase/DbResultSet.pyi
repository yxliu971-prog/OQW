"""
 defines class _DbResultSet_ for lazy interactions with Db query results

**Note**

  this uses the Python iterator interface, so you'll need python 2.2 or above.

"""
from __future__ import annotations
from rdkit.Dbase import DbInfo
import sys as sys
__all__: list[str] = ['DbInfo', 'DbResultBase', 'DbResultSet', 'RandomAccessDbResultSet', 'sys']
class DbResultBase:
    def GetColumnNames(self):
        ...
    def GetColumnNamesAndTypes(self):
        ...
    def GetColumnTypes(self):
        ...
    def Reset(self):
        """
         implement in subclasses
        
            
        """
    def __init__(self, cursor, conn, cmd, removeDups = -1, transform = None, extras = None):
        ...
    def __iter__(self):
        ...
    def _initColumnNamesAndTypes(self):
        ...
class DbResultSet(DbResultBase):
    """
     Only supports forward iteration 
    """
    def Reset(self):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __next__(self):
        ...
    def next(self):
        ...
class RandomAccessDbResultSet(DbResultBase):
    """
     Supports random access 
    """
    def Reset(self):
        ...
    def __getitem__(self, idx):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __len__(self):
        ...
    def __next__(self):
        ...
    def _finish(self):
        ...
    def next(self):
        ...

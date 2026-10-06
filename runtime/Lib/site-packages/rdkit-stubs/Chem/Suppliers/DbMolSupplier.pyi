"""

Supplies a class for working with molecules from databases
"""
from __future__ import annotations
from rdkit import Chem
import rdkit.Chem.Suppliers.MolSupplier
from rdkit.Chem.Suppliers.MolSupplier import MolSupplier
import sys as sys
__all__: list[str] = ['Chem', 'DbMolSupplier', 'ForwardDbMolSupplier', 'MolSupplier', 'RandomAccessDbMolSupplier', 'sys', 'warning']
class DbMolSupplier(rdkit.Chem.Suppliers.MolSupplier.MolSupplier):
    """
    
        new molecules come back with all additional fields from the
        database set in a "_fieldsFromDb" data member
    
      
    """
    def GetColumnNames(self):
        ...
    def _BuildMol(self, data):
        ...
    def __init__(self, dbResults, molColumnFormats = {'SMILES': 'SMI', 'SMI': 'SMI', 'MOLPKL': 'PKL'}, nameCol = '', transformFunc = None, **kwargs):
        """
        
        
              DbResults should be a subclass of Dbase.DbResultSet.DbResultBase
        
            
        """
class ForwardDbMolSupplier(DbMolSupplier):
    """
     DbMol supplier supporting only forward iteration
    
    
        new molecules come back with all additional fields from the
        database set in a "_fieldsFromDb" data member
    
      
    """
    def NextMol(self):
        """
        
        
              NOTE: this has side effects
        
            
        """
    def Reset(self):
        ...
    def __init__(self, dbResults, **kwargs):
        """
        
        
              DbResults should be an iterator for Dbase.DbResultSet.DbResultBase
        
            
        """
class RandomAccessDbMolSupplier(DbMolSupplier):
    def NextMol(self):
        ...
    def Reset(self):
        ...
    def __getitem__(self, idx):
        ...
    def __init__(self, dbResults, **kwargs):
        """
        
        
              DbResults should be a Dbase.DbResultSet.RandomAccessDbResultSet
        
            
        """
    def __len__(self):
        ...
def warning(msg, dest = ...):
    ...

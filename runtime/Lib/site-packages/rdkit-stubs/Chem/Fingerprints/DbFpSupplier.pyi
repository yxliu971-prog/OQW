"""
 Supplies a class for working with fingerprints from databases
#DOC

"""
from __future__ import annotations
import pickle as pickle
from rdkit import DataStructs
import rdkit.VLib.Node
from rdkit.VLib.Node import VLibNode
__all__: list[str] = ['DataStructs', 'DbFpSupplier', 'ForwardDbFpSupplier', 'RandomAccessDbFpSupplier', 'VLibNode', 'pickle']
class DbFpSupplier(rdkit.VLib.Node.VLibNode):
    """
    
          new fps come back with all additional fields from the
          database set in a "_fieldsFromDb" data member
    
        
    """
    def GetColumnNames(self):
        ...
    def _BuildFp(self, data):
        ...
    def __init__(self, dbResults, fpColName = 'AutoFragmentFp', usePickles = True):
        """
        
        
                  DbResults should be a subclass of Dbase.DbResultSet.DbResultBase
        
                
        """
    def __next__(self):
        ...
    def next(self):
        ...
class ForwardDbFpSupplier(DbFpSupplier):
    """
     DbFp supplier supporting only forward iteration
    
        >>> from rdkit import RDConfig
        >>> from rdkit.Dbase.DbConnection import DbConnect
        >>> fName = RDConfig.RDTestDatabase
        >>> conn = DbConnect(fName,'simple_combined')
        >>> suppl = ForwardDbFpSupplier(conn.GetData())
    
        we can loop over the supplied fingerprints:
        
        >>> fps = []
        >>> for fp in suppl:
        ...   fps.append(fp)
        >>> len(fps)
        12
    
        
    """
    def NextItem(self):
        """
        
        
                  NOTE: this has side effects
        
                
        """
    def __init__(self, *args, **kwargs):
        ...
    def reset(self):
        ...
class RandomAccessDbFpSupplier(DbFpSupplier):
    """
     DbFp supplier supporting random access:
    
      >>> import os.path
      >>> from rdkit import RDConfig
      >>> from rdkit.Dbase.DbConnection import DbConnect
      >>> fName = RDConfig.RDTestDatabase
      >>> conn = DbConnect(fName,'simple_combined')
      >>> suppl = RandomAccessDbFpSupplier(conn.GetData())
      >>> len(suppl)
      12
    
      we can pull individual fingerprints:
    
      >>> fp = suppl[5]
      >>> fp.GetNumBits()
      128
      >>> fp.GetNumOnBits()
      54
    
      a standard loop over the fingerprints:
    
      >>> fps = []
      >>> for fp in suppl:
      ...   fps.append(fp)
      >>> len(fps)
      12
    
      or we can use an indexed loop:
    
      >>> fps = [None] * len(suppl)
      >>> for i in range(len(suppl)):
      ...   fps[i] = suppl[i]
      >>> len(fps)
      12
    
      
    """
    def NextItem(self):
        ...
    def __getitem__(self, idx):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __len__(self):
        ...
    def reset(self):
        ...
def _runDoctests(verbose = None):
    ...

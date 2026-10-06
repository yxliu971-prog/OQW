"""
 This functionality gets mixed into the BitEnsemble class

"""
from __future__ import annotations
from rdkit.DataStructs.BitEnsemble import BitEnsemble
__all__: list[str] = ['BitEnsemble']
def _InitScoreTable(self, dbConn, tableName, idInfo = '', actInfo = ''):
    """
     inializes a db table to store our scores
    
        idInfo and actInfo should be strings with the definitions of the id and
        activity columns of the table (when desired)
    
      
    """
def _ScoreToDb(self, sig, dbConn, tableName = None, id = None, act = None):
    """
     scores the "signature" that is passed in and puts the
      results in the db table
    
      
    """

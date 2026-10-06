from __future__ import annotations
import os as os
from rdkit import Chem
from rdkit.Chem.Suppliers import DbMolSupplier
from rdkit import RDConfig
import rdkit.VLib.Supply
from rdkit.VLib.Supply import SupplyNode
import sys as sys
__all__: list[str] = ['Chem', 'DbMolSupplier', 'DbMolSupplyNode', 'GetNode', 'RDConfig', 'SupplyNode', 'os', 'sys']
class DbMolSupplyNode(rdkit.VLib.Supply.SupplyNode):
    """
     Supplies molecules from a db result set:
    
      Sample Usage:
        >>> from rdkit.Dbase.DbConnection import DbConnect
        >>> dbName = os.path.join(RDConfig.RDCodeDir,'Chem','Fingerprints',                             'test_data','data.gdb')
        >>> conn = DbConnect(dbName,'simple_mols')
        >>> dataset = conn.GetData()
        >>> suppl = DbMolSupplyNode(dataset)
        >>> ms = [x for x in suppl]
        >>> len(ms)
        12
        >>> ms[0].GetProp("ID")
        'ether-1'
        >>> ms[10].GetProp("ID")
        'acid-4'
        >>> suppl.reset()
        >>> suppl.next().GetProp("ID")
        'ether-1'
        >>> suppl.next().GetProp("ID")
        'acid-1'
        >>> suppl.reset()
      
      
    """
    def __init__(self, dbResults, **kwargs):
        ...
    def next(self):
        """
        
        
            
        """
    def reset(self):
        ...
def GetNode(dbName, tableName):
    ...
def _test():
    ...

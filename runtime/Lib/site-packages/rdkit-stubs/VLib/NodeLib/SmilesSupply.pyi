from __future__ import annotations
from rdkit import Chem
import rdkit.VLib.Supply
from rdkit.VLib.Supply import SupplyNode
__all__: list[str] = ['Chem', 'SmilesSupplyNode', 'SupplyNode']
class SmilesSupplyNode(rdkit.VLib.Supply.SupplyNode):
    """
     Smiles supplier
    
        Sample Usage:
          >>> import os
          >>> from rdkit import RDConfig
          >>> fileN = os.path.join(RDConfig.RDCodeDir,'VLib','NodeLib',                               'test_data','pgp_20.txt')
          >>> suppl = SmilesSupplyNode(fileN,delim="\\t",smilesColumn=2,nameColumn=1,titleLine=1)
          >>> ms = [x for x in suppl]
          >>> len(ms)
          20
          >>> ms[0].GetProp("_Name")
          'ALDOSTERONE'
          >>> ms[0].GetProp("ID")
          'RD-PGP-0001'
          >>> ms[1].GetProp("_Name")
          'AMIODARONE'
          >>> ms[3].GetProp("ID")
          'RD-PGP-0004'
          >>> suppl.reset()
          >>> suppl.next().GetProp("_Name")
          'ALDOSTERONE'
          >>> suppl.next().GetProp("_Name")
          'AMIODARONE'
          >>> suppl.reset()
    
        
    """
    def __init__(self, fileName, delim = '\t', nameColumn = 1, smilesColumn = 0, titleLine = 0, **kwargs):
        ...
    def __next__(self):
        """
        
        
                
        """
    def next(self):
        """
        
        
                
        """
    def reset(self):
        ...
def _runDoctests(verbose = None):
    ...

from __future__ import annotations
from rdkit import Chem
import rdkit.VLib.Supply
from rdkit.VLib.Supply import SupplyNode
__all__: list[str] = ['Chem', 'SDSupplyNode', 'SupplyNode']
class SDSupplyNode(rdkit.VLib.Supply.SupplyNode):
    """
     SD supplier
    
        Sample Usage:
          >>> import os
          >>> from rdkit import RDConfig
          >>> fileN = os.path.join(RDConfig.RDCodeDir,'VLib','NodeLib',                               'test_data','NCI_aids.10.sdf')
          >>> suppl = SDSupplyNode(fileN)
          >>> ms = [x for x in suppl]
          >>> len(ms)
          10
          >>> ms[0].GetProp("_Name")
          '48'
          >>> ms[1].GetProp("_Name")
          '78'
          >>> suppl.reset()
          >>> suppl.next().GetProp("_Name")
          '48'
          >>> suppl.next().GetProp("_Name")
          '78'
    
        
    """
    def __init__(self, fileName, **kwargs):
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

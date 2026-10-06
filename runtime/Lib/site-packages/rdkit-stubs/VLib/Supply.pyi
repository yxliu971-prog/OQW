from __future__ import annotations
import rdkit.VLib.Node
from rdkit.VLib.Node import VLibNode
__all__: list[str] = ['SupplyNode', 'VLibNode']
class SupplyNode(rdkit.VLib.Node.VLibNode):
    """
     base class for nodes which supply things
    
        Assumptions:
          1) no parents
    
        Usage Example:
        
          >>> supplier = SupplyNode(contents=[1,2,3])
          >>> supplier.next()
          1
          >>> supplier.next()
          2
          >>> supplier.next()
          3
          >>> supplier.next()
          Traceback (most recent call last):
              ...
          StopIteration
          >>> supplier.reset()
          >>> supplier.next()
          1
          >>> [x for x in supplier]
          [1, 2, 3]
    
    
        
    """
    def AddParent(self, parent, notify = 1):
        ...
    def __init__(self, contents = None, **kwargs):
        ...
    def __next__(self):
        ...
    def next(self):
        ...
    def reset(self):
        ...
def _runDoctests(verbose = None):
    ...

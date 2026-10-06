from __future__ import annotations
from rdkit import Chem
import rdkit.VLib.Output
from rdkit.VLib.Output import OutputNode as BaseOutputNode
__all__: list[str] = ['BaseOutputNode', 'Chem', 'OutputNode']
class OutputNode(rdkit.VLib.Output.OutputNode):
    """
     dumps smiles output
    
        Assumptions:
    
          - destination supports a write() method
    
          - inputs (parents) can be stepped through in lockstep
    
    
        Usage Example:
          >>> smis = ['C1CCC1','C1CC1','C=O','NCC']
          >>> mols = [Chem.MolFromSmiles(x) for x in smis]
          >>> from rdkit.VLib.Supply import SupplyNode
          >>> suppl = SupplyNode(contents=mols)
          >>> from io import StringIO
          >>> sio = StringIO()
          >>> node = OutputNode(dest=sio,delim=', ')
          >>> node.AddParent(suppl)
          >>> ms = [x for x in node]
          >>> len(ms)
          4
          >>> txt = sio.getvalue()
          >>> repr(txt)
          "'1, C1CCC1\\\\n2, C1CC1\\\\n3, C=O\\\\n4, CCN\\\\n'"
    
        
    """
    def __init__(self, dest = None, delim = '\t', idField = None, **kwargs):
        ...
    def reset(self):
        ...
    def smilesOut(self, mol):
        ...
def _runDoctests(verbose = None):
    ...

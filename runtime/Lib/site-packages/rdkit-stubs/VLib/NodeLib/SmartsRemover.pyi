from __future__ import annotations
from rdkit import Chem
import rdkit.VLib.Transform
from rdkit.VLib.Transform import TransformNode
__all__: list[str] = ['Chem', 'SmartsRemover', 'TransformNode', 'biggerTest']
class SmartsRemover(rdkit.VLib.Transform.TransformNode):
    """
     transforms molecules by removing atoms matching smarts patterns
    
      Assumptions:
    
        - inputs are molecules
    
    
      Sample Usage:
        >>> smis = ['C1CCC1.C=O','C1CCC1C=O','CCC=O.C=O','NCC=O.C=O.CN']
        >>> mols = [Chem.MolFromSmiles(x) for x in smis]
        >>> from rdkit.VLib.Supply import SupplyNode
        >>> suppl = SupplyNode(contents=mols)
        >>> ms = [x for x in suppl]
        >>> len(ms)
        4
    
        We can pass in SMARTS strings:
        >>> smas = ['C=O','CN']
        >>> tform = SmartsRemover(patterns=smas)
        >>> tform.AddParent(suppl)
        >>> ms = [x for x in tform]
        >>> len(ms)
        4
        >>> Chem.MolToSmiles(ms[0])
        'C1CCC1'
        >>> Chem.MolToSmiles(ms[1])
        'O=CC1CCC1'
        >>> Chem.MolToSmiles(ms[2])
        'CCC=O'
        >>> Chem.MolToSmiles(ms[3])
        'NCC=O'
    
        We can also remove pieces of the molecule that are not complete
        fragments:
        >>> tform.Destroy()
        >>> smas = ['C=O','CN']
        >>> smas = [Chem.MolFromSmarts(x) for x in smas]
        >>> tform = SmartsRemover(patterns=smas,wholeFragments=0)
        >>> tform.AddParent(suppl)
        >>> ms = [x for x in tform]
        >>> len(ms)
        4
        >>> Chem.MolToSmiles(ms[0])
        'C1CCC1'
        >>> Chem.MolToSmiles(ms[1])
        'C1CCC1'
        >>> Chem.MolToSmiles(ms[3])
        ''
    
        Or patterns themselves:
        >>> tform.Destroy()
        >>> smas = ['C=O','CN']
        >>> smas = [Chem.MolFromSmarts(x) for x in smas]
        >>> tform = SmartsRemover(patterns=smas)
        >>> tform.AddParent(suppl)
        >>> ms = [x for x in tform]
        >>> len(ms)
        4
        >>> Chem.MolToSmiles(ms[0])
        'C1CCC1'
        >>> Chem.MolToSmiles(ms[3])
        'NCC=O'
    
    
      
    """
    def __init__(self, patterns = list(), wholeFragments = 1, **kwargs):
        ...
    def _initPatterns(self, patterns):
        ...
    def transform(self, cmpd):
        ...
def _runDoctests(verbose = None):
    ...
__test__: dict = {'bigger': "\n>>> smis = ['CCOC','CCO.Cl','CC(=O)[O-].[Na+]','OCC','C[N+](C)(C)C.[Cl-]']\n>>> mols = [Chem.MolFromSmiles(x) for x in smis]\n>>> from rdkit.VLib.Supply import SupplyNode\n>>> suppl = SupplyNode(contents=mols)\n>>> ms = [x for x in suppl]\n>>> len(ms)\n5\n\n#>>> salts = ['[Cl;H1&X1,-]','[Na+]','[O;H2,H1&-,X0&-2]']\n\n>>> salts = ['[Cl;H1&X1,-]','[Na+]','[O;H2,H1&-,X0&-2]']\n>>> m = mols[2]\n>>> m.GetNumAtoms()\n5\n>>> patts = [Chem.MolFromSmarts(x) for x in salts]\n>>> m2 = Chem.DeleteSubstructs(m,patts[0],1)\n>>> m2.GetNumAtoms()\n5\n>>> m2 = Chem.DeleteSubstructs(m2,patts[1],1)\n>>> m2.GetNumAtoms()\n4\n>>> m2 = Chem.DeleteSubstructs(m2,patts[2],1)\n>>> m2.GetNumAtoms()\n4\n\n>>> tform = SmartsRemover(patterns=salts)\n>>> tform.AddParent(suppl)\n>>> ms = [x for x in tform]\n>>> len(ms)\n5\n\n"}
biggerTest: str = "\n>>> smis = ['CCOC','CCO.Cl','CC(=O)[O-].[Na+]','OCC','C[N+](C)(C)C.[Cl-]']\n>>> mols = [Chem.MolFromSmiles(x) for x in smis]\n>>> from rdkit.VLib.Supply import SupplyNode\n>>> suppl = SupplyNode(contents=mols)\n>>> ms = [x for x in suppl]\n>>> len(ms)\n5\n\n#>>> salts = ['[Cl;H1&X1,-]','[Na+]','[O;H2,H1&-,X0&-2]']\n\n>>> salts = ['[Cl;H1&X1,-]','[Na+]','[O;H2,H1&-,X0&-2]']\n>>> m = mols[2]\n>>> m.GetNumAtoms()\n5\n>>> patts = [Chem.MolFromSmarts(x) for x in salts]\n>>> m2 = Chem.DeleteSubstructs(m,patts[0],1)\n>>> m2.GetNumAtoms()\n5\n>>> m2 = Chem.DeleteSubstructs(m2,patts[1],1)\n>>> m2.GetNumAtoms()\n4\n>>> m2 = Chem.DeleteSubstructs(m2,patts[2],1)\n>>> m2.GetNumAtoms()\n4\n\n>>> tform = SmartsRemover(patterns=salts)\n>>> tform.AddParent(suppl)\n>>> ms = [x for x in tform]\n>>> len(ms)\n5\n\n"

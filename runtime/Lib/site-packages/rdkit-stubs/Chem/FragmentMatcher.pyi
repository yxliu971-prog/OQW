"""
Exposes a class for matching fragments of molecules.

The class exposes a simple API:

If you want a matcher that hits C=O, you'd do:

>>> p = FragmentMatcher()
>>> p.Init('C=O')

you can then match with:

>>> mol = Chem.MolFromSmiles('CC(=O)O')
>>> p.HasMatch(mol)
1
>>> p.HasMatch(Chem.MolFromSmiles('CC(C)C'))
0

information about the matches:

>>> len(p.GetMatches(Chem.MolFromSmiles('CC=O')))
1
>>> len(p.GetMatches(Chem.MolFromSmiles('O=CC=O')))
2

or, you can add exclusion fragments (defined as smarts) with:

>>> p.AddExclusion('c1ccccc1')

now the matcher will not hit anything that has a benzene ring.

>>> p.HasMatch(Chem.MolFromSmiles('CC=O'))
1
>>> p.HasMatch(Chem.MolFromSmiles('c1ccccc1CC=O'))
0


"""
from __future__ import annotations
from rdkit import Chem
__all__: list[str] = ['Chem', 'FragmentMatcher']
class FragmentMatcher:
    def AddExclusion(self, sma):
        ...
    def GetBond(self, idx):
        ...
    def GetExclusionSMARTS(self):
        ...
    def GetMatch(self, mol):
        ...
    def GetMatches(self, mol, uniquify = 1):
        ...
    def GetSMARTS(self):
        ...
    def HasMatch(self, mol):
        ...
    def Init(self, sma):
        ...
    def __init__(self):
        ...
def _test():
    ...

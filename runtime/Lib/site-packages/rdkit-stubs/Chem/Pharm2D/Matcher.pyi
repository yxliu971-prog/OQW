"""
 functionality for finding pharmacophore matches in molecules


  See Docs/Chem/Pharm2D.triangles.jpg for an illustration of the way
  pharmacophores are broken into triangles and labelled.

  See Docs/Chem/Pharm2D.signatures.jpg for an illustration of bit
  numbering

"""
from __future__ import annotations
from rdkit import Chem
from rdkit.Chem.Pharm2D import Utils
__all__: list[str] = ['Chem', 'GetAtomsMatchingBit', 'MatchError', 'Utils']
class MatchError(Exception):
    pass
def GetAtomsMatchingBit(sigFactory, bitIdx, mol, dMat = None, justOne = 0, matchingAtoms = None):
    """
     Returns a list of lists of atom indices for a bit
    
        **Arguments**
    
          - sigFactory: a SigFactory
    
          - bitIdx: the bit to be queried
    
          - mol: the molecule to be examined
    
          - dMat: (optional) the distance matrix of the molecule
    
          - justOne: (optional) if this is nonzero, only the first match
            will be returned.
    
          - matchingAtoms: (optional) if this is nonzero, it should
            contain a sequence of sequences with the indices of atoms in
            the molecule which match each of the patterns used by the
            signature.
    
        **Returns**
    
          a list of tuples with the matching atoms
      
    """
def _exampleCode():
    ...
_verbose: int = 0

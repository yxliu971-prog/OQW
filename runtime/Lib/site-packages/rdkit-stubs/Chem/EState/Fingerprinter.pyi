"""
  EState fingerprinting

"""
from __future__ import annotations
import numpy as numpy
from rdkit.Chem.EState import AtomTypes
from rdkit.Chem.EState.EState import EStateIndices
__all__: list[str] = ['AtomTypes', 'EStateIndices', 'FingerprintMol', 'numpy']
def FingerprintMol(mol):
    """
     generates the EState fingerprints for the molecule
    
      Concept from the paper: Hall and Kier JCICS _35_ 1039-1045 (1995)
    
      two numeric arrays are returned:
        The first (of ints) contains the number of times each possible atom type is hit
        The second (of floats) contains the sum of the EState indices for atoms of
          each type.
    
      
    """
def _exampleCode():
    """
     Example code for calculating E-state fingerprints 
    """

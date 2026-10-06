"""
 Python functions for manipulating molecular graphs

In theory much of the functionality in here should be migrating into the
C/C++ codebase.

"""
from __future__ import annotations
import numpy as numpy
from rdkit import Chem
from rdkit import DataStructs
import types as types
__all__: list[str] = ['CharacteristicPolynomial', 'Chem', 'DataStructs', 'numpy', 'types']
def CharacteristicPolynomial(mol, mat = None):
    """
     calculates the characteristic polynomial for a molecular graph
    
          if mat is not passed in, the molecule's Weighted Adjacency Matrix will
          be used.
    
          The approach used is the Le Verrier-Faddeev-Frame method described
          in _Chemical Graph Theory, 2nd Edition_ by Nenad Trinajstic (CRC Press,
          1992), pg 76.
    
        
    """

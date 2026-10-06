"""
Module containing an assortment of functionality for basic data structures.

At the moment the data structures defined are:
  Bit Vector classes (for storing signatures, fingerprints and the like:
    - ExplicitBitVect: class for relatively small (10s of thousands of bits) or
                       dense bit vectors.
    - SparseBitVect:   class for large, sparse bit vectors
  DiscreteValueVect:   class for storing vectors of integers
  SparseIntVect:       class for storing sparse vectors of integers
"""
from __future__ import annotations
import math as math
from rdkit.DataStructs.cDataStructs import DiscreteValueType
from rdkit.DataStructs.cDataStructs import DiscreteValueVect
from rdkit.DataStructs.cDataStructs import ExplicitBitVect
from rdkit.DataStructs.cDataStructs import FPBReader
from rdkit.DataStructs.cDataStructs import IntSparseIntVect
from rdkit.DataStructs.cDataStructs import LongSparseIntVect
from rdkit.DataStructs.cDataStructs import MultiFPBReader
from rdkit.DataStructs.cDataStructs import RealValueVect
from rdkit.DataStructs.cDataStructs import SparseBitVect
from rdkit.DataStructs.cDataStructs import UIntSparseIntVect
from rdkit.DataStructs.cDataStructs import ULongSparseIntVect
from rdkit import rdBase
from .cDataStructs import *
__all__: list[str] = ['DiscreteValueType', 'DiscreteValueVect', 'EIGHTBITVALUE', 'ExplicitBitVect', 'FOURBITVALUE', 'FPBReader', 'FingerprintSimilarity', 'FoldToTargetDensity', 'IntSparseIntVect', 'LongSparseIntVect', 'MultiFPBReader', 'ONEBITVALUE', 'RealValueVect', 'SIXTEENBITVALUE', 'SparseBitVect', 'TWOBITVALUE', 'UIntSparseIntVect', 'ULongSparseIntVect', 'cDataStructs', 'getElementFromFlatMatrix', 'getNForFlatMatrix', 'math', 'rdBase', 'similarityFunctions']
def FingerprintSimilarity(fp1, fp2, metric = ...):
    """
     returns the calculated similarity between two fingerprints,
          handles any folding that may need to be done to ensure that they
          are compatible
    
        
    """
def FoldToTargetDensity(fp, density = 0.3, minLength = 64):
    ...
def getElementFromFlatMatrix(matrix, i, j):
    """
    Return element (i,j); diagonal is 0; lower side mirrors upper.
    """
def getNForFlatMatrix(matrix):
    """
    Get n for a strict upper- (or lower-) triangular matrix.
    """
EIGHTBITVALUE: cDataStructs.DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.EIGHTBITVALUE
FOURBITVALUE: cDataStructs.DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.FOURBITVALUE
ONEBITVALUE: cDataStructs.DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.ONEBITVALUE
SIXTEENBITVALUE: cDataStructs.DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.SIXTEENBITVALUE
TWOBITVALUE: cDataStructs.DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE
similarityFunctions: list  # value = [('Tanimoto', <Boost.Python.function object>, ''), ('Dice', <Boost.Python.function object>, ''), ('Cosine', <Boost.Python.function object>, ''), ('Sokal', <Boost.Python.function object>, ''), ('Russel', <Boost.Python.function object>, ''), ('RogotGoldberg', <Boost.Python.function object>, ''), ('AllBit', <Boost.Python.function object>, ''), ('Kulczynski', <Boost.Python.function object>, ''), ('McConnaughey', <Boost.Python.function object>, ''), ('Asymmetric', <Boost.Python.function object>, ''), ('BraunBlanquet', <Boost.Python.function object>, '')]

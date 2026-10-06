"""
 Functionality for ranking bits using info gains

 **Definitions used in this module**

    - *sequence*: an object capable of containing other objects which supports
      __getitem__() and __len__().  Examples of these include lists, tuples, and
      Numeric arrays.

    - *IntVector*: an object containing integers which supports __getitem__() and
       __len__(). Examples include lists, tuples, Numeric Arrays, and BitVects.


 **NOTE**: Neither *sequences* nor *IntVectors* need to support item assignment.
   It is perfectly acceptable for them to be read-only, so long as they are
   random-access.

"""
from __future__ import annotations
import numpy as numpy
from rdkit.ML.InfoTheory import entropy
__all__: list[str] = ['AnalyzeSparseVects', 'CalcInfoGains', 'FormCounts', 'RankBits', 'SparseRankBits', 'entropy', 'numpy']
def AnalyzeSparseVects(bitVects, actVals):
    """
     #DOC
    
      **Arguments**
    
        - bitVects: a *sequence* containing SBVs
    
        - actVals: a *sequence*
    
       **Returns**
    
         a list of floats
    
       **Notes**
    
          - these need to be bit vects and binary activities
    
      
    """
def CalcInfoGains(bitVects, actVals, nPossibleActs, nPossibleBitVals = 2):
    """
      Calculates the information gain for a set of points and activity values
    
      **Arguments**
    
        - bitVects: a *sequence* containing *IntVectors*
    
        - actVals: a *sequence*
    
        - nPossibleActs: the (integer) number of possible activity values.
    
        - nPossibleBitVals: (optional) if specified, this integer provides the maximum
          value attainable by the (increasingly inaccurately named) bits in _bitVects_.
    
       **Returns**
    
         a list of floats
    
      
    """
def FormCounts(bitVects, actVals, whichBit, nPossibleActs, nPossibleBitVals = 2):
    """
     generates the counts matrix for a particular bit
    
      **Arguments**
    
        - bitVects: a *sequence* containing *IntVectors*
    
        - actVals: a *sequence*
    
        - whichBit: an integer, the bit number to use.
    
        - nPossibleActs: the (integer) number of possible activity values.
    
        - nPossibleBitVals: (optional) if specified, this integer provides the maximum
          value attainable by the (increasingly inaccurately named) bits in _bitVects_.
    
      **Returns**
    
        a Numeric array with the counts
    
      **Notes**
    
        This is really intended for internal use.
    
      
    """
def RankBits(bitVects, actVals, nPossibleBitVals = 2, metricFunc = CalcInfoGains):
    """
     Rank a set of bits according to a metric function
    
      **Arguments**
    
        - bitVects: a *sequence* containing *IntVectors*
    
        - actVals: a *sequence*
    
        - nPossibleBitVals: (optional) if specified, this integer provides the maximum
          value attainable by the (increasingly inaccurately named) bits in _bitVects_.
    
        - metricFunc: (optional) the metric function to be used.  See _CalcInfoGains()_
          for a description of the signature of this function.
    
       **Returns**
    
         A 2-tuple containing:
    
           - the relative order of the bits (a list of ints)
    
           - the metric calculated for each bit (a list of floats)
    
      
    """
def SparseRankBits(bitVects, actVals, metricFunc = AnalyzeSparseVects):
    """
     Rank a set of bits according to a metric function
    
      **Arguments**
    
        - bitVects: a *sequence* containing SBVs
    
        - actVals: a *sequence*
    
        - metricFunc: (optional) the metric function to be used.  See _SparseCalcInfoGains()_
          for a description of the signature of this function.
    
       **Returns**
    
         A 2-tuple containing:
    
           - the relative order of the bits (a list of ints)
    
           - the metric calculated for each bit (a list of floats)
    
        **Notes**
    
          - these need to be bit vects and binary activities
    
      
    """

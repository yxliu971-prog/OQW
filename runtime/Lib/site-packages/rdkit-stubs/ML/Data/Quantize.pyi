"""
 Automatic search for quantization bounds

This uses the expected informational gain to determine where quantization bounds should
lie.

**Notes**:

  - bounds are less than, so if the bounds are [1.,2.],
    [0.9,1.,1.1,2.,2.2] -> [0,1,1,2,2]

"""
from __future__ import annotations
import numpy as numpy
from rdkit.ML.Data import cQuantize
from rdkit.ML.InfoTheory import entropy
__all__: list[str] = ['FindVarMultQuantBounds', 'FindVarQuantBound', 'cQuantize', 'entropy', 'feq', 'hascQuantize', 'numpy']
def FindVarMultQuantBounds(vals, nBounds, results, nPossibleRes):
    """
     finds multiple quantization bounds for a single variable
    
         **Arguments**
    
           - vals: sequence of variable values (assumed to be floats)
    
           - nBounds: the number of quantization bounds to find
    
           - results: a list of result codes (should be integers)
    
           - nPossibleRes: an integer with the number of possible values of the
             result variable
    
         **Returns**
    
           - a 2-tuple containing:
    
             1) a list of the quantization bounds (floats)
    
             2) the information gain associated with this quantization
    
    
        
    """
def FindVarQuantBound(vals, results, nPossibleRes):
    """
     Uses FindVarMultQuantBounds, only here for historic reasons
        
    """
def _GenVarTable(vals, cuts, starts, results, nPossibleRes):
    """
     Primarily intended for internal use
    
         constructs a variable table for the data passed in
         The table for a given variable records the number of times each possible value
          of that variable appears for each possible result of the function.
    
         **Arguments**
    
           - vals: a 1D Numeric array with the values of the variables
    
           - cuts: a list with the indices of the quantization bounds
             (indices are into _starts_ )
    
           - starts: a list of potential starting points for quantization bounds
    
           - results: a 1D Numeric array of integer result codes
    
           - nPossibleRes: an integer with the number of possible result codes
    
         **Returns**
    
           the varTable, a 2D Numeric array which is nVarValues x nPossibleRes
    
         **Notes**
    
           - _vals_ should be sorted!
    
        
    """
def _NewPyFindStartPoints(sortVals, sortResults, nData):
    ...
def _NewPyRecurseOnBounds(vals, cuts, which, starts, results, nPossibleRes, varTable = None):
    """
     Primarily intended for internal use
    
         Recursively finds the best quantization boundaries
    
         **Arguments**
    
           - vals: a 1D Numeric array with the values of the variables,
             this should be sorted
    
           - cuts: a list with the indices of the quantization bounds
             (indices are into _starts_ )
    
           - which: an integer indicating which bound is being adjusted here
             (and index into _cuts_ )
    
           - starts: a list of potential starting points for quantization bounds
    
           - results: a 1D Numeric array of integer result codes
    
           - nPossibleRes: an integer with the number of possible result codes
    
         **Returns**
    
           - a 2-tuple containing:
    
             1) the best information gain found so far
    
             2) a list of the quantization bound indices ( _cuts_ for the best case)
    
         **Notes**
    
          - this is not even remotely efficient, which is why a C replacement
            was written
    
        
    """
def _PyRecurseOnBounds(vals, cuts, which, starts, results, nPossibleRes, varTable = None):
    """
     Primarily intended for internal use
    
         Recursively finds the best quantization boundaries
    
         **Arguments**
    
           - vals: a 1D Numeric array with the values of the variables,
             this should be sorted
    
           - cuts: a list with the indices of the quantization bounds
             (indices are into _starts_ )
    
           - which: an integer indicating which bound is being adjusted here
             (and index into _cuts_ )
    
           - starts: a list of potential starting points for quantization bounds
    
           - results: a 1D Numeric array of integer result codes
    
           - nPossibleRes: an integer with the number of possible result codes
    
         **Returns**
    
           - a 2-tuple containing:
    
             1) the best information gain found so far
    
             2) a list of the quantization bound indices ( _cuts_ for the best case)
    
         **Notes**
    
          - this is not even remotely efficient, which is why a C replacement
            was written
    
        
    """
def feq(v1, v2, tol = 1e-08):
    """
     floating point equality with a tolerance factor
    
          **Arguments**
    
            - v1: a float
    
            - v2: a float
    
            - tol: the tolerance for comparison
    
          **Returns**
    
            0 or 1
    
        
    """
_float_tol: float = 1e-08
hascQuantize: int = 1

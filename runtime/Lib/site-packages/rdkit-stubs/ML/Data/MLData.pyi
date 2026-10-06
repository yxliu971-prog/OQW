"""
 classes to be used to help work with data sets

"""
from __future__ import annotations
import copy as copy
import math as math
import numpy as numpy
__all__: list[str] = ['MLDataSet', 'MLQuantDataSet', 'copy', 'math', 'numericTypes', 'numpy']
class MLDataSet:
    """
     A data set for holding general data (floats, ints, and strings)
    
         **Note**
           this is intended to be a read-only data structure
           (i.e. after calling the constructor you cannot touch it)
        
    """
    def AddPoint(self, pt):
        ...
    def AddPoints(self, pts, names):
        ...
    def GetAllData(self):
        """
         returns a *copy* of the data
        
                
        """
    def GetInputData(self):
        """
         returns the input data
        
                 **Note**
        
                   _inputData_ means the examples without their result fields
                    (the last _NResults_ entries)
        
                
        """
    def GetNPossibleVals(self):
        ...
    def GetNPts(self):
        ...
    def GetNResults(self):
        ...
    def GetNVars(self):
        ...
    def GetNamedData(self):
        """
         returns a list of named examples
        
                 **Note**
        
                   a named example is the result of prepending the example
                    name to the data list
        
                
        """
    def GetPtNames(self):
        ...
    def GetQuantBounds(self):
        ...
    def GetResults(self):
        """
         Returns the result fields from each example
        
                
        """
    def GetVarNames(self):
        ...
    def _CalcNPossible(self, data):
        """
        calculates the number of possible values of each variable (where possible)
        
                  **Arguments**
        
                     -data: a list of examples to be used
        
                  **Returns**
        
                     a list of nPossible values for each variable
        
                
        """
    def __getitem__(self, idx):
        ...
    def __init__(self, data, nVars = None, nPts = None, nPossibleVals = None, qBounds = None, varNames = None, ptNames = None, nResults = 1):
        """
         Constructor
        
                  **Arguments**
        
                    - data: a list of lists containing the data. The data are copied, so don't worry
                          about us overwriting them.
        
                    - nVars: the number of variables
        
                    - nPts: the number of points
        
                    - nPossibleVals: an list containing the number of possible values
                                   for each variable (should contain 0 when not relevant)
                                   This is _nVars_ long
        
                    - qBounds: a list of lists containing quantization bounds for variables
                             which are to be quantized (note, this class does not quantize
                             the variables itself, it merely stores quantization bounds.
                             an empty sublist indicates no quantization for a given variable
                             This is _nVars_ long
        
                    - varNames: a list of the names of the variables.
                             This is _nVars_ long
        
                    - ptNames: the names (labels) of the individual data points
                       This is _nPts_ long
        
                    - nResults: the number of results columns in the data lists.  This is usually
                                1, but can be higher.
                
        """
    def __setitem__(self, idx, val):
        ...
class MLQuantDataSet(MLDataSet):
    """
     a data set for holding quantized data
    
    
          **Note**
    
            this is intended to be a read-only data structure
            (i.e. after calling the constructor you cannot touch it)
    
          **Big differences to MLDataSet**
    
            1) data are stored in a numpy array since they are homogenous
    
            2) results are assumed to be quantized (i.e. no qBounds entry is required)
    
        
    """
    def GetAllData(self):
        """
         returns a *copy* of the data
        
                
        """
    def GetInputData(self):
        """
         returns the input data
        
                 **Note**
        
                   _inputData_ means the examples without their result fields
                    (the last _NResults_ entries)
        
                
        """
    def GetNamedData(self):
        """
         returns a list of named examples
        
                 **Note**
        
                   a named example is the result of prepending the example
                    name to the data list
        
                
        """
    def GetResults(self):
        """
         Returns the result fields from each example
        
                
        """
    def _CalcNPossible(self, data):
        """
        calculates the number of possible values of each variable
        
                  **Arguments**
        
                     -data: a list of examples to be used
        
                  **Returns**
        
                     a list of nPossible values for each variable
        
                
        """
    def __init__(self, data, nVars = None, nPts = None, nPossibleVals = None, qBounds = None, varNames = None, ptNames = None, nResults = 1):
        """
         Constructor
        
                  **Arguments**
        
                    - data: a list of lists containing the data. The data are copied, so don't worry
                          about us overwriting them.
        
                    - nVars: the number of variables
        
                    - nPts: the number of points
        
                    - nPossibleVals: an list containing the number of possible values
                                   for each variable (should contain 0 when not relevant)
                                   This is _nVars_ long
        
                    - qBounds: a list of lists containing quantization bounds for variables
                             which are to be quantized (note, this class does not quantize
                             the variables itself, it merely stores quantization bounds.
                             an empty sublist indicates no quantization for a given variable
                             This is _nVars_ long
        
                    - varNames: a list of the names of the variables.
                             This is _nVars_ long
        
                    - ptNames: the names (labels) of the individual data points
                       This is _nPts_ long
        
                    - nResults: the number of results columns in the data lists.  This is usually
                                1, but can be higher.
                
        """
numericTypes: tuple = (int, float)

"""
 Generic file manipulation stuff

"""
from __future__ import annotations
import numpy as numpy
import re as re
__all__: list[str] = ['ReFile', 'ReadDataFile', 'numpy', 're']
class ReFile:
    """
    convenience class for dealing with files with comments
    
      blank (all whitespace) lines, and lines beginning with comment
        characters are skipped.
    
      anything following a comment character on a line is stripped off
      
    """
    def __init__(self, fileName, mode = 'r', comment = '#', trailer = '\\n'):
        ...
    def readline(self):
        """
         read the next line and return it.
        
            return '' on EOF
        
            
        """
    def readlines(self):
        """
         return a list of all the lines left in the file
        
            return [] if there are none
        
            
        """
    def rewind(self):
        """
         rewinds the file (seeks to the beginning)
        
            
        """
def ReadDataFile(fileName, comment = '#', depVarCol = 0, dataType = float):
    """
     read in the data file and return a tuple of two Numeric arrays:
      (independent variables, dependant variables).
    
      **ARGUMENTS:**
    
      - fileName: the fileName
    
      - comment: the comment character for the file
    
      - depVarcol: the column number containing the dependant variable
    
      - dataType: the Numeric short-hand for the data type
    
      RETURNS:
    
       a tuple of two Numeric arrays:
    
        (independent variables, dependant variables).
    
      
    """

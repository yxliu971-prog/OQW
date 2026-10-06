"""
 utility functions to help work with files

"""
from __future__ import annotations
__all__: list[str] = ['MoveToMatchingLine', 'NoMatchFoundError']
class NoMatchFoundError(RuntimeError):
    pass
def MoveToMatchingLine(inFile, matchStr, fullMatch = 0):
    """
     skip forward in a file until a given string is found
    
         **Arguments**
    
           - inFile: a file object (or anything supporting a _readline()_ method)
    
           - matchStr: the string to search for
    
           - fullMatch: if nonzero, _matchStr_ must match the entire line
    
         **Returns**
    
           the matching line
    
         **Notes:**
    
           - if _matchStr_ is not found in the file, a NoMatchFound exception
             will be raised
    
      
    """

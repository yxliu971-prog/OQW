from __future__ import annotations
import bisect as bisect
__all__: list[str] = ['TopNContainer', 'bisect']
class TopNContainer:
    """
     maintains a sorted list of a particular number of data elements.
    
      
    """
    def GetExtras(self):
        """
         returns our set of extras 
        """
    def GetPts(self):
        """
         returns our set of points 
        """
    def Insert(self, val, extra = None):
        """
         only does the insertion if val fits 
        """
    def __getitem__(self, which):
        ...
    def __init__(self, size, mostNeg = -1e+99):
        """
        
            if size is negative, all entries will be kept in sorted order
            
        """
    def __len__(self):
        ...
    def reverse(self):
        ...
def _exampleCode():
    ...

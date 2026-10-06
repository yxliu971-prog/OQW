"""
 Various bits and pieces for calculating descriptors

"""
from __future__ import annotations
import pickle as pickle
__all__: list[str] = ['DescriptorCalculator', 'pickle']
class DescriptorCalculator:
    """
     abstract base class for descriptor calculators
    
      
    """
    def CalcDescriptors(self, what, *args, **kwargs):
        ...
    def GetDescriptorNames(self):
        """
         returns a list of the names of the descriptors this calculator generates
        
            
        """
    def SaveState(self, fileName):
        """
         Writes this calculator off to a file so that it can be easily loaded later
        
             **Arguments**
        
               - fileName: the name of the file to be written
        
            
        """
    def ShowDescriptors(self):
        """
         prints out a list of the descriptors
        
            
        """
    def __init__(self, *args, **kwargs):
        """
         Constructor
        
            
        """

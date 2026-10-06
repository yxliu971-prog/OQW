"""
 Supplies an abstract class for working with sequences of molecules

"""
from __future__ import annotations
__all__: list[str] = ['MolSupplier']
class MolSupplier:
    """
     we must, at minimum, support forward iteration
    
      
    """
    def NextMol(self):
        """
           Must be implemented in child class
        
            
        """
    def Reset(self):
        ...
    def __init__(self):
        ...
    def __iter__(self):
        ...
    def __next__(self):
        ...
    def next(self):
        ...

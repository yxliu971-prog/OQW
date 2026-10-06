"""

Collection of utilities to be used with descriptors

"""
from __future__ import annotations
import math as math
__all__: list[str] = ['VectorDescriptorNamespace', 'VectorDescriptorWrapper', 'math', 'setDescriptorVersion']
class VectorDescriptorNamespace(dict):
    def __init__(self, **kwargs):
        ...
class VectorDescriptorWrapper:
    """
    Wrap a function that returns a vector and make it seem like there
        is one function for each entry.  These functions are added to the global
        namespace with the names provided
    """
    def __init__(self, func, names, version, namespace):
        ...
    def _get_key(self, index):
        ...
    def call_desc(self, mol, index):
        ...
def setDescriptorVersion(version = '1.0.0'):
    """
     Set the version on the descriptor function.
    
      Use as a decorator 
    """

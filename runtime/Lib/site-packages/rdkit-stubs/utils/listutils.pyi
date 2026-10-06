"""
 utility functions for lists

"""
from __future__ import annotations
__all__: list[str] = ['CompactListRepr']
def CompactListRepr(lst):
    """
    
    
      >>> CompactListRepr([0,1,1,1,1,0])
      '[0]+[1]*4+[0]'
      >>> CompactListRepr([0,1,1,2,1,1])
      '[0]+[1]*2+[2]+[1]*2'
      >>> CompactListRepr([])
      '[]'
      >>> CompactListRepr((0,1,1,1,1))
      '[0]+[1]*4'
      >>> CompactListRepr('foo')
      "['f']+['o']*2"
    
      
    """
def _runDoctests(verbose = None):
    ...

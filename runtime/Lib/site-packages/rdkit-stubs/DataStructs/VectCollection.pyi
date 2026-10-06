from __future__ import annotations
import copy as copy
from rdkit import DataStructs
import struct as struct
__all__: list[str] = ['DataStructs', 'VectCollection', 'copy', 'struct']
class VectCollection:
    """
    
    
        >>> vc = VectCollection()
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((1,3,5))
        >>> vc.AddVect(1,bv1)
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((6,8))
        >>> vc.AddVect(2,bv1)
        >>> len(vc)
        10
        >>> vc.GetNumBits()
        10
        >>> vc[0]
        0
        >>> vc[1]
        1
        >>> vc[9]
        0
        >>> vc[6]
        1
        >>> vc.GetBit(6)
        1
        >>> list(vc.GetOnBits())
        [1, 3, 5, 6, 8]
    
        keys must be unique, so adding a duplicate replaces the
        previous values:
    
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((7,9))
        >>> vc.AddVect(1,bv1)
        >>> len(vc)
        10
        >>> vc[1]
        0
        >>> vc[9]
        1
        >>> vc[6]
        1
    
        we can also query the children:
    
        >>> vc.NumChildren()
        2
        >>> cs = vc.GetChildren()
        >>> id,fp = cs[0]
        >>> id
        1
        >>> list(fp.GetOnBits())
        [7, 9]
        >>> id,fp = cs[1]
        >>> id
        2
        >>> list(fp.GetOnBits())
        [6, 8]
    
        attach/detach operations:
    
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((5,6))
        >>> vc.AddVect(3,bv1)
        >>> vc.NumChildren()
        3
        >>> list(vc.GetOnBits())
        [5, 6, 7, 8, 9]
        >>> vc.DetachVectsNotMatchingBit(6)
        >>> vc.NumChildren()
        2
        >>> list(vc.GetOnBits())
        [5, 6, 8]
    
    
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((7,9))
        >>> vc.AddVect(1,bv1)
        >>> vc.NumChildren()
        3
        >>> list(vc.GetOnBits())
        [5, 6, 7, 8, 9]
        >>> vc.DetachVectsMatchingBit(6)
        >>> vc.NumChildren()
        1
        >>> list(vc.GetOnBits())
        [7, 9]
    
    
        to copy VectCollections, use the copy module:
    
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((5,6))
        >>> vc.AddVect(3,bv1)
        >>> list(vc.GetOnBits())
        [5, 6, 7, 9]
        >>> vc2 = copy.copy(vc)
        >>> vc.DetachVectsNotMatchingBit(6)
        >>> list(vc.GetOnBits())
        [5, 6]
        >>> list(vc2.GetOnBits())
        [5, 6, 7, 9]
    
        The Uniquify() method can be used to remove duplicate vectors:
    
        >>> vc = VectCollection()
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((7,9))
        >>> vc.AddVect(1,bv1)
        >>> vc.AddVect(2,bv1)
        >>> bv1 = DataStructs.ExplicitBitVect(10)
        >>> bv1.SetBitsFromList((2,3,5))
        >>> vc.AddVect(3,bv1)
        >>> vc.NumChildren()
        3
        >>> vc.Uniquify()
        >>> vc.NumChildren()
        2
    
    
        
    """
    def AddVect(self, idx, vect):
        ...
    def DetachVectsMatchingBit(self, bit):
        ...
    def DetachVectsNotMatchingBit(self, bit):
        ...
    def GetBit(self, idx):
        ...
    def GetChildren(self):
        ...
    def GetNumBits(self):
        ...
    def GetOnBits(self):
        ...
    def GetOrVect(self):
        ...
    def NumChildren(self):
        ...
    def Reset(self):
        ...
    def Uniquify(self, verbose = False):
        ...
    def __getitem__(self, idx):
        ...
    def __getstate__(self):
        ...
    def __init__(self):
        ...
    def __len__(self):
        ...
    def __setstate__(self, pkl):
        ...
    @property
    def orVect(self):
        ...
def _runDoctests(verbose = None):
    ...

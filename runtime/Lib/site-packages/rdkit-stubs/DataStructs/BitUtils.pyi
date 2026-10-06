from __future__ import annotations
__all__: list[str] = ['ConstructEnsembleBV']
def ConstructEnsembleBV(bv, bitsToKeep):
    """
    
    
      >>> from rdkit import DataStructs
      >>> bv = DataStructs.ExplicitBitVect(128)
      >>> bv.SetBitsFromList((1,5,47,99,120))
      >>> r = ConstructEnsembleBV(bv,(0,1,2,3,45,46,47,48,49))
      >>> r.GetNumBits()
      9
      >>> r.GetBit(0)
      0
      >>> r.GetBit(1)
      1
      >>> r.GetBit(5)
      0
      >>> r.GetBit(6)  # old bit 47
      1
    
      
    """
def _runDoctests(verbose = None):
    ...

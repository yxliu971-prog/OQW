"""
 contains factory class for producing signatures


"""
from __future__ import annotations
import copy as copy
import numpy as numpy
from rdkit.Chem.Pharm2D import Utils
from rdkit.DataStructs.cDataStructs import IntSparseIntVect
from rdkit.DataStructs.cDataStructs import LongSparseIntVect
from rdkit.DataStructs.cDataStructs import SparseBitVect
__all__: list[str] = ['IntSparseIntVect', 'LongSparseIntVect', 'SigFactory', 'SparseBitVect', 'Utils', 'copy', 'numpy']
class SigFactory:
    """
    
    
          SigFactory's are used by creating one, setting the relevant
          parameters, then calling the GetSignature() method each time a
          signature is required.
    
        
    """
    def GetBins(self):
        ...
    def GetBitDescription(self, bitIdx):
        """
          returns a text description of the bit
        
                **Arguments**
        
                  - bitIdx: an integer bit index
        
                **Returns**
        
                  a string
        
                
        """
    def GetBitDescriptionAsText(self, bitIdx, includeBins = 0, fullPage = 1):
        """
          returns text with a description of the bit
        
                **Arguments**
        
                  - bitIdx: an integer bit index
        
                  - includeBins: (optional) if nonzero, information about the bins will be
                    included as well
        
                  - fullPage: (optional) if nonzero, html headers and footers will
                    be included (so as to make the output a complete page)
        
                **Returns**
        
                  a string with the HTML
        
                
        """
    def GetBitIdx(self, featIndices, dists, sortIndices = True):
        """
         returns the index for a pharmacophore described using a set of
                  feature indices and distances
        
                **Arguments***
        
                  - featIndices: a sequence of feature indices
        
                  - dists: a sequence of distance between the features, only the
                    unique distances should be included, and they should be in the
                    order defined in Utils.
        
                  - sortIndices : sort the indices
        
                **Returns**
        
                  the integer bit index
        
                
        """
    def GetBitInfo(self, idx):
        """
         returns information about the given bit
        
                 **Arguments**
        
                   - idx: the bit index to be considered
        
                 **Returns**
        
                   a 3-tuple:
        
                     1) the number of points in the pharmacophore
        
                     2) the proto-pharmacophore (tuple of pattern indices)
        
                     3) the scaffold (tuple of distance indices)
        
                
        """
    def GetFeatFamilies(self):
        ...
    def GetMolFeats(self, mol):
        ...
    def GetNumBins(self):
        ...
    def GetSigSize(self):
        ...
    def GetSignature(self):
        ...
    def Init(self):
        """
         Initializes internal parameters.  This **must** be called after
                  making any changes to the signature parameters
        
                
        """
    def SetBins(self, bins):
        """
         bins should be a list of 2-tuples 
        """
    def _GetBitSummaryData(self, bitIdx):
        ...
    def __init__(self, featFactory, useCounts = False, minPointCount = 2, maxPointCount = 3, shortestPathsOnly = True, includeBondOrder = False, skipFeats = None, trianglePruneBins = True):
        ...
    def _findBinIdx(self, dists, bins, scaffolds):
        """
         OBSOLETE: this has been rewritten in C++
                Internal use only
                 Returns the index of a bin defined by a set of distances.
        
                **Arguments**
        
                  - dists: a sequence of distances (not binned)
        
                  - bins: a sorted sequence of distance bins (2-tuples)
        
                  - scaffolds: a list of possible scaffolds (bin combinations)
        
                **Returns**
        
                  an integer bin index
        
                **Note**
        
                  the value returned here is not an index in the overall
                  signature.  It is, rather, an offset of a scaffold in the
                  possible combinations of distance bins for a given
                  proto-pharmacophore.
        
                
        """
_verbose: bool = False

"""
 class definitions for similarity screening

See _SimilarityScreener_ for overview of required API

"""
from __future__ import annotations
from rdkit import DataStructs
from rdkit.DataStructs import TopNContainer
__all__: list[str] = ['DataStructs', 'SimilarityScreener', 'ThresholdScreener', 'TopNContainer', 'TopNScreener']
class SimilarityScreener:
    """
      base class
    
         important attributes:
            probe: the probe fingerprint against which we screen.
    
            metric: a function that takes two arguments and returns a similarity
                    measure between them
    
            dataSource: the source pool from which to draw, needs to support
                    a next() method
    
            fingerprinter: a function that takes a molecule and returns a
                   fingerprint of the appropriate format
    
    
          **Notes**
             subclasses must support either an iterator interface
             or __len__ and __getitem__
        
    """
    def GetSingleFingerprint(self, probe):
        """
         returns a fingerprint for a single probe object
        
                 This is potentially useful in initializing our internal
                 probe object.
        
                
        """
    def Reset(self):
        """
         used to reset screeners that behave as iterators 
        """
    def SetProbe(self, probeFingerprint):
        """
         sets our probe fingerprint 
        """
    def __init__(self, probe = None, metric = None, dataSource = None, fingerprinter = None):
        ...
class ThresholdScreener(SimilarityScreener):
    """
     Used to return all compounds that have a similarity
          to the probe beyond a threshold value
    
         **Notes**:
    
           - This is as lazy as possible, so the data source isn't
             queried until the client asks for a hit.
    
           - In addition to being lazy, this class is as thin as possible.
             (Who'd have thought it was possible!)
             Hits are *not* stored locally, so if a client resets
             the iteration and starts over, the same amount of work must
             be done to retrieve the hits.
    
           - The thinness and laziness forces us to support only forward
             iteration (not random access)
    
        
    """
    def Reset(self):
        """
         used to reset our internal state so that iteration
                  starts again from the beginning
                
        """
    def __init__(self, threshold, **kwargs):
        ...
    def __iter__(self):
        """
         returns an iterator for this screener
                
        """
    def __next__(self):
        """
         required part of iterator interface 
        """
    def _nextMatch(self):
        """
         *Internal use only* 
        """
    def next(self):
        """
         required part of iterator interface 
        """
class TopNScreener(SimilarityScreener):
    """
     A screener that only returns the top N hits found
    
          **Notes**
    
            - supports forward iteration and getitem
    
        
    """
    def Reset(self):
        ...
    def __getitem__(self, idx):
        ...
    def __init__(self, num, **kwargs):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def __next__(self):
        ...
    def _initTopN(self):
        ...
    def next(self):
        ...

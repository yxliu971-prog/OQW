from __future__ import annotations
__all__: list[str] = ['ExcludedVolume']
class ExcludedVolume:
    def __init__(self, featInfo, index = -1, exclusionDist = 3.0):
        """
        
            featInfo should be a sequence of ([indices],min,max) tuples
        
            
        """

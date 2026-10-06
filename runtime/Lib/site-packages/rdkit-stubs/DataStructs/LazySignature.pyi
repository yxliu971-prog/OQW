from __future__ import annotations
__all__: list[str] = ['LazySig']
class LazySig:
    def __getitem__(self, which):
        """
        
        
             >>> obj = LazySig(lambda x:x,10)
             >>> obj[1]
             1
             >>> obj[-1]
             9
             >>> try:
             ...   obj[10]
             ... except IndexError:
             ...   1
             ... else:
             ...   0
             1
             >>> try:
             ...   obj[-10]
             ... except IndexError:
             ...   1
             ... else:
             ...   0
             1
        
            
        """
    def __init__(self, computeFunc, sigSize):
        """
        
            computeFunc should take a single argument, the integer bit id
            to compute
        
            
        """
    def __len__(self):
        """
        
        
             >>> obj = LazySig(lambda x:1,10)
             >>> len(obj)
             10
        
            
        """
def _runDoctests(verbose = None):
    ...

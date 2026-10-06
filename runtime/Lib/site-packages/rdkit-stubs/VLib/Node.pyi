from __future__ import annotations
import sys as sys
__all__: list[str] = ['VLibNode', 'sys']
class VLibNode:
    """
     base class for all virtual library nodes,
        defines minimal required interface
    
        
    """
    def AddChild(self, child, notify = 1):
        """
        
        
                >>> p1 = VLibNode()
                >>> p2 = VLibNode()
                >>> c1 = VLibNode()
                >>> p1.AddChild(c1)
                >>> len(c1.GetParents())
                1
                >>> len(p1.GetChildren())
                1
                >>> p2.AddChild(c1,notify=0)
                >>> len(c1.GetParents())
                1
                >>> len(p2.GetChildren())
                1
                >>> c1.AddParent(p2,notify=0)
                >>> len(c1.GetParents())
                2
                >>> len(p2.GetChildren())
                1
        
                
        """
    def AddParent(self, parent, notify = True):
        """
        
                >>> p1 = VLibNode()
                >>> p2 = VLibNode()
                >>> c1 = VLibNode()
                >>> c1.AddParent(p1)
                >>> len(c1.GetParents())
                1
                >>> len(p1.GetChildren())
                1
                >>> c1.AddParent(p2,notify=0)
                >>> len(c1.GetParents())
                2
                >>> len(p2.GetChildren())
                0
                >>> p2.AddChild(c1,notify=0)
                >>> len(c1.GetParents())
                2
                >>> len(p2.GetChildren())
                1
                
        """
    def Destroy(self, notify = True, propagateDown = False, propagateUp = False):
        """
        
                >>> p1 = VLibNode()
                >>> p2 = VLibNode()
                >>> c1 = VLibNode()
                >>> c2 = VLibNode()
                >>> p1.AddChild(c1)
                >>> p2.AddChild(c1)
                >>> p2.AddChild(c2)
                >>> len(c1.GetParents())
                2
                >>> len(c2.GetParents())
                1
                >>> len(p1.GetChildren())
                1
                >>> len(p2.GetChildren())
                2
                >>> c1.Destroy(propagateUp=True)
                >>> len(p2.GetChildren())
                0
                >>> len(c1.GetParents())
                0
                >>> len(c2.GetParents())
                0
        
                
        """
    def GetChildren(self):
        ...
    def GetParents(self):
        ...
    def RemoveChild(self, child, notify = 1):
        """
        
                >>> p1 = VLibNode()
                >>> c1 = VLibNode()
                >>> p1.AddChild(c1)
                >>> len(c1.GetParents())
                1
                >>> len(p1.GetChildren())
                1
                >>> p1.RemoveChild(c1)
                >>> len(c1.GetParents())
                0
                >>> len(p1.GetChildren())
                0
                
        """
    def RemoveParent(self, parent, notify = True):
        """
        
                >>> p1 = VLibNode()
                >>> c1 = VLibNode()
                >>> p1.AddChild(c1)
                >>> len(c1.GetParents())
                1
                >>> len(p1.GetChildren())
                1
                >>> c1.RemoveParent(p1)
                >>> len(c1.GetParents())
                0
                >>> len(p1.GetChildren())
                0
                
        """
    def __init__(self, *args, **kwargs):
        ...
    def __iter__(self):
        """
         part of the iterator interface 
        """
    def __next__(self):
        """
         part of the iterator interface
        
                  raises StopIteration on failure
                
        """
    def next(self):
        """
         part of the iterator interface
        
                  raises StopIteration on failure
                
        """
    def reset(self):
        """
         resets our iteration state
        
                
        """
def _runDoctests(verbose = None):
    ...

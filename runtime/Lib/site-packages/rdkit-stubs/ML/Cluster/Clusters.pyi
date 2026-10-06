"""
 contains the Cluster class for representing hierarchical cluster trees

"""
from __future__ import annotations
__all__: list[str] = ['CMPTOL', 'Cluster', 'cmp']
class Cluster:
    """
    a class for storing clusters/data
    
          **General Remarks**
    
           - It is assumed that the bottom of any cluster hierarchy tree is composed of
             the individual data points which were clustered.
    
           - Clusters objects store the following pieces of data, most are
              accessible via standard Setters/Getters:
    
             - Children: *Not Settable*, the list of children.  You can add children
               with the _AddChild()_ and _AddChildren()_ methods.
    
               **Note** this can be of arbitrary length,
               but the current algorithms I have only produce trees with two children
               per cluster
    
             - Metric: the metric for this cluster (i.e. how far apart its children are)
    
             - Index: the order in which this cluster was generated
    
             - Points: *Not Settable*, the list of original points in this cluster
                  (calculated recursively from the children)
    
             - PointsPositions: *Not Settable*, the list of positions of the original
                points in this cluster (calculated recursively from the children)
    
             - Position: the location of the cluster **Note** for a cluster this
               probably means the location of the average of all the Points which are
               its children.
    
             - Data: a data field.  This is used with the original points to store their
               data value (i.e. the value we're using to classify)
    
             - Name: the name of this cluster
    
        
    """
    def AddChild(self, child):
        """
        Adds a child to our list
        
                  **Arguments**
        
                    - child: a Cluster
        
                
        """
    def AddChildren(self, children):
        """
        Adds a bunch of children to our list
        
                  **Arguments**
        
                    - children: a list of Clusters
        
                
        """
    def Compare(self, other, ignoreExtras = 1):
        """
         not as choosy as self==other
        
                
        """
    def FindSubtree(self, index):
        """
         finds and returns the subtree with a particular index
                
        """
    def GetChildren(self):
        ...
    def GetData(self):
        ...
    def GetIndex(self):
        ...
    def GetMetric(self):
        ...
    def GetName(self):
        ...
    def GetPoints(self):
        ...
    def GetPointsPositions(self):
        ...
    def GetPosition(self):
        ...
    def IsTerminal(self):
        ...
    def Print(self, level = 0, showData = 0, offset = '\t'):
        ...
    def RemoveChild(self, child):
        """
        Removes a child from our list
        
                  **Arguments**
        
                    - child: a Cluster
        
                
        """
    def SetData(self, data):
        ...
    def SetIndex(self, index):
        ...
    def SetMetric(self, metric):
        ...
    def SetName(self, name):
        ...
    def SetPosition(self, pos):
        ...
    def _GenPoints(self):
        """
         Generates the _Points_ and _PointsPositions_ lists
        
                 *intended for internal use*
        
                
        """
    def _UpdateLength(self):
        """
         updates our length
        
                 *intended for internal use*
        
                
        """
    def __cmp__(self, other):
        """
         allows _cluster1 == cluster2_ to work
        
                
        """
    def __init__(self, metric = 0.0, children = None, position = None, index = -1, name = None, data = None):
        """
        Constructor
        
                  **Arguments**
        
                    see the class documentation for the meanings of these arguments
        
                    *my wrists are tired*
        
                
        """
    def __len__(self):
        """
         allows _len(cluster)_ to work
        
                
        """
def cmp(t1, t2):
    ...
CMPTOL: float = 1e-06

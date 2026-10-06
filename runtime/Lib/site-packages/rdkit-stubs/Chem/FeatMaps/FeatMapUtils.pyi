from __future__ import annotations
import copy as copy
from rdkit.Chem.FeatMaps import FeatMaps
import typing
__all__: list[str] = ['CombineFeatMaps', 'DirMergeMode', 'FeatMaps', 'GetFeatFeatDistMatrix', 'MergeFeatPoints', 'MergeMethod', 'MergeMetric', 'copy', 'familiesMatch', 'feq']
class DirMergeMode:
    NoMerge: typing.ClassVar[int] = 0
    Sum: typing.ClassVar[int] = 1
    @classmethod
    def valid(cls, dirMergeMode):
        """
         Check that dirMergeMode is valid 
        """
class MergeMethod:
    Average: typing.ClassVar[int] = 1
    UseLarger: typing.ClassVar[int] = 2
    WeightedAverage: typing.ClassVar[int] = 0
    @classmethod
    def valid(cls, mergeMethod):
        """
         Check that mergeMethod is valid 
        """
class MergeMetric:
    Distance: typing.ClassVar[int] = 1
    NoMerge: typing.ClassVar[int] = 0
    Overlap: typing.ClassVar[int] = 2
    @classmethod
    def valid(cls, mergeMetric):
        """
         Check that mergeMetric is valid 
        """
def CombineFeatMaps(fm1, fm2, mergeMetric = 0, mergeTol = 1.5, dirMergeMode = 0):
    """
    
         the parameters will be taken from fm1
      
    """
def GetFeatFeatDistMatrix(fm, mergeMetric, mergeTol, dirMergeMode, compatFunc):
    """
    
    
        NOTE that mergeTol is a max value for merging when using distance-based
        merging and a min value when using score-based merging.
    
      
    """
def MergeFeatPoints(fm, mergeMetric = 0, mergeTol = 1.5, dirMergeMode = 0, mergeMethod = 0, compatFunc = familiesMatch):
    """
    
    
        NOTE that mergeTol is a max value for merging when using distance-based
        merging and a min value when using score-based merging.
    
        returns whether or not any points were actually merged
    
      
    """
def __copyAll(res, fm1, fm2):
    """
     no user-serviceable parts inside 
    """
def familiesMatch(f1, f2):
    ...
def feq(v1, v2, tol = 0.0001):
    ...

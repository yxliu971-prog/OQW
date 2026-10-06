from __future__ import annotations
import math as math
from rdkit.Chem.FeatMaps.FeatMapPoint import FeatMapPoint
import typing
__all__: list[str] = ['FeatDirScoreMode', 'FeatMap', 'FeatMapParams', 'FeatMapPoint', 'FeatMapScoreMode', 'math']
class FeatDirScoreMode:
    DotFullRange: typing.ClassVar[int] = 1
    DotPosRange: typing.ClassVar[int] = 2
    Ignore: typing.ClassVar[int] = 0
class FeatMap:
    dirScoreMode: typing.ClassVar[int] = 0
    params: typing.ClassVar[dict] = {}
    scoreMode: typing.ClassVar[int] = 0
    def AddFeatPoint(self, featPt):
        ...
    def AddFeature(self, feat, weight = None):
        ...
    def DropFeature(self, i):
        ...
    def GetFeatFeatScore(self, feat1, feat2, typeMatch = True):
        """
         feat1 is one of our feats
                feat2 is any Feature
        
            
        """
    def GetFeature(self, i):
        ...
    def GetFeatures(self):
        ...
    def GetNumFeatures(self):
        ...
    def ScoreFeats(self, featsToScore, mapScoreVect = None, featsScoreVect = None, featsToFeatMapIdx = None):
        ...
    def __init__(self, params = None, feats = None, weights = None):
        ...
    def __str__(self):
        ...
    def _initializeFeats(self, feats, weights):
        ...
    def _loopOverMatchingFeats(self, oFeat):
        ...
class FeatMapParams:
    """
     one of these should be instantiated for each
      feature type in the feature map
      
    """
    class FeatProfile:
        """
         scoring profile of the feature 
        """
        Box: typing.ClassVar[int] = 2
        Gaussian: typing.ClassVar[int] = 0
        Triangle: typing.ClassVar[int] = 1
    featProfile: typing.ClassVar[int] = 0
    radius: typing.ClassVar[float] = 2.5
    width: typing.ClassVar[float] = 1.0
class FeatMapScoreMode:
    All: typing.ClassVar[int] = 0
    Best: typing.ClassVar[int] = 2
    Closest: typing.ClassVar[int] = 1

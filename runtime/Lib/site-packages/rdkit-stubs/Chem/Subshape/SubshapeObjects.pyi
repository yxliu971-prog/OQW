from __future__ import annotations
import typing
__all__: list[str] = ['DisplaySubshape', 'DisplaySubshapeSkeleton', 'ShapeWithSkeleton', 'SkeletonPoint', 'SubshapeShape']
class ShapeWithSkeleton:
    grid = None
    skelPts = None
    def __init__(self, *args, **kwargs):
        ...
    def _initMemberData(self):
        ...
class SkeletonPoint:
    featmapFeatures = None
    fracVol: typing.ClassVar[float] = 0.0
    location = None
    molFeatures = None
    shapeDirs = None
    shapeMoments = None
    def __init__(self, *args, **kwargs):
        ...
    def _initMemberData(self):
        ...
class SubshapeShape:
    featMap = None
    keyFeat = None
    shapes = None
    def __init__(self, *args, **kwargs):
        ...
    def _initMemberData(self):
        ...
def DisplaySubshape(viewer, shape, name, showSkelPts = True, color = (1, 0, 1)):
    ...
def DisplaySubshapeSkeleton(viewer, shape, name, color = (1, 0, 1), colorByOrder = False):
    ...
def _displaySubshapeSkelPt(viewer, skelPt, cgoNm, color):
    ...

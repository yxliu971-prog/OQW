from __future__ import annotations
import copy as copy
import pickle as pickle
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Subshape import BuilderUtils
from rdkit.Chem.Subshape import SubshapeObjects
from rdkit import Geometry
import time as time
import typing
__all__: list[str] = ['AllChem', 'BuilderUtils', 'Chem', 'Geometry', 'SubshapeBuilder', 'SubshapeCombineOperations', 'SubshapeObjects', 'copy', 'pickle', 'time']
class SubshapeBuilder:
    featFactory = None
    fraction: typing.ClassVar[float] = 0.25
    gridDims: typing.ClassVar[tuple] = (20, 15, 10)
    gridSpacing: typing.ClassVar[float] = 0.5
    nbrCount: typing.ClassVar[int] = 7
    stepSize: typing.ClassVar[float] = 1.0
    terminalPtRadScale: typing.ClassVar[float] = 0.75
    winRad: typing.ClassVar[float] = 3.0
    def CombineSubshapes(self, subshape1, subshape2, operation = 0):
        ...
    def GenerateSubshapeShape(self, cmpd, confId = -1, addSkeleton = True, **kwargs):
        ...
    def GenerateSubshapeSkeleton(self, shape, conf = None, terminalPtsOnly = False, skelFromConf = True):
        ...
    def SampleSubshape(self, subshape1, newSpacing):
        ...
    def __call__(self, cmpd, **kwargs):
        ...
class SubshapeCombineOperations:
    INTERSECT: typing.ClassVar[int] = 2
    SUM: typing.ClassVar[int] = 1
    UNION: typing.ClassVar[int] = 0

from __future__ import annotations
import numpy as numpy
from rdkit import Chem
from rdkit.Chem.Subshape import SubshapeObjects
from rdkit import Geometry
from rdkit.Numerics import rdAlignment as Alignment
import rdkit.RDLogger
from rdkit import RDLogger
import typing
__all__: list[str] = ['Alignment', 'Chem', 'ClusterAlignments', 'Geometry', 'GetShapeShapeDistance', 'RDLogger', 'SubshapeAligner', 'SubshapeAlignment', 'SubshapeDistanceMetric', 'SubshapeObjects', 'TransformMol', 'logger', 'numpy']
class SubshapeAligner:
    coarseGridToleranceMult: typing.ClassVar[float] = 1.0
    dirThresh: typing.ClassVar[float] = 2.6
    distMetric: typing.ClassVar[int] = 1
    edgeTol: typing.ClassVar[float] = 6.0
    medGridToleranceMult: typing.ClassVar[float] = 1.0
    numFeatThresh: typing.ClassVar[int] = 3
    shapeDistTol: typing.ClassVar[float] = 0.2
    triangleRMSTol: typing.ClassVar[float] = 1.0
    def GetSubshapeAlignments(self, targetMol, target, queryMol, query, builder, tgtConf = -1, queryConf = -1, pruneStats = None):
        ...
    def GetTriangleMatches(self, target, query):
        """
         this is a generator function returning the possible triangle
                matches between the two shapes
            
        """
    def PruneMatchesUsingDirection(self, target, query, alignments, pruneStats = None):
        ...
    def PruneMatchesUsingFeatures(self, target, query, alignments, pruneStats = None):
        ...
    def PruneMatchesUsingShape(self, targetMol, target, queryMol, query, builder, alignments, tgtConf = -1, queryConf = -1, pruneStats = None):
        ...
    def __call__(self, targetMol, target, queryMol, query, builder, tgtConf = -1, queryConf = -1, pruneStats = None):
        ...
    def _addCoarseAndMediumGrids(self, mol, tgt, confId, builder):
        ...
    def _checkMatchDirections(self, targetPts, queryPts, alignment):
        ...
    def _checkMatchFeatures(self, targetPts, queryPts, alignment):
        ...
    def _checkMatchShape(self, targetMol, target, queryMol, query, alignment, builder, targetConf, queryConf, pruneStats = None, tConfId = 1001):
        ...
class SubshapeAlignment:
    alignedConfId: typing.ClassVar[int] = -1
    dirMatch: typing.ClassVar[float] = 0.0
    queryTri = None
    shapeDist: typing.ClassVar[float] = 0.0
    targetTri = None
    transform = None
    triangleSSD = None
class SubshapeDistanceMetric:
    PROTRUDE: typing.ClassVar[int] = 1
    TANIMOTO: typing.ClassVar[int] = 0
def ClusterAlignments(mol, alignments, builder, neighborTol = 0.1, distMetric = 1, tempConfId = 1001):
    """
     clusters a set of alignments and returns the cluster centroid 
    """
def GetShapeShapeDistance(s1, s2, distMetric):
    """
     returns the distance between two shapes according to the provided metric 
    """
def TransformMol(mol, tform, confId = -1, newConfId = 100):
    """
      Applies the transformation to a molecule and sets it up with a single conformer 
    """
def _getAllTriangles(pts, orderedTraversal = False):
    ...
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>

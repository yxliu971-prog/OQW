from __future__ import annotations
import math as math
import numpy as numpy
from rdkit.Chem.Subshape import SubshapeObjects
from rdkit import Geometry
__all__: list[str] = ['AppendSkeletonPoints', 'AssignMolFeatsToPoints', 'CalculateDirectionsAtPoint', 'ClusterTerminalPts', 'ComputeGridIndices', 'ComputeShapeGridCentroid', 'ExpandTerminalPts', 'FindFarthestGridPoint', 'FindGridPointBetweenPoints', 'FindTerminalPtsFromConformer', 'FindTerminalPtsFromShape', 'Geometry', 'GetMoreTerminalPoints', 'SubshapeObjects', 'math', 'numpy']
def AppendSkeletonPoints(shapeGrid, termPts, winRad, stepDist, maxGridVal = 3, maxDistC = 15.0, distTol = 1.5, symFactor = 1.5, verbose = False):
    ...
def AssignMolFeatsToPoints(pts, mol, featFactory, winRad):
    ...
def CalculateDirectionsAtPoint(pt, shapeGrid, winRad):
    ...
def ClusterTerminalPts(pts, winRad, scale):
    ...
def ComputeGridIndices(shapeGrid, winRad):
    ...
def ComputeShapeGridCentroid(pt, shapeGrid, winRad):
    ...
def ExpandTerminalPts(shape, pts, winRad, maxGridVal = 3.0, targetNumPts = 5):
    """
     find additional terminal points until a target number is reached
      
    """
def FindFarthestGridPoint(shape, loc, winRad, maxGridVal):
    """
     find the grid point with max occupancy that is furthest from a
        given location
      
    """
def FindGridPointBetweenPoints(pt1, pt2, shapeGrid, winRad):
    ...
def FindTerminalPtsFromConformer(conf, winRad, nbrCount):
    ...
def FindTerminalPtsFromShape(shape, winRad, fraction, maxGridVal = 3):
    ...
def GetMoreTerminalPoints(shape, pts, winRad, maxGridVal, targetNumber = 5):
    """
     adds a set of new terminal points using a max-min algorithm
      
    """

"""
 A module for Geometry stuff	
 
"""
from __future__ import annotations
from rdkit import DataStructs
from rdkit.Geometry.rdGeometry import Point2D
from rdkit.Geometry.rdGeometry import Point3D
from rdkit.Geometry.rdGeometry import PointND
from rdkit.Geometry.rdGeometry import UniformGrid3D_
from rdkit.Geometry.rdGeometry import UniformRealValueGrid3D
from .rdGeometry import *
__all__: list[str] = ['DataStructs', 'Point2D', 'Point3D', 'PointND', 'UniformGrid3D_', 'UniformRealValueGrid3D', 'rdGeometry']

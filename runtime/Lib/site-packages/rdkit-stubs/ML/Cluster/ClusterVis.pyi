"""
Cluster tree visualization using Sping

"""
from __future__ import annotations
import numpy as numpy
from rdkit.ML.Cluster import ClusterUtils
import rdkit.sping.colors
from rdkit.sping import pid as piddle
from rdkit.sping import pid
import typing
__all__: list[str] = ['ClusterRenderer', 'ClusterToImg', 'ClusterToPDF', 'ClusterToSVG', 'ClusterUtils', 'DrawClusterTree', 'VisOpts', 'numpy', 'pid', 'piddle']
class ClusterRenderer:
    def DrawTree(self, cluster, minHeight = 2.0):
        ...
    def _AssignClusterLocations(self, cluster):
        ...
    def _AssignPointLocations(self, cluster, terminalOffset = 4):
        ...
    def _DrawToLimit(self, cluster):
        """
        
              we assume that _drawPos settings have been done already
            
        """
    def __init__(self, canvas, size, ptColors = list(), lineWidth = None, showIndices = 0, showNodes = 1, stopAtCentroids = 0, logScale = 0, tooClose = -1):
        ...
class VisOpts:
    """
     stores visualization options for cluster viewing
    
        **Instance variables**
    
          - x/yOffset: amount by which the drawing is offset from the edges of the canvas
    
          - lineColor: default color for drawing the cluster tree
    
          - lineWidth: the width of the lines used to draw the tree
    
      
    """
    hideColor: typing.ClassVar[rdkit.sping.colors.Color]  # value = Color(0.80,0.80,0.80)
    hideWidth: typing.ClassVar[float] = 1.1
    highlightColor: typing.ClassVar[rdkit.sping.colors.Color]  # value = Color(1.00,1.00,0.40)
    highlightRad: typing.ClassVar[int] = 10
    lineColor: typing.ClassVar[rdkit.sping.colors.Color]  # value = Color(0.00,0.00,0.00)
    lineWidth: typing.ClassVar[int] = 2
    nodeColor: typing.ClassVar[rdkit.sping.colors.Color]  # value = Color(1.00,0.40,0.40)
    nodeRad: typing.ClassVar[int] = 15
    terminalColors: typing.ClassVar[list]  # value = [Color(1.00,0.00,0.00), Color(0.00,0.00,1.00), Color(1.00,1.00,0.00), Color(0.00,0.50,0.50), Color(0.00,0.80,0.00), Color(0.50,0.50,0.50), Color(0.80,0.30,0.30), Color(0.30,0.30,0.80), Color(0.80,0.80,0.30), Color(0.30,0.80,0.80)]
    xOffset: typing.ClassVar[int] = 20
    yOffset: typing.ClassVar[int] = 20
def ClusterToImg(cluster, fileName, size = (300, 300), ptColors = list(), lineWidth = None, showIndices = 0, stopAtCentroids = 0, logScale = 0):
    """
     handles the work of drawing a cluster tree to an image file
    
        **Arguments**
    
          - cluster: the cluster tree to be drawn
    
          - fileName: the name of the file to be created
    
          - size: the size of output canvas
    
          - ptColors: if this is specified, the _colors_ will be used to color
            the terminal nodes of the cluster tree.  (color == _pid.Color_)
    
          - lineWidth: if specified, it will be used for the widths of the lines
            used to draw the tree
    
       **Notes**
    
         - The extension on  _fileName_ determines the type of image file created.
           All formats supported by PIL can be used.
    
         - if _ptColors_ is the wrong length for the number of possible terminal
           node types, this will throw an IndexError
    
         - terminal node types are determined using their _GetData()_ methods
    
      
    """
def ClusterToPDF(cluster, fileName, size = (300, 300), ptColors = list(), lineWidth = None, showIndices = 0, stopAtCentroids = 0, logScale = 0):
    """
     handles the work of drawing a cluster tree to an PDF file
    
        **Arguments**
    
          - cluster: the cluster tree to be drawn
    
          - fileName: the name of the file to be created
    
          - size: the size of output canvas
    
          - ptColors: if this is specified, the _colors_ will be used to color
            the terminal nodes of the cluster tree.  (color == _pid.Color_)
    
          - lineWidth: if specified, it will be used for the widths of the lines
            used to draw the tree
    
       **Notes**
    
         - if _ptColors_ is the wrong length for the number of possible terminal
           node types, this will throw an IndexError
    
         - terminal node types are determined using their _GetData()_ methods
    
      
    """
def ClusterToSVG(cluster, fileName, size = (300, 300), ptColors = list(), lineWidth = None, showIndices = 0, stopAtCentroids = 0, logScale = 0):
    """
     handles the work of drawing a cluster tree to an SVG file
    
        **Arguments**
    
          - cluster: the cluster tree to be drawn
    
          - fileName: the name of the file to be created
    
          - size: the size of output canvas
    
          - ptColors: if this is specified, the _colors_ will be used to color
            the terminal nodes of the cluster tree.  (color == _pid.Color_)
    
          - lineWidth: if specified, it will be used for the widths of the lines
            used to draw the tree
    
       **Notes**
    
         - if _ptColors_ is the wrong length for the number of possible terminal
           node types, this will throw an IndexError
    
         - terminal node types are determined using their _GetData()_ methods
    
      
    """
def DrawClusterTree(cluster, canvas, size, ptColors = list(), lineWidth = None, showIndices = 0, showNodes = 1, stopAtCentroids = 0, logScale = 0, tooClose = -1):
    """
     handles the work of drawing a cluster tree on a Sping canvas
    
        **Arguments**
    
          - cluster: the cluster tree to be drawn
    
          - canvas:  the Sping canvas on which to draw
    
          - size: the size of _canvas_
    
          - ptColors: if this is specified, the _colors_ will be used to color
            the terminal nodes of the cluster tree.  (color == _pid.Color_)
    
          - lineWidth: if specified, it will be used for the widths of the lines
            used to draw the tree
    
       **Notes**
    
         - _Canvas_ is neither _save_d nor _flush_ed at the end of this
    
         - if _ptColors_ is the wrong length for the number of possible terminal
           node types, this will throw an IndexError
    
         - terminal node types are determined using their _GetData()_ methods
    
      
    """
def _DrawClusterTree(cluster, canvas, size, ptColors = list(), lineWidth = None, showIndices = 0, showNodes = 1, stopAtCentroids = 0, logScale = 0, tooClose = -1):
    """
     handles the work of drawing a cluster tree on a Sping canvas
    
        **Arguments**
    
          - cluster: the cluster tree to be drawn
    
          - canvas:  the Sping canvas on which to draw
    
          - size: the size of _canvas_
    
          - ptColors: if this is specified, the _colors_ will be used to color
            the terminal nodes of the cluster tree.  (color == _pid.Color_)
    
          - lineWidth: if specified, it will be used for the widths of the lines
            used to draw the tree
    
       **Notes**
    
         - _Canvas_ is neither _save_d nor _flush_ed at the end of this
    
         - if _ptColors_ is the wrong length for the number of possible terminal
           node types, this will throw an IndexError
    
         - terminal node types are determined using their _GetData()_ methods
    
      
    """
def _scaleMetric(val, power = 2, min = 0.0001):
    ...

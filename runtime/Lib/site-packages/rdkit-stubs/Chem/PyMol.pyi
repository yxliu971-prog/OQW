"""
 uses pymol to interact with molecules

"""
from __future__ import annotations
import os as os
from rdkit import Chem
import sys as sys
import tempfile as tempfile
from xmlrpc.client import ServerProxy as Server
__all__: list[str] = ['Chem', 'MolViewer', 'Server', 'os', 'sys', 'tempfile']
class MolViewer:
    def AddPharmacophore(self, locs, colors, label, sphereRad = 0.5):
        """
         adds a set of spheres 
        """
    def DeleteAll(self):
        """
         blows out everything in the viewer 
        """
    def DeleteAllExcept(self, excludes):
        """
         deletes everything except the items in the provided list of arguments 
        """
    def DisplayCollisions(self, objName, molName, proteinName, distCutoff = 3.0, color = 'red', molSelText = '(%(molName)s)', proteinSelText = '(%(proteinName)s and not het)'):
        """
         toggles display of collisions between the protein and a specified molecule 
        """
    def DisplayHBonds(self, objName, molName, proteinName, molSelText = '(%(molName)s)', proteinSelText = '(%(proteinName)s and not het)'):
        """
         toggles display of h bonds between the protein and a specified molecule 
        """
    def DisplayObject(self, objName):
        ...
    def GetAtomCoords(self, sels):
        """
         returns the coordinates of the selected atoms 
        """
    def GetPNG(self, h = None, w = None, preDelay = 0):
        ...
    def GetSelectedAtoms(self, whichSelection = None):
        """
         returns the selected atoms 
        """
    def HideAll(self):
        ...
    def HideObject(self, objName):
        ...
    def HighlightAtoms(self, indices, where, extraHighlight = False):
        """
         highlights a set of atoms 
        """
    def InitializePyMol(self):
        """
         does some initializations to set up PyMol according to our
            tastes
        
            
        """
    def LoadFile(self, filename, name, showOnly = False):
        """
         calls pymol's "load" command on the given filename; the loaded object
            is assigned the name "name"
            
        """
    def Redraw(self):
        ...
    def SaveFile(self, filename):
        ...
    def SelectAtoms(self, itemId, atomIndices, selName = 'selection'):
        """
         selects a set of atoms 
        """
    def SelectProteinNeighborhood(self, aroundObj, inObj, distance = 5.0, name = 'neighborhood', showSurface = False):
        """
         selects the area of a protein around a specified object/selection name;
            optionally adds a surface to that 
        """
    def SetDisplayStyle(self, obj, style = ''):
        """
         change the display style of the specified object 
        """
    def SetDisplayUpdate(self, val):
        ...
    def ShowMol(self, mol, name = 'molecule', showOnly = True, highlightFeatures = list(), molB = '', confId = -1, zoom = True, forcePDB = False, showSticks = False):
        """
         special case for displaying a molecule or mol block 
        """
    def Zoom(self, objName):
        ...
    def __init__(self, host = None, port = 9123, force = 0, **kwargs):
        ...
_server = None

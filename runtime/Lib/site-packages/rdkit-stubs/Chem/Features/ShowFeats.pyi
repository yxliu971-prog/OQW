from __future__ import annotations
import math as math
import optparse
from optparse import OptionParser
import os as os
from rdkit.Chem.Features import FeatDirUtilsRD as FeatDirUtils
from rdkit import Geometry
from rdkit import RDConfig
import rdkit.RDLogger
from rdkit import RDLogger as logging
import sys as sys
__all__: list[str] = ['ALPHA', 'BEGIN', 'COLOR', 'CYLINDER', 'END', 'FeatDirUtils', 'Geometry', 'NORMAL', 'OptionParser', 'RDConfig', 'SPHERE', 'ShowArrow', 'ShowMolFeats', 'TRIANGLE_FAN', 'VERTEX', 'logger', 'logging', 'math', 'os', 'parser', 'sys']
def ShowArrow(viewer, tail, head, radius, color, label, transparency = 0, includeArrowhead = True):
    ...
def ShowMolFeats(mol, factory, viewer, radius = 0.5, confId = -1, showOnly = True, name = '', transparency = 0.0, colors = None, excludeTypes = list(), useFeatDirs = True, featLabel = None, dirLabel = None, includeArrowheads = True, writeFeats = False, showMol = True, featMapFile = False):
    ...
def _buildCanonArrowhead(headFrac, nSteps, aspect):
    ...
def _cgoArrowhead(viewer, tail, head, radius, color, label, headFrac = 0.3, nSteps = 10, aspect = 0.5):
    ...
def _getVectNormal(v, tol = 0.0001):
    ...
ALPHA: int = 25
BEGIN: int = 2
COLOR: int = 6
CYLINDER: int = 9
END: int = 3
NORMAL: int = 5
SPHERE: int = 7
TRIANGLE_FAN: int = 6
VERTEX: int = 4
_canonArrowhead = None
_featColors: dict = {'Donor': (0, 1, 1), 'Acceptor': (1, 0, 1), 'NegIonizable': (1, 0, 0), 'PosIonizable': (0, 0, 1), 'ZnBinder': (1, 0.5, 0.5), 'Aromatic': (1, 0.8, 0.2), 'LumpedHydrophobe': (0.5, 0.25, 0), 'Hydrophobe': (0.5, 0.25, 0)}
_globalArrowCGO: list = list()
_globalSphereCGO: list = list()
_usage: str = '\n   ShowFeats [optional args] <filenames>\n\n  if "-" is provided as a filename, data will be read from stdin (the console)\n'
_version: str = '0.3.2'
_welcomeMessage: str = 'This is ShowFeats version 0.3.2'
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>
parser: optparse.OptionParser  # value = <optparse.OptionParser object>

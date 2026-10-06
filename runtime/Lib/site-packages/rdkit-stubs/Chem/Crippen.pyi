"""
 Atom-based calculation of LogP and MR using Crippen's approach


    Reference:
      S. A. Wildman and G. M. Crippen *JCICS* _39_ 868-873 (1999)


"""
from __future__ import annotations
import numpy as numpy
import os as os
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
from rdkit import RDConfig
__all__: list[str] = ['Chem', 'RDConfig', 'defaultPatternFileName', 'numpy', 'os', 'rdMolDescriptors']
def _Init():
    ...
def _ReadPatts(fileName):
    """
     *Internal Use Only*
    
        parses the pattern list from the data file
    
      
    """
def _pyGetAtomContribs(mol, patts = None, order = None, verbose = 0, force = 0):
    """
     *Internal Use Only*
    
        calculates atomic contributions to the LogP and MR values
    
        if the argument *force* is not set, we'll use the molecules stored
        _crippenContribs value when possible instead of re-calculating.
    
      **Note:** Changes here affect the version numbers of MolLogP and MolMR
        as well as the VSA descriptors in Chem.MolSurf
    
      
    """
def _pyMolLogP(inMol, patts = None, order = None, verbose = 0, addHs = 1):
    """
     DEPRECATED
      
    """
def _pyMolMR(inMol, patts = None, order = None, verbose = 0, addHs = 1):
    """
     DEPRECATED
      
    """
_patternOrder: list = list()
_smartsPatterns: dict = {}
defaultPatternFileName: str = 'C:/rdkit/build/temp.win-amd64-cpython-312/Release/rdkit_install\\share/RDKit\\Data\\Crippen.txt'

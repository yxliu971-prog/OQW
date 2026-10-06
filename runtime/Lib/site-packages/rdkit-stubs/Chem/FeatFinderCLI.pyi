from __future__ import annotations
import argparse as argparse
import os as os
from rdkit import Chem
from rdkit.Chem import ChemicalFeatures
import rdkit.RDLogger
from rdkit import RDLogger
import re as re
__all__: list[str] = ['Chem', 'ChemicalFeatures', 'GetAtomFeatInfo', 'RDLogger', 'argparse', 'existingFile', 'initParser', 'logger', 'main', 'os', 'processArgs', 're', 'splitExpr']
def GetAtomFeatInfo(factory, mol):
    ...
def existingFile(filename):
    """
     'type' for argparse - check that filename exists 
    """
def initParser():
    """
     Initialize the parser 
    """
def main():
    """
     Main application 
    """
def processArgs(args, parser):
    ...
_splashMessage: str = '\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n  FeatFinderCLI\n  Part of the RDKit (http://www.rdkit.org)\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n'
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>
splitExpr: re.Pattern  # value = re.compile('[ \\t,]')

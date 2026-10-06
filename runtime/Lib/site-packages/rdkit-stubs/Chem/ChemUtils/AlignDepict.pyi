from __future__ import annotations
import argparse as argparse
from rdkit import Chem
from rdkit.Chem import rdDepictor
from rdkit import Geometry
import sys as sys
__all__: list[str] = ['AlignDepict', 'Chem', 'Geometry', 'argparse', 'initParser', 'main', 'processArgs', 'rdDepictor', 'sys']
def AlignDepict(mol, core, corePattern = None, acceptFailure = False):
    """
    
      Arguments:
        - mol:          the molecule to be aligned, this will come back
                        with a single conformer.
        - core:         a molecule with the core atoms to align to;
                        this should have a depiction.
        - corePattern:  (optional) an optional molecule to be used to
                        generate the atom mapping between the molecule
                        and the core.
      
    """
def initParser():
    """
     Initialize the parser 
    """
def main():
    """
     Main application 
    """
def processArgs(args):
    ...

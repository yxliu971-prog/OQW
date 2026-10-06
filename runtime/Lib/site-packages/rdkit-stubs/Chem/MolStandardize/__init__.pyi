"""

Molecule Validation and Standardization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a C++ reimplementation and exapansion of Matt Swain's MolVS tool

"""
from __future__ import annotations
from rdkit import Chem
from .rdMolStandardize import *
__all__: list[str] = ['Chem', 'ReorderTautomers', 'rdMolStandardize']
def ReorderTautomers(molecule):
    """
    Returns the list of the molecule's tautomers
        so that the canonical one as determined by the canonical
        scoring system in TautomerCanonicalizer appears first.
    
        :param molecule: An RDKit Molecule object.
        :return: A list of Molecule objects.
        
    """

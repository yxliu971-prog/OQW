"""
  Functionality for SATIS typing atoms

"""
from __future__ import annotations
import itertools as itertools
from rdkit import Chem
import rdkit.Chem.rdchem
__all__: list[str] = ['Chem', 'SATISTypes', 'aldehydePatt', 'amidePatt', 'carboxylPatt', 'carboxylatePatt', 'esterPatt', 'itertools', 'ketonePatt', 'specialCases']
def SATISTypes(mol, neighborsToInclude = 4):
    """
     returns SATIS codes for all atoms in a molecule
    
       The SATIS definition used is from:
       J. Chem. Inf. Comput. Sci. _39_ 751-757 (1999)
    
       each SATIS code is a string consisting of _neighborsToInclude_ + 1
       2 digit numbers
    
       **Arguments**
    
         - mol: a molecule
    
         - neighborsToInclude (optional): the number of neighbors to include
           in the SATIS codes
    
       **Returns**
    
         a list of strings nAtoms long
    
      
    """
aldehydePatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
amidePatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
carboxylPatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
carboxylatePatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
esterPatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
ketonePatt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
specialCases: tuple  # value = ((<rdkit.Chem.rdchem.Mol object>, 97), (<rdkit.Chem.rdchem.Mol object>, 96), (<rdkit.Chem.rdchem.Mol object>, 98), (<rdkit.Chem.rdchem.Mol object>, 95), (<rdkit.Chem.rdchem.Mol object>, 94), (<rdkit.Chem.rdchem.Mol object>, 93))

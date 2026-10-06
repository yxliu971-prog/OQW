"""
 Basic EState definitions

"""
from __future__ import annotations
import numpy as numpy
from rdkit import Chem
__all__: list[str] = ['Chem', 'EStateIndices', 'GetPrincipleQuantumNumber', 'MaxAbsEStateIndex', 'MaxEStateIndex', 'MinAbsEStateIndex', 'MinEStateIndex', 'numpy']
def EStateIndices(mol, force = True):
    """
     returns a tuple of EState indices for the molecule
    
        Reference: Hall, Mohney and Kier. JCICS _31_ 76-81 (1991)
    
      
    """
def GetPrincipleQuantumNumber(atNum):
    """
     Get principal quantum number for atom number 
    """
def MaxAbsEStateIndex(mol, force = 1):
    ...
def MaxEStateIndex(mol, force = 1):
    ...
def MinAbsEStateIndex(mol, force = 1):
    ...
def MinEStateIndex(mol, force = 1):
    ...
def _exampleCode():
    """
     Example code for calculating E-state indices 
    """

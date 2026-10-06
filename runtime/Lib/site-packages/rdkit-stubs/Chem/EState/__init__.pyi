"""
 A module for Kier and Hall's EState Descriptors

Unless otherwise noted, all definitions here can be found in:

  L.B. Kier and L.H. Hall _Molecular Structure Description:
  The Electrotopological State"_  Academic Press (1999)

"""
from __future__ import annotations
import numpy as numpy
from rdkit import Chem
from rdkit.Chem.EState.AtomTypes import BuildPatts
from rdkit.Chem.EState.AtomTypes import TypeAtoms
from rdkit.Chem.EState.EState import EStateIndices
from rdkit.Chem.EState.EState import GetPrincipleQuantumNumber
from rdkit.Chem.EState.EState import MaxAbsEStateIndex
from rdkit.Chem.EState.EState import MaxEStateIndex
from rdkit.Chem.EState.EState import MinAbsEStateIndex
from rdkit.Chem.EState.EState import MinEStateIndex
import sys as sys
from .AtomTypes import *
from .EState import *
__all__: list[str] = ['AtomTypes', 'BuildPatts', 'Chem', 'EState', 'EStateIndices', 'GetPrincipleQuantumNumber', 'MaxAbsEStateIndex', 'MaxEStateIndex', 'MinAbsEStateIndex', 'MinEStateIndex', 'TypeAtoms', 'esPatterns', 'numpy', 'sys']
esPatterns = None

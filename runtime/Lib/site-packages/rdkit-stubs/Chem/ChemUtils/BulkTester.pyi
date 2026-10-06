from __future__ import annotations
from rdkit import Chem
from rdkit.Chem import Randomize
import sys as sys
__all__: list[str] = ['Chem', 'Randomize', 'TestMolecule', 'TestSupplier', 'sys']
def TestMolecule(mol):
    ...
def TestSupplier(suppl, stopAfter = -1, reportInterval = 100, reportTo = ..., nameProp = '_Name'):
    ...

"""
 Contains an implementation of Physicochemical property fingerprints, as
described in:
Kearsley, S. K. et al.
"Chemical Similarity Using Physiochemical Property Descriptors."
J. Chem.Inf. Model. 36, 118-127 (1996)

The fingerprints can be accessed through the following functions:
- GetBPFingerprint
- GetBTFingerprint

"""
from __future__ import annotations
import os as os
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import rdMolDescriptors
from rdkit import RDConfig
import re as re
__all__: list[str] = ['AssignPattyTypes', 'Chem', 'GetBPFingerprint', 'GetBTFingerprint', 'RDConfig', 'fpLen', 'numFpBits', 'numPathBits', 'os', 'rdFingerprintGenerator', 'rdMolDescriptors', 're', 'typMap']
def AssignPattyTypes(mol, defns = None):
    """
    
    
        >>> from rdkit import Chem
        >>> AssignPattyTypes(Chem.MolFromSmiles('OCC(=O)O'))
        ['POL', 'HYD', 'OTH', 'ANI', 'ANI']
    
        
    """
def GetBPFingerprint(mol, fpfn = _atomPairFingerprintFunc):
    """
    
        >>> from rdkit import Chem
        >>> fp = GetBPFingerprint(Chem.MolFromSmiles('OCC(=O)O'))
        >>> fp.GetTotalVal()
        10
        >>> nze = fp.GetNonzeroElements()
        >>> sorted([(k, v) for k, v in nze.items()])
        [(32834, 1), (49219, 2), (98370, 2), (98401, 1), (114753, 2), (114786, 1), (114881, 1)]
    
        
    """
def GetBTFingerprint(mol, fpfn = _topologicalTorsionsFingerprintFunc):
    """
    
        >>> from rdkit import Chem
        >>> mol = Chem.MolFromSmiles('OCC(N)O')
        >>> AssignPattyTypes(mol)
        ['POL', 'HYD', 'HYD', 'CAT', 'POL']
        >>> fp = GetBTFingerprint(mol)
        >>> fp.GetTotalVal()
        2
        >>> nze = fp.GetNonzeroElements()
        >>> sorted([(k, v) for k, v in nze.items()])
        [(538446850..., 1), (538446852..., 1)]
    
        
    """
def _atomPairFingerprintFunc(mol, atomInvariants):
    ...
def _readPattyDefs(fname = 'C:/rdkit/build/temp.win-amd64-cpython-312/Release/rdkit_install\\share/RDKit\\Data\\SmartsLib\\patty_rules.txt'):
    ...
def _runDoctests(verbose = None):
    ...
def _topologicalTorsionsFingerprintFunc(mol, atomInvariants):
    ...
_apFPG = None
_maxPathLen: int = 31
_pattyDefs = None
_ttFPG = None
fpLen: int = 8388608
numFpBits: int = 23
numPathBits: int = 5
typMap: dict = {'CAT': 1, 'ANI': 2, 'POL': 3, 'DON': 4, 'ACC': 5, 'HYD': 6, 'OTH': 7}

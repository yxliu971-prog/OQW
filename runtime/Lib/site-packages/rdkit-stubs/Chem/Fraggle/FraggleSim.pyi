"""

Fragmentation algorithm
-----------------------

identify acyclic bonds
enumerate all single cuts
make sure you chop off more that 1 atom
keeps bits which are >60% query mol
enumerate all double cuts
keeps bits with 1 attachment point (i.e throw middle bit away)
need to be >60% query mol

identify exocyclic bonds
enumerate all single "ring" cuts
Check if it results in more that one component
keep correct bit if >40% query mol

enumerate successful "rings" cuts with an acyclic cut
Check if it results in more that one component
keep correct if >60% query mol

"""
from __future__ import annotations
from itertools import combinations
from rdkit import Chem
import rdkit.Chem.rdchem
from rdkit.Chem import rdqueries
from rdkit import DataStructs
import sys as sys
__all__: list[str] = ['ACYC_SMARTS', 'CYC_SMARTS', 'Chem', 'DataStructs', 'FTYPE_ACYCLIC', 'FTYPE_CYCLIC', 'FTYPE_CYCLIC_ACYCLIC', 'GetFraggleSimilarity', 'atomContrib', 'cSma1', 'cSma2', 'combinations', 'compute_fraggle_similarity_for_subs', 'delete_bonds', 'dummyAtomQuery', 'generate_fraggle_fragmentation', 'isValidRingCut', 'modified_query_fps', 'rdkitFpParams', 'rdqueries', 'select_fragments', 'sys']
def GetFraggleSimilarity(queryMol, refMol, tverskyThresh = 0.8):
    """
     return the Fraggle similarity between two molecules
    
        >>> q = Chem.MolFromSmiles('COc1cc(CN2CCC(NC(=O)c3cncc(C)c3)CC2)c(OC)c2ccccc12')
        >>> m = Chem.MolFromSmiles('COc1cc(CN2CCC(NC(=O)c3ccccc3)CC2)c(OC)c2ccccc12')
        >>> sim,match = GetFraggleSimilarity(q,m)
        >>> sim
        0.980...
        >>> match
        '*C1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1'
    
        >>> m = Chem.MolFromSmiles('COc1cc(CN2CCC(Nc3nc4ccccc4s3)CC2)c(OC)c2ccccc12')
        >>> sim,match = GetFraggleSimilarity(q,m)
        >>> sim
        0.794...
        >>> match
        '*C1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1'
    
        >>> q = Chem.MolFromSmiles('COc1ccccc1')
        >>> sim,match = GetFraggleSimilarity(q,m)
        >>> sim
        0.347...
        >>> match
        '*c1ccccc1'
    
        
    """
def _runDoctests(verbose = None):
    ...
def atomContrib(subs, mol, tverskyThresh = 0.8):
    """
     atomContrib algorithm
      generate fp of query_substructs (qfp)
    
      loop through atoms of smiles
        For each atom
        Generate partial fp of the atom (pfp)
        Find Tversky sim of pfp in qfp
        If Tversky < 0.8, mark atom in smiles
    
      Loop through marked atoms
        If marked atom in ring - turn all atoms in that ring to * (aromatic) or Sc (aliphatic)
        For each marked atom
          If aromatic turn to a *
          If aliphatic turn to a Sc
    
      Return modified smiles
      
    """
def compute_fraggle_similarity_for_subs(inMol, qMol, qSmi, qSubs, tverskyThresh = 0.8):
    ...
def delete_bonds(mol, bonds, ftype, hac):
    """
     Fragment molecule on bonds and reduce to fraggle fragmentation SMILES.
      If none exists, returns None 
    """
def generate_fraggle_fragmentation(mol, verbose = False):
    """
     Create all possible fragmentations for molecule
        >>> q = Chem.MolFromSmiles('COc1cc(CN2CCC(NC(=O)c3cncc(C)c3)CC2)c(OC)c2ccccc12')
        >>> fragments = generate_fraggle_fragmentation(q)
        >>> fragments = sorted(['.'.join(sorted(s.split('.'))) for s in fragments])
        >>> fragments
         ['*C(=O)NC1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1',
          '*C(=O)c1cncc(C)c1.*C1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1',
          '*C(=O)c1cncc(C)c1.*Cc1cc(OC)c2ccccc2c1OC',
          '*C(=O)c1cncc(C)c1.*c1cc(OC)c2ccccc2c1OC',
          '*C1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1',
          '*C1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1.*c1cncc(C)c1',
          '*Cc1cc(OC)c2ccccc2c1OC.*NC(=O)c1cncc(C)c1',
          '*Cc1cc(OC)c2ccccc2c1OC.*c1cncc(C)c1',
          '*N1CCC(NC(=O)c2cncc(C)c2)CC1.*c1cc(OC)c2ccccc2c1OC',
          '*NC(=O)c1cncc(C)c1.*c1cc(OC)c2ccccc2c1OC',
          '*NC1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1',
          '*NC1CCN(Cc2cc(OC)c3ccccc3c2OC)CC1.*c1cncc(C)c1',
          '*c1c(CN2CCC(NC(=O)c3cncc(C)c3)CC2)cc(OC)c2ccccc12',
          '*c1c(OC)cc(CN2CCC(NC(=O)c3cncc(C)c3)CC2)c(OC)c1*',
          '*c1cc(CN2CCC(NC(=O)c3cncc(C)c3)CC2)c(OC)c2ccccc12',
          '*c1cc(OC)c2ccccc2c1OC.*c1cncc(C)c1']
      
    """
def isValidRingCut(mol):
    """
     to check is a fragment is a valid ring cut, it needs to match the
      SMARTS: [$([#0][r].[r][#0]),$([#0][r][#0])] 
    """
def select_fragments(fragments, ftype, hac):
    ...
ACYC_SMARTS: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
CYC_SMARTS: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
FTYPE_ACYCLIC: str = 'acyclic'
FTYPE_CYCLIC: str = 'cyclic'
FTYPE_CYCLIC_ACYCLIC: str = 'cyclic_and_acyclic'
cSma1: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
cSma2: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
dummyAtomQuery: rdkit.Chem.rdchem.QueryAtom  # value = <rdkit.Chem.rdchem.QueryAtom object>
modified_query_fps: dict = {}
rdkitFpParams: dict = {'maxPath': 5, 'fpSize': 1024, 'nBitsPerHash': 2}

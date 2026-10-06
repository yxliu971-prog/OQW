"""
 Calculation of topological/topochemical descriptors.



"""
from __future__ import annotations
import math as math
import numpy as numpy
from rdkit import Chem
from rdkit.Chem import Graphs
from rdkit.Chem import rdMolDescriptors
import rdkit.Chem.rdchem
from rdkit.Chem import rdchem
from rdkit.ML.InfoTheory import entropy
__all__: list[str] = ['AvgIpc', 'BalabanJ', 'BertzCT', 'Chem', 'Chi0', 'Chi1', 'Graphs', 'Ipc', 'entropy', 'hallKierAlphas', 'math', 'numpy', 'ptable', 'rdMolDescriptors', 'rdchem']
def AvgIpc(mol, dMat = None, forceDMat = False):
    """
    This returns the average information content of the coefficients of the characteristic
        polynomial of the adjacency matrix of a hydrogen-suppressed graph of a molecule.
    
        From Eq 7 of D. Bonchev & N. Trinajstic, J. Chem. Phys. vol 67, 4517-4533 (1977)
    
      
    """
def BalabanJ(mol, dMat = None, forceDMat = 0):
    """
     Calculate Balaban's J value for a molecule
    
      **Arguments**
    
        - mol: a molecule
    
        - dMat: (optional) a distance/adjacency matrix for the molecule, if this
          is not provide, one will be calculated
    
        - forceDMat: (optional) if this is set, the distance/adjacency matrix
          will be recalculated regardless of whether or not _dMat_ is provided
          or the molecule already has one
    
      **Returns**
    
        - a float containing the J value
    
      We follow the notation of Balaban's paper:
        Chem. Phys. Lett. vol 89, 399-404, (1982)
    
      
    """
def BertzCT(mol, cutoff = 100, dMat = None, forceDMat = 1):
    """
     A topological index meant to quantify "complexity" of molecules.
    
         Consists of a sum of two terms, one representing the complexity
         of the bonding, the other representing the complexity of the
         distribution of heteroatoms.
    
         From S. H. Bertz, J. Am. Chem. Soc., vol 103, 3599-3601 (1981)
    
         "cutoff" is an integer value used to limit the computational
         expense.  A cutoff value tells the program to consider vertices
         topologically identical if their distance vectors (sets of
         distances to all other vertices) are equal out to the "cutoff"th
         nearest-neighbor.
    
         **NOTE**  The original implementation had the following comment:
             > this implementation treats aromatic rings as the
             > corresponding Kekule structure with alternating bonds,
             > for purposes of counting "connections".
           Upon further thought, this is the WRONG thing to do.  It
            results in the possibility of a molecule giving two different
            CT values depending on the kekulization.  For example, in the
            old implementation, these two SMILES:
               CC2=CN=C1C3=C(C(C)=C(C=N3)C)C=CC1=C2C
               CC3=CN=C2C1=NC=C(C)C(C)=C1C=CC2=C3C
            which correspond to differentk kekule forms, yield different
            values.
           The new implementation uses consistent (aromatic) bond orders
            for aromatic bonds.
    
           THIS MEANS THAT THIS IMPLEMENTATION IS NOT BACKWARDS COMPATIBLE.
    
           Any molecule containing aromatic rings will yield different
           values with this implementation.  The new behavior is the correct
           one, so we're going to live with the breakage.
    
         **NOTE** this barfs if the molecule contains a second (or
           nth) fragment that is one atom.
    
      
    """
def Chi0(mol):
    """
     From equations (1),(9) and (10) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def Chi1(mol):
    """
     From equations (1),(11) and (12) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def Ipc(mol, avg = False, dMat = None, forceDMat = False):
    """
    This returns the information content of the coefficients of the characteristic
        polynomial of the adjacency matrix of a hydrogen-suppressed graph of a molecule.
    
        'avg = True' returns the information content divided by the total population.
    
        From Eq 6 of D. Bonchev & N. Trinajstic, J. Chem. Phys. vol 67, 4517-4533 (1977)
    
      
    """
def _AssignSymmetryClasses(mol, vdList, bdMat, forceBDMat, numAtoms, cutoff):
    """
    
         Used by BertzCT
    
         vdList: the number of neighbors each atom has
         bdMat: "balaban" distance matrix
    
      
    """
def _CalculateEntropies(connectionDict, atomTypeDict, numAtoms):
    """
    
         Used by BertzCT
      
    """
def _CreateBondDictEtc(mol, numAtoms):
    """
     _Internal Use Only_
         Used by BertzCT
    
      
    """
def _GetCountDict(arr):
    """
      *Internal Use Only*
    
      
    """
def _LookUpBondOrder(atom1Id, atom2Id, bondDic):
    """
    
         Used by BertzCT
      
    """
def _NumAdjacencies(mol, dMat):
    """
      *Internal Use Only*
    
      
    """
def _VertexDegrees(mat, onlyOnes = 0):
    """
      *Internal Use Only*
    
      this is just a row sum of the matrix... simple, neh?
    
      
    """
def _hkDeltas(mol, skipHs = 1):
    ...
def _nVal(atom):
    ...
def _pyChi0n(mol):
    """
      Similar to Hall Kier Chi0v, but uses nVal instead of valence
      This makes a big difference after we get out of the first row.
    
      
    """
def _pyChi0v(mol):
    """
      From equations (5),(9) and (10) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyChi1n(mol):
    """
      Similar to Hall Kier Chi1v, but uses nVal instead of valence
    
      
    """
def _pyChi1v(mol):
    """
      From equations (5),(11) and (12) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyChi2n(mol):
    """
      Similar to Hall Kier Chi2v, but uses nVal instead of valence
      This makes a big difference after we get out of the first row.
    
      
    """
def _pyChi2v(mol):
    """
     From equations (5),(15) and (16) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyChi3n(mol):
    """
      Similar to Hall Kier Chi3v, but uses nVal instead of valence
      This makes a big difference after we get out of the first row.
    
      
    """
def _pyChi3v(mol):
    """
     From equations (5),(15) and (16) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyChi4n(mol):
    """
      Similar to Hall Kier Chi4v, but uses nVal instead of valence
      This makes a big difference after we get out of the first row.
    
    
      **NOTE**: because the current path finding code does, by design,
      detect rings as paths (e.g. in C1CC1 there is *1* atom path of
      length 3), values of Chi4n may give results that differ from those
      provided by the old code in molecules that have 3 rings.
    
      
    """
def _pyChi4v(mol):
    """
     From equations (5),(15) and (16) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      **NOTE**: because the current path finding code does, by design,
      detect rings as paths (e.g. in C1CC1 there is *1* atom path of
      length 3), values of Chi4v may give results that differ from those
      provided by the old code in molecules that have 3 rings.
    
      
    """
def _pyChiNn_(mol, order = 2):
    """
      Similar to Hall Kier ChiNv, but uses nVal instead of valence
      This makes a big difference after we get out of the first row.
    
      **NOTE**: because the current path finding code does, by design,
      detect rings as paths (e.g. in C1CC1 there is *1* atom path of
      length 3), values of ChiNn with N >= 3 may give results that differ
      from those provided by the old code in molecules that have rings of
      size 3.
    
      
    """
def _pyChiNv_(mol, order = 2):
    """
      From equations (5),(15) and (16) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      **NOTE**: because the current path finding code does, by design,
      detect rings as paths (e.g. in C1CC1 there is *1* atom path of
      length 3), values of ChiNv with N >= 3 may give results that differ
      from those provided by the old code in molecules that have rings of
      size 3.
    
      
    """
def _pyHallKierAlpha(m):
    """
     calculate the Hall-Kier alpha value for a molecule
    
       From equations (58) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyKappa1(mol):
    """
     Hall-Kier Kappa1 value
    
       From equations (58) and (59) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyKappa2(mol):
    """
      Hall-Kier Kappa2 value
    
       From equations (58) and (60) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
def _pyKappa3(mol):
    """
      Hall-Kier Kappa3 value
    
       From equations (58), (61) and (62) of Rev. Comp. Chem. vol 2, 367-422, (1991)
    
      
    """
_log2val: float = 0.6931471805599453
hallKierAlphas: dict = {'Br': [None, None, 0.48], 'C': [-0.22, -0.13, 0.0], 'Cl': [None, None, 0.29], 'F': [None, None, -0.07], 'H': [0.0, 0.0, 0.0], 'I': [None, None, 0.73], 'N': [-0.29, -0.2, -0.04], 'O': [None, -0.2, -0.04], 'P': [None, 0.3, 0.43], 'S': [None, 0.22, 0.35]}
ptable: rdkit.Chem.rdchem.PeriodicTable  # value = <rdkit.Chem.rdchem.PeriodicTable object>

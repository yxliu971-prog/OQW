"""
 Torsion Fingerprints (Deviation) (TFD)
    According to a paper from Schulz-Gasch et al., JCIM, 52, 1499-1512 (2012).

"""
from __future__ import annotations
import math as math
import os as os
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import rdchem
from rdkit import Geometry
from rdkit import RDConfig
from rdkit import rdBase
__all__: list[str] = ['CalculateTFD', 'CalculateTorsionAngles', 'CalculateTorsionLists', 'CalculateTorsionWeights', 'Chem', 'Geometry', 'GetBestTFDBetweenMolecules', 'GetTFDBetweenConformers', 'GetTFDBetweenMolecules', 'GetTFDMatrix', 'RDConfig', 'math', 'os', 'rdBase', 'rdFingerprintGenerator', 'rdMolDescriptors', 'rdchem']
def CalculateTFD(torsions1, torsions2, weights = None):
    """
     Calculate the torsion deviation fingerprint (TFD) given two lists of
          torsion angles.
    
          Arguments:
          - torsions1:  torsion angles of conformation 1
          - torsions2:  torsion angles of conformation 2
          - weights:    list of torsion weights (default: None)
    
          Return: TFD value (float)
      
    """
def CalculateTorsionAngles(mol, tors_list, tors_list_rings, confId = -1):
    """
     Calculate the torsion angles for a list of non-ring and 
          a list of ring torsions.
    
          Arguments:
          - mol:       the molecule of interest
          - tors_list: list of non-ring torsions
          - tors_list_rings: list of ring torsions
          - confId:    index of the conformation (default: first conformer)
    
          Return: list of torsion angles
      
    """
def CalculateTorsionLists(mol, maxDev = 'equal', symmRadius = 2, ignoreColinearBonds = True):
    """
     Calculate a list of torsions for a given molecule. For each torsion
          the four atom indices are determined and stored in a set.
    
          Arguments:
          - mol:      the molecule of interest
          - maxDev:   maximal deviation used for normalization
                      'equal': all torsions are normalized using 180.0 (default)
                      'spec':  each torsion is normalized using its specific
                               maximal deviation as given in the paper
          - symmRadius: radius used for calculating the atom invariants
                        (default: 2)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: two lists of torsions: non-ring and ring torsions
      
    """
def CalculateTorsionWeights(mol, aid1 = -1, aid2 = -1, ignoreColinearBonds = True):
    """
     Calculate the weights for the torsions in a molecule.
          By default, the highest weight is given to the bond 
          connecting the two most central atoms.
          If desired, two alternate atoms can be specified (must 
          be connected by a bond).
    
          Arguments:
          - mol:   the molecule of interest
          - aid1:  index of the first atom (default: most central)
          - aid2:  index of the second atom (default: second most central)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: list of torsion weights (both non-ring and ring)
      
    """
def GetBestTFDBetweenMolecules(mol1, mol2, confId1 = -1, useWeights = True, maxDev = 'equal', symmRadius = 2, ignoreColinearBonds = True):
    """
     Wrapper to calculate the best TFD between a single conformer of mol1 and all the conformers of mol2
          Important: The two molecules must be isomorphic
    
          Arguments:
          - mol1:     first instance of the molecule of interest
          - mol2:     second instance the molecule of interest
          - confId1:  conformer index for mol1 (default: first conformer)
          - useWeights: flag for using torsion weights in the TFD calculation
          - maxDev:   maximal deviation used for normalization
                      'equal': all torsions are normalized using 180.0 (default)
                      'spec':  each torsion is normalized using its specific
                               maximal deviation as given in the paper
          - symmRadius: radius used for calculating the atom invariants
                        (default: 2)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: TFD value
      
    """
def GetTFDBetweenConformers(mol, confIds1, confIds2, useWeights = True, maxDev = 'equal', symmRadius = 2, ignoreColinearBonds = True):
    """
     Wrapper to calculate the TFD between two list of conformers 
          of a molecule
    
          Arguments:
          - mol:      the molecule of interest
          - confIds1:  first list of conformer indices
          - confIds2:  second list of conformer indices
          - useWeights: flag for using torsion weights in the TFD calculation
          - maxDev:   maximal deviation used for normalization
                      'equal': all torsions are normalized using 180.0 (default)
                      'spec':  each torsion is normalized using its specific
                               maximal deviation as given in the paper
          - symmRadius: radius used for calculating the atom invariants
                        (default: 2)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: list of TFD values
      
    """
def GetTFDBetweenMolecules(mol1, mol2, confId1 = -1, confId2 = -1, useWeights = True, maxDev = 'equal', symmRadius = 2, ignoreColinearBonds = True):
    """
     Wrapper to calculate the TFD between two molecules.
          Important: The two molecules must be isomorphic
    
          Arguments:
          - mol1:     first instance of the molecule of interest
          - mol2:     second instance the molecule of interest
          - confId1:  conformer index for mol1 (default: first conformer)
          - confId2:  conformer index for mol2 (default: first conformer)
          - useWeights: flag for using torsion weights in the TFD calculation
          - maxDev:   maximal deviation used for normalization
                      'equal': all torsions are normalized using 180.0 (default)
                      'spec':  each torsion is normalized using its specific
                               maximal deviation as given in the paper
          - symmRadius: radius used for calculating the atom invariants
                        (default: 2)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: TFD value
      
    """
def GetTFDMatrix(mol, useWeights = True, maxDev = 'equal', symmRadius = 2, ignoreColinearBonds = True):
    """
     Wrapper to calculate the matrix of TFD values for the
          conformers of a molecule.
    
          Arguments:
          - mol:      the molecule of interest
          - useWeights: flag for using torsion weights in the TFD calculation
          - maxDev:   maximal deviation used for normalization
                      'equal': all torsions are normalized using 180.0 (default)
                      'spec':  each torsion is normalized using its specific
                               maximal deviation as given in the paper
          - symmRadius: radius used for calculating the atom invariants
                        (default: 2)
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
    
          Return: matrix of TFD values
          Note that the returned matrix is symmetrical, i.e. it is the
          lower half of the matrix, e.g. for 5 conformers:
          matrix = [ a,
                     b, c,
                     d, e, f,
                     g, h, i, j]
      
    """
def _calculateBeta(mol, distmat, aid1):
    """
     Helper function to calculate the beta for torsion weights
          according to the formula in the paper.
          w(dmax/2) = 0.1
    
          Arguments:
          - mol:     the molecule of interest
          - distmat: distance matrix of the molecule
          - aid1:    atom index of the most central atom
    
          Return: value of beta (float)
      
    """
def _doMatch(inv, atoms):
    """
     Helper function to check if all atoms in the list are the same
          
          Arguments:
          - inv:    atom invariants (used to define equivalence of atoms)
          - atoms:  list of atoms to check
    
          Return: boolean
      
    """
def _doMatchExcept1(inv, atoms):
    """
     Helper function to check if two atoms in the list are the same, 
          and one not
          Note: Works only for three atoms
          
          Arguments:
          - inv:    atom invariants (used to define equivalence of atoms)
          - atoms:  list of atoms to check
    
          Return: atom that is different
      
    """
def _doNotMatch(inv, atoms):
    """
     Helper function to check if all atoms in the list are NOT the same
          
          Arguments:
          - inv:    atom invariants (used to define equivalence of atoms)
          - atoms:  list of atoms to check
    
          Return: boolean
      
    """
def _findCentralBond(mol, distmat):
    """
     Helper function to identify the atoms of the most central bond.
    
          Arguments:
          - mol:     the molecule of interest
          - distmat: distance matrix of the molecule
    
          Return: atom indices of the two most central atoms (in order)
      
    """
def _getAtomInvariantsWithRadius(mol, radius):
    """
     Helper function to calculate the atom invariants for each atom 
          with a given radius
    
          Arguments:
          - mol:    the molecule of interest
          - radius: the radius for the Morgan fingerprint
    
          Return: list of atom invariants
      
    """
def _getBondsForTorsions(mol, ignoreColinearBonds):
    """
     Determine the bonds (or pair of atoms treated like a bond) for which
          torsions should be calculated.
    
          Arguments:
          - refmol: the molecule of interest
          - ignoreColinearBonds: if True (default), single bonds adjacent to
                                 triple bonds are ignored
                                 if False, alternative not-covalently bound
                                 atoms are used to define the torsion
      
    """
def _getHeavyAtomNeighbors(atom1, aid2 = -1):
    """
     Helper function to calculate the number of heavy atom neighbors.
    
          Arguments:
          - atom1:    the atom of interest
          - aid2:     atom index that should be excluded from neighbors (default: none)
    
          Return: a list of heavy atom neighbors of the given atom
      
    """
def _getIndexforTorsion(neighbors, inv):
    """
     Helper function to calculate the index of the reference atom for 
          a given atom
    
          Arguments:
          - neighbors:  list of the neighbors of the atom
          - inv:        atom invariants
    
          Return: list of atom indices as reference for torsion
      
    """
def _getSameAtomOrder(mol1, mol2):
    """
     Generate a new molecule with the atom order of mol1 and coordinates
          from mol2.
          
          Arguments:
          - mol1:     first instance of the molecule of interest
          - mol2:     second instance the molecule of interest
    
          Return: RDKit molecule
      
    """
def _getTorsionAtomPositions(atoms, conf):
    """
     Helper function to retrieve the coordinates of the four atoms
          in a torsion
    
          Arguments:
          - atoms:   list with the four atoms
          - conf:    conformation of the molecule
    
          Return: Point3D objects of the four atoms
      
    """

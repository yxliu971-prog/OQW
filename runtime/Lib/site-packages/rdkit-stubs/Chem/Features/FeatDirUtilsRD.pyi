from __future__ import annotations
import math as math
import numpy as numpy
from rdkit import Chem
from rdkit import Geometry
__all__: list[str] = ['ArbAxisRotation', 'Chem', 'Geometry', 'GetAcceptor1FeatVects', 'GetAcceptor2FeatVects', 'GetAcceptor3FeatVects', 'GetAromaticFeatVects', 'GetDonor1FeatVects', 'GetDonor2FeatVects', 'GetDonor3FeatVects', 'cross', 'findNeighbors', 'math', 'numpy']
def ArbAxisRotation(theta, ax, pt):
    ...
def GetAcceptor1FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Acceptor of type 1
    
      This is a acceptor with one heavy atom neighbor. There are two possibilities we will
      consider here
      1. The bond to the heavy atom is a single bond e.g. CO
         In this case we don't know the exact direction and we just use the inversion of this bond direction
         and mark this direction as a 'cone'
      2. The bond to the heavy atom is a double bond e.g. C=O
         In this case the we have two possible direction except in some special cases e.g. SO2
         where again we will use bond direction
         
      ARGUMENTS:
        featAtoms - list of atoms that are part of the feature
        scale - length of the direction vector
      
    """
def GetAcceptor2FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Acceptor of type 2
      
      This is the acceptor with two adjacent heavy atoms. We will special case a few things here.
      If the acceptor atom is an oxygen we will assume a sp3 hybridization
      the acceptor directions (two of them)
      reflect that configurations. Otherwise the direction vector in plane with the neighboring
      heavy atoms
      
      ARGUMENTS:
          featAtoms - list of atoms that are part of the feature
          scale - length of the direction vector
      
    """
def GetAcceptor3FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Donor of type 3
    
      This is a donor with three heavy atoms as neighbors. We will assume
      a tetrahedral arrangement of these neighbors. So the direction we are seeking
      is the last fourth arm of the sp3 arrangement
    
      ARGUMENTS:
        featAtoms - list of atoms that are part of the feature
        scale - length of the direction vector
      
    """
def GetAromaticFeatVects(conf, featAtoms, featLoc, scale = 1.5):
    """
    
      Compute the direction vector for an aromatic feature
      
      ARGUMENTS:
         conf - a conformer
         featAtoms - list of atom IDs that make up the feature
         featLoc - location of the aromatic feature specified as point3d
         scale - the size of the direction vector
      
    """
def GetDonor1FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Donor of type 1
    
      This is a donor with one heavy atom. It is not clear where we should we should be putting the
      direction vector for this. It should probably be a cone. In this case we will just use the
      direction vector from the donor atom to the heavy atom
        
      ARGUMENTS:
        
        featAtoms - list of atoms that are part of the feature
        scale - length of the direction vector
      
    """
def GetDonor2FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Donor of type 2
    
      This is a donor with two heavy atoms as neighbors. The atom may are may not have
      hydrogen on it. Here are the situations with the neighbors that will be considered here
        1. two heavy atoms and two hydrogens: we will assume a sp3 arrangement here
        2. two heavy atoms and one hydrogen: this can either be sp2 or sp3
        3. two heavy atoms and no hydrogens
        
      ARGUMENTS:
        featAtoms - list of atoms that are part of the feature
        scale - length of the direction vector
      
    """
def GetDonor3FeatVects(conf, featAtoms, scale = 1.5):
    """
    
      Get the direction vectors for Donor of type 3
    
      This is a donor with three heavy atoms as neighbors. We will assume
      a tetrahedral arrangement of these neighbors. So the direction we are seeking
      is the last fourth arm of the sp3 arrangement
    
      ARGUMENTS:
        featAtoms - list of atoms that are part of the feature
        scale - length of the direction vector
      
    """
def _GetTetrahedralFeatVect(conf, aid, scale):
    ...
def _checkPlanarity(conf, cpt, nbrs, tol = 0.001):
    ...
def _findAvgVec(conf, center, nbrs):
    ...
def _findHydAtoms(nbrs, atomNames):
    ...
def cross(v1, v2):
    ...
def findNeighbors(atomId, adjMat):
    """
    
      Find the IDs of the neighboring atom IDs
      
      ARGUMENTS:
      atomId - atom of interest
      adjMat - adjacency matrix for the compound
      
    """

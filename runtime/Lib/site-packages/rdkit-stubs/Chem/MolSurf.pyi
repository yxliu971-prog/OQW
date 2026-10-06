"""
 Exposes functionality for MOE-like approximate molecular surface area
descriptors.

  The MOE-like VSA descriptors are also calculated here

"""
from __future__ import annotations
import bisect as bisect
import numpy as numpy
from rdkit import Chem
from rdkit.Chem import Crippen
from rdkit.Chem import rdMolDescriptors
from rdkit.Chem import rdPartialCharges
import rdkit.Chem.rdchem
__all__: list[str] = ['Chem', 'Crippen', 'bisect', 'bondScaleFacts', 'chgBins', 'logpBins', 'mrBins', 'numpy', 'ptable', 'pyLabuteASA', 'pyPEOE_VSA_', 'pySMR_VSA_', 'pySlogP_VSA_', 'rdMolDescriptors', 'rdPartialCharges']
def _InstallDescriptors():
    ...
def _LabuteHelper(mol, includeHs = 1, force = 0):
    """
     *Internal Use Only*
        helper function for LabuteASA calculation
        returns an array of atomic contributions to the ASA
    
      **Note:** Changes here affect the version numbers of all ASA descriptors
    
      
    """
def _pyLabuteHelper(mol, includeHs = 1, force = 0):
    """
     *Internal Use Only*
        helper function for LabuteASA calculation
        returns an array of atomic contributions to the ASA
    
      **Note:** Changes here affect the version numbers of all ASA descriptors
    
      
    """
def _pyTPSA(mol, verbose = False):
    """
     DEPRECATED: this has been reimplmented in C++
       calculates the polar surface area of a molecule based upon fragments
    
       Algorithm in:
        P. Ertl, B. Rohde, P. Selzer
         Fast Calculation of Molecular Polar Surface Area as a Sum of Fragment-based
         Contributions and Its Application to the Prediction of Drug Transport
         Properties, J.Med.Chem. 43, 3714-3717, 2000
    
       Implementation based on the Daylight contrib program tpsa.c
      
    """
def _pyTPSAContribs(mol, verbose = False):
    """
     DEPRECATED: this has been reimplmented in C++
      calculates atomic contributions to a molecules TPSA
    
       Algorithm described in:
        P. Ertl, B. Rohde, P. Selzer
         Fast Calculation of Molecular Polar Surface Area as a Sum of Fragment-based
         Contributions and Its Application to the Prediction of Drug Transport
         Properties, J.Med.Chem. 43, 3714-3717, 2000
    
       Implementation based on the Daylight contrib program tpsa.c
    
       NOTE: The JMC paper describing the TPSA algorithm includes
       contributions from sulfur and phosphorus, however according to
       Peter Ertl (personal communication, 2010) the correlation of TPSA
       with various ADME properties is better if only contributions from
       oxygen and nitrogen are used. This matches the daylight contrib
       implementation.
    
      
    """
def pyLabuteASA(mol, includeHs = 1):
    """
     calculates Labute's Approximate Surface Area (ASA from MOE)
    
        Definition from P. Labute's article in the Journal of the Chemical Computing Group
        and J. Mol. Graph. Mod.  _18_ 464-477 (2000)
    
      
    """
def pyPEOE_VSA_(mol, bins = None, force = 1):
    """
     *Internal Use Only*
      
    """
def pySMR_VSA_(mol, bins = None, force = 1):
    """
     *Internal Use Only*
      
    """
def pySlogP_VSA_(mol, bins = None, force = 1):
    """
     *Internal Use Only*
      
    """
bondScaleFacts: list = [0.1, 0, 0.2, 0.3]
chgBins: list = [-0.3, -0.25, -0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]
logpBins: list = [-0.4, -0.2, 0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6]
mrBins: list = [1.29, 1.82, 2.24, 2.45, 2.75, 3.05, 3.63, 3.8, 4.0]
ptable: rdkit.Chem.rdchem.PeriodicTable  # value = <rdkit.Chem.rdchem.PeriodicTable object>

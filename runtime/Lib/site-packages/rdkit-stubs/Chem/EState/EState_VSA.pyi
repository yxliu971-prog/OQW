"""
 Hybrid EState-VSA descriptors (like the MOE VSA descriptors)

"""
from __future__ import annotations
import bisect as bisect
import numpy as numpy
from rdkit.Chem.EState.EState import EStateIndices as EStateIndices_
from rdkit.Chem.MolSurf import _LabuteHelper as VSAContribs_
__all__: list[str] = ['EStateIndices_', 'EState_VSA1', 'EState_VSA10', 'EState_VSA11', 'EState_VSA2', 'EState_VSA3', 'EState_VSA4', 'EState_VSA5', 'EState_VSA6', 'EState_VSA7', 'EState_VSA8', 'EState_VSA9', 'EState_VSA_', 'VSAContribs_', 'VSA_EState_', 'bisect', 'estateBins', 'numpy', 'vsaBins']
def EState_VSA1(mol):
    """
    EState VSA Descriptor 1 (-inf < x <  -0.39)
    """
def EState_VSA10(mol):
    """
    EState VSA Descriptor 10 ( 9.17 <= x <  15.00)
    """
def EState_VSA11(mol):
    """
    EState VSA Descriptor 11 ( 15.00 <= x < inf)
    """
def EState_VSA2(mol):
    """
    EState VSA Descriptor 2 ( -0.39 <= x <  0.29)
    """
def EState_VSA3(mol):
    """
    EState VSA Descriptor 3 ( 0.29 <= x <  0.72)
    """
def EState_VSA4(mol):
    """
    EState VSA Descriptor 4 ( 0.72 <= x <  1.17)
    """
def EState_VSA5(mol):
    """
    EState VSA Descriptor 5 ( 1.17 <= x <  1.54)
    """
def EState_VSA6(mol):
    """
    EState VSA Descriptor 6 ( 1.54 <= x <  1.81)
    """
def EState_VSA7(mol):
    """
    EState VSA Descriptor 7 ( 1.81 <= x <  2.05)
    """
def EState_VSA8(mol):
    """
    EState VSA Descriptor 8 ( 2.05 <= x <  4.69)
    """
def EState_VSA9(mol):
    """
    EState VSA Descriptor 9 ( 4.69 <= x <  9.17)
    """
def EState_VSA_(mol, bins = None, force = 1):
    """
     *Internal Use Only*
      
    """
def VSA_EState_(mol, bins = None, force = 1):
    """
     *Internal Use Only*
      
    """
def _InstallDescriptors():
    ...
def _descriptorDocstring(name, nbin, bins):
    """
     Create a docstring for the descriptor name 
    """
def _descriptor_EState_VSA(nbin):
    ...
def _descriptor_VSA_EState(nbin):
    ...
estateBins: list = [-0.39, 0.29, 0.717, 1.165, 1.54, 1.807, 2.05, 4.69, 9.17, 15.0]
vsaBins: list = [4.78, 5.0, 5.41, 5.74, 6.0, 6.07, 6.45, 7.0, 11.0]

"""
 Various bits and pieces for calculating Molecular descriptors

"""
from __future__ import annotations
import pickle as pickle
from rdkit.Chem import Descriptors as DescriptorsMod
import rdkit.ML.Descriptors.Descriptors
from rdkit.ML.Descriptors import Descriptors
import rdkit.RDLogger
import re as re
__all__: list[str] = ['Descriptors', 'DescriptorsMod', 'MolecularDescriptorCalculator', 'logger', 'pickle', 're']
class MolecularDescriptorCalculator(rdkit.ML.Descriptors.Descriptors.DescriptorCalculator):
    """
     used for calculating descriptors for molecules
    
      
    """
    def CalcDescriptors(self, mol, *args, **kwargs):
        """
         calculates all descriptors for a given molecule
        
              **Arguments**
        
                - mol: the molecule to be used
        
              **Returns**
                a tuple of all descriptor values
        
            
        """
    def GetDescriptorFuncs(self):
        """
         returns a tuple of the functions used to generate this calculator's descriptors
        
            
        """
    def GetDescriptorNames(self):
        """
         returns a tuple of the names of the descriptors this calculator generates
        
            
        """
    def GetDescriptorSummaries(self):
        """
         returns a tuple of summaries for the descriptors this calculator generates
        
            
        """
    def GetDescriptorVersions(self):
        """
         returns a tuple of the versions of the descriptor calculators
        
            
        """
    def SaveState(self, fileName):
        """
         Writes this calculator off to a file so that it can be easily loaded later
        
             **Arguments**
        
               - fileName: the name of the file to be written
        
            
        """
    def __init__(self, simpleList, *args, **kwargs):
        """
         Constructor
        
              **Arguments**
        
                - simpleList: list of simple descriptors to be calculated
                      (see below for format)
        
              **Note**
        
                - format of simpleList:
        
                   a list of strings which are functions in the rdkit.Chem.Descriptors module
        
            
        """
    def _findVersions(self):
        """
         returns a tuple of the versions of the descriptor calculators
        
            
        """
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>

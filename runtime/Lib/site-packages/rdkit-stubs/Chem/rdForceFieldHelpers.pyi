"""
Module containing functions to handle force fields
"""
from __future__ import annotations
import rdkit
import typing
__all__: list[str] = ['CreateEmptyForceFieldForMol', 'GetUFFAngleBendParams', 'GetUFFBondStretchParams', 'GetUFFInversionParams', 'GetUFFTorsionParams', 'GetUFFVdWParams', 'MMFFGetMoleculeForceField', 'MMFFGetMoleculeProperties', 'MMFFHasAllMoleculeParams', 'MMFFOptimizeMolecule', 'MMFFOptimizeMoleculeConfs', 'MMFFSanitizeMolecule', 'OptimizeMolecule', 'OptimizeMoleculeConfs', 'UFFGetMoleculeForceField', 'UFFHasAllMoleculeParams', 'UFFOptimizeMolecule', 'UFFOptimizeMoleculeConfs']
def CreateEmptyForceFieldForMol(mol: Mol, confId: int = -1) -> rdkit.ForceField:
    """
        Get An empty Force Field, with only the positions of the atoms but no Contributions.
        
          
          ARGUMENTS :
        
              - mol : the molecule of interest
              - confId: the conformer which positions should be added to the force field.
        
         
    
        C++ signature :
            class ForceFields::PyForceField * __ptr64 CreateEmptyForceFieldForMol(class RDKit::ROMol {lvalue} [,int=-1])
    """
def GetUFFAngleBendParams(mol: Mol, idx1: int, idx2: int, idx3: int) -> typing.Any:
    """
        Retrieves UFF angle bend parameters for atoms with indexes idx1, idx2, idx3 as a (ka, theta0) tuple, or None if no parameters could be found
    
        C++ signature :
            struct _object * __ptr64 GetUFFAngleBendParams(class RDKit::ROMol,unsigned int,unsigned int,unsigned int)
    """
def GetUFFBondStretchParams(mol: Mol, idx1: int, idx2: int) -> typing.Any:
    """
        Retrieves UFF bond stretch parameters for atoms with indexes idx1, idx2 as a (kb, r0) tuple, or None if no parameters could be found
    
        C++ signature :
            struct _object * __ptr64 GetUFFBondStretchParams(class RDKit::ROMol,unsigned int,unsigned int)
    """
def GetUFFInversionParams(mol: Mol, idx1: int, idx2: int, idx3: int, idx4: int) -> typing.Any:
    """
        Retrieves UFF inversion parameters for atoms with indexes idx1, idx2, idx3, idx4 as a K float value, or None if no parameters could be found
    
        C++ signature :
            struct _object * __ptr64 GetUFFInversionParams(class RDKit::ROMol,unsigned int,unsigned int,unsigned int,unsigned int)
    """
def GetUFFTorsionParams(mol: Mol, idx1: int, idx2: int, idx3: int, idx4: int) -> typing.Any:
    """
        Retrieves UFF torsion parameters for atoms with indexes idx1, idx2, idx3, idx4 as a V float value, or None if no parameters could be found
    
        C++ signature :
            struct _object * __ptr64 GetUFFTorsionParams(class RDKit::ROMol,unsigned int,unsigned int,unsigned int,unsigned int)
    """
def GetUFFVdWParams(mol: Mol, idx1: int, idx2: int) -> typing.Any:
    """
        Retrieves UFF van der Waals parameters for atoms with indexes idx1, idx2 as a (x_ij, D_ij) tuple, or None if no parameters could be found
    
        C++ signature :
            struct _object * __ptr64 GetUFFVdWParams(class RDKit::ROMol,unsigned int,unsigned int)
    """
def MMFFGetMoleculeForceField(mol: Mol, pyMMFFMolProperties: MMFFMolProperties, nonBondedThresh: float = 100.0, confId: int = -1, ignoreInterfragInteractions: bool = True) -> rdkit.ForceField:
    """
        returns a MMFF force field for a molecule
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - pyMMFFMolProperties : PyMMFFMolProperties object as returned
                          by MMFFGetMoleculeProperties()
            - nonBondedThresh : used to exclude long-range non-bonded
                          interactions (defaults to 100.0)
            - confId : indicates which conformer to optimize
            - ignoreInterfragInteractions : if true, nonbonded terms between
                          fragments will not be added to the forcefield
        
        
    
        C++ signature :
            class ForceFields::PyForceField * __ptr64 MMFFGetMoleculeForceField(class RDKit::ROMol {lvalue},class ForceFields::PyMMFFMolProperties * __ptr64 [,double=100.0 [,int=-1 [,bool=True]]])
    """
def MMFFGetMoleculeProperties(mol: Mol, mmffVariant: str = 'MMFF94', mmffVerbosity: int = 0) -> MMFFMolProperties:
    """
        returns a PyMMFFMolProperties object for a
          molecule, which is required by MMFFGetMoleculeForceField()
          and can be used to get/set MMFF properties
        
          
          ARGUMENTS:
        
            - mol : the molecule of interest
            - mmffVariant : "MMFF94" or "MMFF94s"
                          (defaults to "MMFF94")
            - mmffVerbosity : 0: none; 1: low; 2: high (defaults to 0).
        
        
    
        C++ signature :
            class ForceFields::PyMMFFMolProperties * __ptr64 MMFFGetMoleculeProperties(class RDKit::ROMol {lvalue} [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='MMFF94' [,unsigned int=0]])
    """
def MMFFHasAllMoleculeParams(mol: Mol) -> bool:
    """
        checks if MMFF parameters are available for all of a molecule's atoms
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
        
        
    
        C++ signature :
            bool MMFFHasAllMoleculeParams(class RDKit::ROMol)
    """
def MMFFOptimizeMolecule(mol: Mol, mmffVariant: str = 'MMFF94', maxIters: int = 200, nonBondedThresh: float = 100.0, confId: int = -1, ignoreInterfragInteractions: bool = True) -> int:
    """
        uses MMFF to optimize a molecule's structure
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - mmffVariant : "MMFF94" or "MMFF94s"
            - maxIters : the maximum number of iterations (defaults to 200)
            - nonBondedThresh : used to exclude long-range non-bonded
                         interactions (defaults to 100.0)
            - confId : indicates which conformer to optimize
            - ignoreInterfragInteractions : if true, nonbonded terms between
                         fragments will not be added to the forcefield
        
         RETURNS: 0 if the optimization converged, -1 if the forcefield could
                  not be set up, 1 if more iterations are required.
        
        
    
        C++ signature :
            int MMFFOptimizeMolecule(class RDKit::ROMol {lvalue} [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='MMFF94' [,int=200 [,double=100.0 [,int=-1 [,bool=True]]]]])
    """
def MMFFOptimizeMoleculeConfs(self: Mol, numThreads: int = 1, maxIters: int = 200, mmffVariant: str = 'MMFF94', nonBondedThresh: float = 100.0, ignoreInterfragInteractions: bool = True) -> typing.Any:
    """
        uses MMFF to optimize all of a molecule's conformations
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - numThreads : the number of threads to use, only has an effect if the RDKit
                           was built with thread support (defaults to 1)
                           If set to zero, the max supported by the system will be used.
            - maxIters : the maximum number of iterations (defaults to 200)
            - mmffVariant : "MMFF94" or "MMFF94s"
            - nonBondedThresh : used to exclude long-range non-bonded
                          interactions (defaults to 100.0)
            - ignoreInterfragInteractions : if true, nonbonded terms between
                          fragments will not be added to the forcefield.
        
        RETURNS: a list of (not_converged, energy) 2-tuples. 
            If not_converged is 0 the optimization converged for that conformer.
        
        
    
        C++ signature :
            class boost::python::api::object MMFFOptimizeMoleculeConfs(class RDKit::ROMol {lvalue} [,int=1 [,int=200 [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='MMFF94' [,double=100.0 [,bool=True]]]]])
    """
def MMFFSanitizeMolecule(mol: Mol) -> int:
    """
        sanitizes a molecule according to MMFF requirements.
        
            - mol : the molecule of interest.
        
        
    
        C++ signature :
            unsigned int MMFFSanitizeMolecule(class RDKit::ROMol {lvalue})
    """
def OptimizeMolecule(ff: ForceField, maxIters: int = 200) -> int:
    """
        uses the supplied force field to optimize a molecule's structure
        
         
         ARGUMENTS:
        
            - ff : the force field
            - maxIters : the maximum number of iterations (defaults to 200)
        
         RETURNS: 0 if the optimization converged, 1 if more iterations are required.
        
        
    
        C++ signature :
            int OptimizeMolecule(class ForceFields::PyForceField {lvalue} [,int=200])
    """
def OptimizeMoleculeConfs(mol: Mol, ff: ForceField, numThreads: int = 1, maxIters: int = 200) -> typing.Any:
    """
        uses the supplied force field to optimize all of a molecule's conformations
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - ff : the force field
            - numThreads : the number of threads to use, only has an effect if the RDKit
                           was built with thread support (defaults to 1)
                           If set to zero, the max supported by the system will be used.
            - maxIters : the maximum number of iterations (defaults to 200)
        
         RETURNS: a list of (not_converged, energy) 2-tuples. 
             If not_converged is 0 the optimization converged for that conformer.
        
        
    
        C++ signature :
            class boost::python::api::object OptimizeMoleculeConfs(class RDKit::ROMol {lvalue},class ForceFields::PyForceField {lvalue} [,int=1 [,int=200]])
    """
def UFFGetMoleculeForceField(mol: Mol, vdwThresh: float = 10.0, confId: int = -1, ignoreInterfragInteractions: bool = True) -> rdkit.ForceField:
    """
        returns a UFF force field for a molecule
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - vdwThresh : used to exclude long-range van der Waals interactions
                          (defaults to 10.0)
            - confId : indicates which conformer to optimize
            - ignoreInterfragInteractions : if true, nonbonded terms between
                          fragments will not be added to the forcefield.
        
        
    
        C++ signature :
            class ForceFields::PyForceField * __ptr64 UFFGetMoleculeForceField(class RDKit::ROMol {lvalue} [,double=10.0 [,int=-1 [,bool=True]]])
    """
def UFFHasAllMoleculeParams(mol: Mol) -> bool:
    """
        checks if UFF parameters are available for all of a molecule's atoms
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest.
        
        
    
        C++ signature :
            bool UFFHasAllMoleculeParams(class RDKit::ROMol)
    """
def UFFOptimizeMolecule(self: Mol, maxIters: int = 200, vdwThresh: float = 10.0, confId: int = -1, ignoreInterfragInteractions: bool = True) -> int:
    """
        uses UFF to optimize a molecule's structure
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - maxIters : the maximum number of iterations (defaults to 200)
            - vdwThresh : used to exclude long-range van der Waals interactions
                          (defaults to 10.0)
            - confId : indicates which conformer to optimize
            - ignoreInterfragInteractions : if true, nonbonded terms between
                          fragments will not be added to the forcefield.
        
         RETURNS: 0 if the optimization converged, 1 if more iterations are required.
        
        
    
        C++ signature :
            int UFFOptimizeMolecule(class RDKit::ROMol {lvalue} [,int=200 [,double=10.0 [,int=-1 [,bool=True]]]])
    """
def UFFOptimizeMoleculeConfs(self: Mol, numThreads: int = 1, maxIters: int = 200, vdwThresh: float = 10.0, ignoreInterfragInteractions: bool = True) -> typing.Any:
    """
        uses UFF to optimize all of a molecule's conformations
        
         
         ARGUMENTS:
        
            - mol : the molecule of interest
            - numThreads : the number of threads to use, only has an effect if the RDKit
                           was built with thread support (defaults to 1)
                           If set to zero, the max supported by the system will be used.
            - maxIters : the maximum number of iterations (defaults to 200)
            - vdwThresh : used to exclude long-range van der Waals interactions
                          (defaults to 10.0)
            - ignoreInterfragInteractions : if true, nonbonded terms between
                          fragments will not be added to the forcefield.
        
         RETURNS: a list of (not_converged, energy) 2-tuples. 
             If not_converged is 0 the optimization converged for that conformer.
        
        
    
        C++ signature :
            class boost::python::api::object UFFOptimizeMoleculeConfs(class RDKit::ROMol {lvalue} [,int=1 [,int=200 [,double=10.0 [,bool=True]]]])
    """

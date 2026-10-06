"""
Module containing functions to perform 3D operations like rotate and translate conformations
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CanonicalizeConformer', 'CanonicalizeMol', 'ComputeCanonicalTransform', 'ComputeCentroid', 'ComputePrincipalAxesAndMoments', 'ComputePrincipalAxesAndMomentsFromGyrationMatrix', 'GetAngleDeg', 'GetAngleRad', 'GetBondLength', 'GetDihedralDeg', 'GetDihedralRad', 'SetAngleDeg', 'SetAngleRad', 'SetBondLength', 'SetDihedralDeg', 'SetDihedralRad', 'TransformConformer']
def CanonicalizeConformer(conf: Conformer, center: Point3D = None, normalizeCovar: bool = False, ignoreHs: bool = True) -> None:
    """
        Canonicalize the orientation of a conformer so that its principal axes
                       around the specified center point coincide with the x, y, z axes
          
          ARGUMENTS:
            - conf : conformer of interest 
            - center : optionally center point about which the principal axes are computed 
                                  if not specified the centroid of the conformer will be used
            - normalizeCovar : Optionally normalize the covariance matrix by the number of atoms
        
    
        C++ signature :
            void CanonicalizeConformer(class RDKit::Conformer {lvalue} [,class RDGeom::Point3D const * __ptr64=None [,bool=False [,bool=True]]])
    """
def CanonicalizeMol(mol: Mol, normalizeCovar: bool = False, ignoreHs: bool = True) -> None:
    """
        Loop over the conformers in a molecule and canonicalize their orientation
    
        C++ signature :
            void CanonicalizeMol(class RDKit::ROMol {lvalue} [,bool=False [,bool=True]])
    """
def ComputeCanonicalTransform(conf: Conformer, center: Point3D = None, normalizeCovar: bool = False, ignoreHs: bool = True) -> typing.Any:
    """
        Compute the transformation required aligna conformer so that
                       the principal axes align up with the x,y, z axes
                       The conformer itself is left unchanged
          ARGUMENTS:
            - conf : the conformer of interest
            - center : optional center point to compute the principal axes around (defaults to the centroid)
            - normalizeCovar : optionally normalize the covariance matrix by the number of atoms
        
    
        C++ signature :
            struct _object * __ptr64 ComputeCanonicalTransform(class RDKit::Conformer [,class RDGeom::Point3D const * __ptr64=None [,bool=False [,bool=True]]])
    """
def ComputeCentroid(conf: Conformer, ignoreHs: bool = True, weights: _vectdouble = None) -> Point3D:
    """
        Compute the centroid of the conformation - hydrogens are ignored and no attention
                                   is paid to the difference in sizes of the heavy atoms; however,
                                   an optional vector of weights can be passed.
        
    
        C++ signature :
            class RDGeom::Point3D ComputeCentroid(class RDKit::Conformer [,bool=True [,class std::vector<double,class std::allocator<double> > const * __ptr64=None]])
    """
def ComputePrincipalAxesAndMoments(conf: Conformer, ignoreHs: bool = True, weights: typing.Any = None) -> typing.Any:
    """
        Compute principal axes and moments of inertia for a conformer
               These values are calculated from the inertia tensor:
               Iij = - sum_{s=1..N}(w_s * r_{si} * r_{sj}) i != j
               Iii = sum_{s=1..N} sum_{j!=i} (w_s * r_{sj} * r_{sj})
               where the coordinates are relative to the center of mass.
        
          ARGUMENTS:
            - conf : the conformer of interest
            - ignoreHs : if True, ignore hydrogen atoms
            - weights : if present, used to weight the atomic coordinates
        
          Returns a (principal axes, principal moments) tuple
        
    
        C++ signature :
            struct _object * __ptr64 ComputePrincipalAxesAndMoments(class RDKit::Conformer [,bool=True [,class boost::python::api::object=None]])
    """
def ComputePrincipalAxesAndMomentsFromGyrationMatrix(conf: Conformer, ignoreHs: bool = True, weights: typing.Any = None) -> typing.Any:
    """
        Compute principal axes and moments from the gyration matrix of a conformer
               These values are calculated from the gyration matrix/tensor:
               Iij = sum_{s=1..N}(w_s * r_{si} * r_{sj}) i != j
               Iii = sum_{s=1..N} sum_{t!=s}(w_s * r_{si} * r_{ti})
               where the coordinates are relative to the center of mass.
        
          ARGUMENTS:
            - conf : the conformer of interest
            - ignoreHs : if True, ignore hydrogen atoms
            - weights : if present, used to weight the atomic coordinates
        
          Returns a (principal axes, principal moments) tuple
        
    
        C++ signature :
            struct _object * __ptr64 ComputePrincipalAxesAndMomentsFromGyrationMatrix(class RDKit::Conformer [,bool=True [,class boost::python::api::object=None]])
    """
def GetAngleDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int) -> float:
    """
        Returns the angle in degrees between atoms i, j, k
        
    
        C++ signature :
            double GetAngleDeg(class RDKit::Conformer,unsigned int,unsigned int,unsigned int)
    """
def GetAngleRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int) -> float:
    """
        Returns the angle in radians between atoms i, j, k
        
    
        C++ signature :
            double GetAngleRad(class RDKit::Conformer,unsigned int,unsigned int,unsigned int)
    """
def GetBondLength(conf: Conformer, iAtomId: int, jAtomId: int) -> float:
    """
        Returns the bond length in angstrom between atoms i, j
        
    
        C++ signature :
            double GetBondLength(class RDKit::Conformer,unsigned int,unsigned int)
    """
def GetDihedralDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int) -> float:
    """
        Returns the dihedral angle in degrees between atoms i, j, k, l
        
    
        C++ signature :
            double GetDihedralDeg(class RDKit::Conformer,unsigned int,unsigned int,unsigned int,unsigned int)
    """
def GetDihedralRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int) -> float:
    """
        Returns the dihedral angle in radians between atoms i, j, k, l
        
    
        C++ signature :
            double GetDihedralRad(class RDKit::Conformer,unsigned int,unsigned int,unsigned int,unsigned int)
    """
def SetAngleDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, value: float) -> None:
    """
        Sets the angle in degrees between atoms i, j, k; all atoms bonded to atom k are moved
        
    
        C++ signature :
            void SetAngleDeg(class RDKit::Conformer {lvalue},unsigned int,unsigned int,unsigned int,double)
    """
def SetAngleRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, value: float) -> None:
    """
        Sets the angle in radians between atoms i, j, k; all atoms bonded to atom k are moved
        
    
        C++ signature :
            void SetAngleRad(class RDKit::Conformer {lvalue},unsigned int,unsigned int,unsigned int,double)
    """
def SetBondLength(conf: Conformer, iAtomId: int, jAtomId: int, value: float) -> None:
    """
        Sets the bond length in angstrom between atoms i, j; all atoms bonded to atom j are moved
        
    
        C++ signature :
            void SetBondLength(class RDKit::Conformer {lvalue},unsigned int,unsigned int,double)
    """
def SetDihedralDeg(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int, value: float) -> None:
    """
        Sets the dihedral angle in degrees between atoms i, j, k, l; all atoms bonded to atom l are moved
        
    
        C++ signature :
            void SetDihedralDeg(class RDKit::Conformer {lvalue},unsigned int,unsigned int,unsigned int,unsigned int,double)
    """
def SetDihedralRad(conf: Conformer, iAtomId: int, jAtomId: int, kAtomId: int, lAtomId: int, value: float) -> None:
    """
        Sets the dihedral angle in radians between atoms i, j, k, l; all atoms bonded to atom l are moved
        
    
        C++ signature :
            void SetDihedralRad(class RDKit::Conformer {lvalue},unsigned int,unsigned int,unsigned int,unsigned int,double)
    """
def TransformConformer(conf: Conformer, trans: typing.Any) -> None:
    """
        Transform the coordinates of a conformer
    
        C++ signature :
            void TransformConformer(class RDKit::Conformer {lvalue},class boost::python::api::object)
    """

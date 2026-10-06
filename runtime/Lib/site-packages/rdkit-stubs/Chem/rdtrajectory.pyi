"""
Module containing Trajectory and Snapshot objects
"""
from __future__ import annotations
import typing
__all__: list[str] = ['ReadAmberTrajectory', 'ReadGromosTrajectory', 'Snapshot', 'Trajectory']
class Snapshot(Boost.Python.instance):
    """
    A class which allows storing coordinates from a trajectory
    """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetEnergy(self) -> float:
        """
            returns the energy for this Snapshot
        
            C++ signature :
                double GetEnergy(class RDKit::Snapshot {lvalue})
        """
    def GetPoint2D(self, pointNum: int) -> Point2D:
        """
            return the coordinates at pointNum as a Point2D object; requires the Trajectory dimension to be == 2
        
            C++ signature :
                class RDGeom::Point2D GetPoint2D(class RDKit::Snapshot {lvalue},unsigned int)
        """
    def GetPoint3D(self, pointNum: int) -> Point3D:
        """
            return the coordinates at pointNum as a Point3D object; requires the Trajectory dimension to be >= 2
        
            C++ signature :
                class RDGeom::Point3D GetPoint3D(class RDKit::Snapshot {lvalue},unsigned int)
        """
    def SetEnergy(self, energy: float) -> None:
        """
            sets the energy for this Snapshot
        
            C++ signature :
                void SetEnergy(class RDKit::Snapshot {lvalue},double)
        """
    @typing.overload
    def __init__(self, coordList: list, energy: float = 0.0) -> typing.Any:
        """
            Constructor;
            coordList: list of floats containing the coordinates for this Snapshot;
            energy:    the energy for this Snapshot.
            
        
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,class boost::python::list {lvalue} [,double=0.0])
        """
    @typing.overload
    def __init__(self, other: Snapshot) -> typing.Any:
        """
            Copy constructor
        
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,class RDKit::Snapshot * __ptr64)
        """
class Trajectory(Boost.Python.instance):
    """
    A class which allows storing Snapshots from a trajectory
    """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AddConformersToMol(self, mol: Mol, fromCid: int = -1, toCid: int = -1) -> int:
        """
            adds conformations from the Trajectory to mol
            fromCid is the first Snapshot that will be added as a Conformer; defaults to -1 (first available)
            toCid is the last Snapshot that will be added as a Conformer; defaults to -1 (all)
            
        
            C++ signature :
                unsigned int AddConformersToMol(class RDKit::Trajectory {lvalue},class RDKit::ROMol {lvalue} [,int=-1 [,int=-1]])
        """
    def AddSnapshot(self, s: Snapshot) -> int:
        """
            appends Snapshot s to this Trajectory; returns the zero-based index position of the added snapshot
            
        
            C++ signature :
                unsigned int AddSnapshot(class RDKit::Trajectory {lvalue},class RDKit::Snapshot)
        """
    def Clear(self) -> None:
        """
            removes all Snapshots from the Trajectory
            
        
            C++ signature :
                void Clear(class RDKit::Trajectory {lvalue})
        """
    def Dimension(self) -> int:
        """
            returns the dimensionality of this Trajectory's coordinate tuples
        
            C++ signature :
                unsigned int Dimension(class RDKit::Trajectory {lvalue})
        """
    def GetSnapshot(self, snapshotNum: int) -> Snapshot:
        """
            returns the Snapshot snapshotNum, where the latter is the zero-based index of the retrieved Snapshot
            
        
            C++ signature :
                class RDKit::Snapshot * __ptr64 GetSnapshot(class RDKit::Trajectory * __ptr64,unsigned int)
        """
    def InsertSnapshot(self, snapshotNum: int, s: Snapshot) -> int:
        """
            inserts Snapshot s into the Trajectory at the position snapshotNum, where the latter is the zero-based index of the Trajectory's Snapshot before which the Snapshot s will be inserted; returns the zero-based index position of the inserted snapshot
            
        
            C++ signature :
                unsigned int InsertSnapshot(class RDKit::Trajectory {lvalue},unsigned int,class RDKit::Snapshot)
        """
    def NumPoints(self) -> int:
        """
            returns the number of coordinate tuples associated to each Snapshot
        
            C++ signature :
                unsigned int NumPoints(class RDKit::Trajectory {lvalue})
        """
    def RemoveSnapshot(self, snapshotNum: int) -> int:
        """
            removes Snapshot snapshotNum from the Trajectory, where snapshotNum is the zero-based index of Snapshot to be removed
            
        
            C++ signature :
                unsigned int RemoveSnapshot(class RDKit::Trajectory {lvalue},unsigned int)
        """
    @typing.overload
    def __init__(self, dimension: int, numPoints: int, snapshotList: list = []) -> typing.Any:
        """
            Constructor;
            dimension:    dimensionality of this Trajectory's coordinate tuples;
            numPoints:    number of coordinate tuples associated to each Snapshot;
            snapshotList: list of Snapshot objects used to initialize the Trajectory (optional; defaults to []).
            
        
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,unsigned int,unsigned int [,class boost::python::list=[]])
        """
    @typing.overload
    def __init__(self, other: Trajectory) -> typing.Any:
        """
            Copy constructor
        
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,class RDKit::Trajectory * __ptr64)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned __int64 __len__(class RDKit::Trajectory {lvalue})
        """
def ReadAmberTrajectory(fName: str, traj: Trajectory) -> int:
    """
        reads coordinates from an AMBER trajectory file into the Trajectory object; returns the number of Snapshot objects read in
        
    
        C++ signature :
            unsigned int ReadAmberTrajectory(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class RDKit::Trajectory {lvalue})
    """
def ReadGromosTrajectory(fName: str, traj: Trajectory) -> int:
    """
        reads coordinates from a GROMOS trajectory file into the Trajectory object; returns the number of Snapshot objects read in
        
    
        C++ signature :
            unsigned int ReadGromosTrajectory(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class RDKit::Trajectory {lvalue})
    """

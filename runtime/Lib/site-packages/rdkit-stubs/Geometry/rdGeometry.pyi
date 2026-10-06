"""
Module containing geometry objects like points, grids, etc
"""
from __future__ import annotations
import typing
__all__: list[str] = ['ComputeDihedralAngle', 'ComputeGridCentroid', 'ComputeSignedDihedralAngle', 'FindGridTerminalPoints', 'Point2D', 'Point3D', 'PointND', 'ProtrudeDistance', 'TanimotoDistance', 'TverskyIndex', 'UniformGrid3D', 'UniformGrid3D_', 'UniformRealValueGrid3D', 'WriteGridToFile']
class Point2D(Boost.Python.instance):
    """
    A class to represent a two-dimensional point
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 48
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AngleTo(self, other: Point2D) -> float:
        """
            determines the angle between a vector to this point (between 0 and PI)
        
            C++ signature :
                double AngleTo(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def DirectionVector(self, other: Point2D) -> Point2D:
        """
            return a normalized direction vector from this point to another
        
            C++ signature :
                class RDGeom::Point2D DirectionVector(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def DotProduct(self, other: Point2D) -> float:
        """
            Dot product with another point
        
            C++ signature :
                double DotProduct(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def Length(self) -> float:
        """
            Length of the vector
        
            C++ signature :
                double Length(class RDGeom::Point2D {lvalue})
        """
    def LengthSq(self) -> float:
        """
            Square of the length
        
            C++ signature :
                double LengthSq(class RDGeom::Point2D {lvalue})
        """
    def Normalize(self) -> None:
        """
            Normalize the vector (using L2 norm)
        
            C++ signature :
                void Normalize(class RDGeom::Point2D {lvalue})
        """
    def SignedAngleTo(self, other: Point2D) -> float:
        """
            determines the signed angle between a vector to this point (between 0 and 2*PI)
        
            C++ signature :
                double SignedAngleTo(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def __add__(self, other: Point2D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDGeom::Point2D)
        """
    def __getitem__(self, idx: int) -> float:
        """
            C++ signature :
                double __getitem__(class RDGeom::Point2D,int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: Point2D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDGeom::Point2D & __ptr64>,class RDGeom::Point2D)
        """
    def __idiv__(self, scale: float) -> Point2D:
        """
            Scalar division
        
            C++ signature :
                class RDGeom::Point2D {lvalue} __idiv__(class RDGeom::Point2D {lvalue},double)
        """
    def __imul__(self, scale: float) -> Point2D:
        """
            Scalar multiplication
        
            C++ signature :
                class RDGeom::Point2D {lvalue} __imul__(class RDGeom::Point2D {lvalue},double)
        """
    @typing.overload
    def __init__(self) -> None:
        """
            Default Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @typing.overload
    def __init__(self, xv: float, yv: float) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,double,double)
        """
    @typing.overload
    def __init__(self, other: Point3D) -> None:
        """
            construct from a Point3D (ignoring the z component)
        
            C++ signature :
                void __init__(struct _object * __ptr64,class RDGeom::Point3D)
        """
    def __isub__(self, other: Point2D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDGeom::Point2D & __ptr64>,class RDGeom::Point2D)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class RDGeom::Point2D {lvalue})
        """
    def __mul__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __mul__(class RDGeom::Point2D {lvalue},double)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: Point2D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDGeom::Point2D {lvalue},class RDGeom::Point2D)
        """
    def __truediv__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __truediv__(class RDGeom::Point2D {lvalue},double)
        """
    @property
    def x(*args, **kwargs):
        ...
    @x.setter
    def x(*args, **kwargs):
        ...
    @property
    def y(*args, **kwargs):
        ...
    @y.setter
    def y(*args, **kwargs):
        ...
class Point3D(Boost.Python.instance):
    """
    A class to represent a three-dimensional point
    The x, y, and z coordinates can be read and written using either attributes
    (i.e. pt.x = 4) or indexing (i.e. pt[0] = 4).
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 56
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AngleTo(self, other: Point3D) -> float:
        """
            determines the angle between a vector to this point (between 0 and PI)
        
            C++ signature :
                double AngleTo(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def CrossProduct(self, other: Point3D) -> Point3D:
        """
            Get the cross product between two points
        
            C++ signature :
                class RDGeom::Point3D CrossProduct(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def DirectionVector(self, other: Point3D) -> Point3D:
        """
            return a normalized direction vector from this point to another
        
            C++ signature :
                class RDGeom::Point3D DirectionVector(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def Distance(self, pt2: Point3D) -> float:
        """
            Distance from this point to another point
        
            C++ signature :
                double Distance(class RDGeom::Point3D,class RDGeom::Point3D)
        """
    def DotProduct(self, other: Point3D) -> float:
        """
            Dot product with another point
        
            C++ signature :
                double DotProduct(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def Length(self) -> float:
        """
            Length of the vector
        
            C++ signature :
                double Length(class RDGeom::Point3D {lvalue})
        """
    def LengthSq(self) -> float:
        """
            Square of the length
        
            C++ signature :
                double LengthSq(class RDGeom::Point3D {lvalue})
        """
    def Normalize(self) -> None:
        """
            Normalize the vector (using L2 norm)
        
            C++ signature :
                void Normalize(class RDGeom::Point3D {lvalue})
        """
    def SignedAngleTo(self, other: Point3D) -> float:
        """
            determines the signed angle between a vector to this point (between 0 and 2*PI)
        
            C++ signature :
                double SignedAngleTo(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def __add__(self, other: Point3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDGeom::Point3D)
        """
    def __getitem__(self, idx: int) -> float:
        """
            C++ signature :
                double __getitem__(class RDGeom::Point3D,int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __iadd__(self, other: Point3D) -> Point3D:
        """
            Addition to another point
        
            C++ signature :
                class RDGeom::Point3D {lvalue} __iadd__(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    @typing.overload
    def __iadd__(self, other: Point3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDGeom::Point3D & __ptr64>,class RDGeom::Point3D)
        """
    def __idiv__(self, scale: float) -> Point3D:
        """
            Scalar division
        
            C++ signature :
                class RDGeom::Point3D {lvalue} __idiv__(class RDGeom::Point3D {lvalue},double)
        """
    def __imul__(self, scale: float) -> Point3D:
        """
            Scalar multiplication
        
            C++ signature :
                class RDGeom::Point3D {lvalue} __imul__(class RDGeom::Point3D {lvalue},double)
        """
    @typing.overload
    def __init__(self) -> None:
        """
            Default Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @typing.overload
    def __init__(self, xv: float, yv: float, zv: float) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,double,double,double)
        """
    @typing.overload
    def __isub__(self, other: Point3D) -> Point3D:
        """
            Vector difference
        
            C++ signature :
                class RDGeom::Point3D {lvalue} __isub__(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    @typing.overload
    def __isub__(self, other: Point3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDGeom::Point3D & __ptr64>,class RDGeom::Point3D)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class RDGeom::Point3D {lvalue})
        """
    def __mul__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __mul__(class RDGeom::Point3D {lvalue},double)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: Point3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDGeom::Point3D {lvalue},class RDGeom::Point3D)
        """
    def __truediv__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __truediv__(class RDGeom::Point3D {lvalue},double)
        """
    @property
    def x(*args, **kwargs):
        ...
    @x.setter
    def x(*args, **kwargs):
        ...
    @property
    def y(*args, **kwargs):
        ...
    @y.setter
    def y(*args, **kwargs):
        ...
    @property
    def z(*args, **kwargs):
        ...
    @z.setter
    def z(*args, **kwargs):
        ...
class PointND(Boost.Python.instance):
    """
    A class to represent an N-dimensional point
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 48
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AngleTo(self, other: PointND) -> float:
        """
            determines the angle between a vector to this point (between 0 and PI)
        
            C++ signature :
                double AngleTo(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    def DirectionVector(self, other: PointND) -> PointND:
        """
            return a normalized direction vector from this point to another
        
            C++ signature :
                class RDGeom::PointND DirectionVector(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    def Distance(self: Point3D, pt2: Point3D) -> float:
        """
            Distance from this point to another point
        
            C++ signature :
                double Distance(class RDGeom::Point3D,class RDGeom::Point3D)
        """
    def DotProduct(self, other: PointND) -> float:
        """
            Dot product with another point
        
            C++ signature :
                double DotProduct(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    def Length(self) -> float:
        """
            Length of the vector
        
            C++ signature :
                double Length(class RDGeom::PointND {lvalue})
        """
    def LengthSq(self) -> float:
        """
            Square of the length
        
            C++ signature :
                double LengthSq(class RDGeom::PointND {lvalue})
        """
    def Normalize(self) -> None:
        """
            Normalize the vector (using L2 norm)
        
            C++ signature :
                void Normalize(class RDGeom::PointND {lvalue})
        """
    def __add__(self, other: PointND) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDGeom::PointND)
        """
    def __getitem__(self, idx: int) -> float:
        """
            C++ signature :
                double __getitem__(class RDGeom::PointND,int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class RDGeom::PointND)
        """
    @typing.overload
    def __iadd__(self, other: PointND) -> PointND:
        """
            Addition to another point
        
            C++ signature :
                class RDGeom::PointND {lvalue} __iadd__(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    @typing.overload
    def __iadd__(self, other: PointND) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDGeom::PointND & __ptr64>,class RDGeom::PointND)
        """
    def __idiv__(self, scale: float) -> PointND:
        """
            Scalar division
        
            C++ signature :
                class RDGeom::PointND {lvalue} __idiv__(class RDGeom::PointND {lvalue},double)
        """
    def __imul__(self, scale: float) -> PointND:
        """
            Scalar multiplication
        
            C++ signature :
                class RDGeom::PointND {lvalue} __imul__(class RDGeom::PointND {lvalue},double)
        """
    def __init__(self, dim: int) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int)
        """
    @typing.overload
    def __isub__(self, other: PointND) -> PointND:
        """
            Vector difference
        
            C++ signature :
                class RDGeom::PointND {lvalue} __isub__(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    @typing.overload
    def __isub__(self, other: PointND) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDGeom::PointND & __ptr64>,class RDGeom::PointND)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class RDGeom::PointND {lvalue})
        """
    def __mul__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __mul__(class RDGeom::PointND {lvalue},double)
        """
    def __setitem__(self, idx: int, val: float) -> float:
        """
            C++ signature :
                double __setitem__(class RDGeom::PointND {lvalue},int,double)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class RDGeom::PointND {lvalue},class boost::python::tuple)
        """
    def __sub__(self, other: PointND) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDGeom::PointND {lvalue},class RDGeom::PointND)
        """
    def __truediv__(self, other: float) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __truediv__(class RDGeom::PointND {lvalue},double)
        """
class UniformGrid3D_(Boost.Python.instance):
    """
    Class to represent a uniform three-dimensional
        cubic grid. Each grid point can store a poisitive integer value. For the sake
        of efficiency these value can either be binary, fit in 2, 4, 8 or 16 bits
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 96
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def CompareParams(self, other: UniformGrid3D_) -> bool:
        """
            Compare the parameters between two grid object
        
            C++ signature :
                bool CompareParams(class RDGeom::UniformGrid3D {lvalue},class RDGeom::UniformGrid3D)
        """
    def GetGridIndex(self, xi: int, yi: int, zi: int) -> int:
        """
            Get the index to the grid point with the three integer indices provided
        
            C++ signature :
                int GetGridIndex(class RDGeom::UniformGrid3D {lvalue},unsigned int,unsigned int,unsigned int)
        """
    def GetGridIndices(self, idx: int) -> tuple:
        """
            Returns the integer indices of the grid index provided.
        
            C++ signature :
                class boost::python::tuple GetGridIndices(class RDGeom::UniformGrid3D,unsigned int)
        """
    def GetGridPointIndex(self, point: Point3D) -> int:
        """
            Get the index to the grid point closest to the specified point
        
            C++ signature :
                int GetGridPointIndex(class RDGeom::UniformGrid3D {lvalue},class RDGeom::Point3D)
        """
    def GetGridPointLoc(self, pointId: int) -> Point3D:
        """
            Get the location of the specified grid point
        
            C++ signature :
                class RDGeom::Point3D GetGridPointLoc(class RDGeom::UniformGrid3D {lvalue},unsigned int)
        """
    def GetNumX(self) -> int:
        """
            Get the number of grid points along x-axis
        
            C++ signature :
                unsigned int GetNumX(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetNumY(self) -> int:
        """
            Get the number of grid points along y-axis
        
            C++ signature :
                unsigned int GetNumY(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetNumZ(self) -> int:
        """
            Get the number of grid points along z-axis
        
            C++ signature :
                unsigned int GetNumZ(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetOccupancyVect(self) -> DiscreteValueVect:
        """
            Get the occupancy vector for the grid
        
            C++ signature :
                class RDKit::DiscreteValueVect const * __ptr64 GetOccupancyVect(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetOffset(self) -> Point3D:
        """
            Get the location of the center of the grid
        
            C++ signature :
                class RDGeom::Point3D GetOffset(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetSize(self) -> int:
        """
            Get the size of the grid (number of grid points)
        
            C++ signature :
                unsigned int GetSize(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetSpacing(self) -> float:
        """
            Get the grid spacing
        
            C++ signature :
                double GetSpacing(class RDGeom::UniformGrid3D {lvalue})
        """
    def GetVal(self, id: int) -> int:
        """
            Get the value at the specified grid point
        
            C++ signature :
                int GetVal(class RDGeom::UniformGrid3D,unsigned int)
        """
    def GetValPoint(self, pt: Point3D) -> int:
        """
            Get the value at the closest grid point
        
            C++ signature :
                int GetValPoint(class RDGeom::UniformGrid3D,class RDGeom::Point3D)
        """
    def SetSphereOccupancy(self, center: Point3D, radius: float, stepSize: float, maxLayers: int = -1, ignoreOutOfBound: bool = True) -> None:
        """
            Set the occupancy on the grid for a sphere or specified radius
             and multiple layers around this sphere, with decreasing values of 
            occupancy
            
        
            C++ signature :
                void SetSphereOccupancy(class RDGeom::UniformGrid3D {lvalue},class RDGeom::Point3D,double,double [,int=-1 [,bool=True]])
        """
    def SetVal(self, id: int, val: int) -> None:
        """
            Set the value at the specified grid point
        
            C++ signature :
                void SetVal(class RDGeom::UniformGrid3D {lvalue},unsigned int,unsigned int)
        """
    def SetValPoint(self, pt: Point3D, val: int) -> None:
        """
            Set the value at grid point closest to the specified point
        
            C++ signature :
                void SetValPoint(class RDGeom::UniformGrid3D {lvalue},class RDGeom::Point3D,unsigned int)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDGeom::UniformGrid3D)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: UniformGrid3D_) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDGeom::UniformGrid3D & __ptr64>,class RDGeom::UniformGrid3D)
        """
    def __iand__(self, other: UniformGrid3D_) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iand__(struct boost::python::back_reference<class RDGeom::UniformGrid3D & __ptr64>,class RDGeom::UniformGrid3D)
        """
    def __init__(self, pkl: str) -> None:
        """
            pickle constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def __ior__(self, other: UniformGrid3D_) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ior__(struct boost::python::back_reference<class RDGeom::UniformGrid3D & __ptr64>,class RDGeom::UniformGrid3D)
        """
    def __isub__(self, other: UniformGrid3D_) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDGeom::UniformGrid3D & __ptr64>,class RDGeom::UniformGrid3D)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
class UniformRealValueGrid3D(Boost.Python.instance):
    """
    Class to represent a uniform three-dimensional
        cubic grid. Each grid point can store a floating point value. 
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 120
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def CompareGrids(arg1: UniformRealValueGrid3D, arg2: UniformRealValueGrid3D) -> bool:
        """
            Compare the parameters and values between two grid objects.
        
            C++ signature :
                bool CompareGrids(class RDGeom::UniformRealValueGrid3D {lvalue},class RDGeom::UniformRealValueGrid3D)
        """
    @staticmethod
    def CompareParams(arg1: UniformRealValueGrid3D, arg2: UniformRealValueGrid3D) -> bool:
        """
            Compare the parameters between two grid object.
        
            C++ signature :
                bool CompareParams(class RDGeom::UniformRealValueGrid3D {lvalue},class RDGeom::UniformRealValueGrid3D)
        """
    @staticmethod
    def CompareVectors(arg1: UniformRealValueGrid3D, arg2: UniformRealValueGrid3D) -> bool:
        """
            Compare the vector values between two grid objects.
        
            C++ signature :
                bool CompareVectors(class RDGeom::UniformRealValueGrid3D {lvalue},class RDGeom::UniformRealValueGrid3D)
        """
    @staticmethod
    def GetGridIndex(arg1: UniformRealValueGrid3D, arg2: int, arg3: int, arg4: int) -> int:
        """
            Get the index to the grid point with the three integer indices provided
        
            C++ signature :
                int GetGridIndex(class RDGeom::UniformRealValueGrid3D {lvalue},unsigned int,unsigned int,unsigned int)
        """
    @staticmethod
    def GetGridIndices(arg1: UniformRealValueGrid3D, arg2: int) -> tuple:
        """
            Returns the integer indices of the grid index provided.
        
            C++ signature :
                class boost::python::tuple GetGridIndices(class RDGeom::UniformRealValueGrid3D,unsigned int)
        """
    @staticmethod
    def GetGridPointIndex(arg1: UniformRealValueGrid3D, arg2: Point3D) -> int:
        """
            Get the index to the grid point closest to the specified point
        
            C++ signature :
                int GetGridPointIndex(class RDGeom::UniformRealValueGrid3D {lvalue},class RDGeom::Point3D)
        """
    @staticmethod
    def GetGridPointLoc(arg1: UniformRealValueGrid3D, arg2: int) -> Point3D:
        """
            Get the location of the specified grid point
        
            C++ signature :
                class RDGeom::Point3D GetGridPointLoc(class RDGeom::UniformRealValueGrid3D {lvalue},unsigned int)
        """
    @staticmethod
    def GetNumX(arg1: UniformRealValueGrid3D) -> int:
        """
            Get the number of grid points along x-axis
        
            C++ signature :
                unsigned int GetNumX(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetNumY(arg1: UniformRealValueGrid3D) -> int:
        """
            Get the number of grid points along y-axis
        
            C++ signature :
                unsigned int GetNumY(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetNumZ(arg1: UniformRealValueGrid3D) -> int:
        """
            Get the number of grid points along z-axis
        
            C++ signature :
                unsigned int GetNumZ(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetOccupancyVect(arg1: UniformRealValueGrid3D) -> RealValueVect:
        """
            Get the occupancy vector for the grid
        
            C++ signature :
                class RDKit::RealValueVect const * __ptr64 GetOccupancyVect(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetOffset(arg1: UniformRealValueGrid3D) -> Point3D:
        """
            Get the location of the center of the grid
        
            C++ signature :
                class RDGeom::Point3D GetOffset(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetSize(arg1: UniformRealValueGrid3D) -> int:
        """
            Get the size of the grid (number of grid points)
        
            C++ signature :
                unsigned int GetSize(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetSpacing(arg1: UniformRealValueGrid3D) -> float:
        """
            Get the grid spacing
        
            C++ signature :
                double GetSpacing(class RDGeom::UniformRealValueGrid3D {lvalue})
        """
    @staticmethod
    def GetVal(arg1: UniformRealValueGrid3D, arg2: int) -> float:
        """
            Get the value at the specified grid point
        
            C++ signature :
                double GetVal(class RDGeom::UniformRealValueGrid3D,unsigned int)
        """
    @staticmethod
    def GetValPoint(arg1: UniformRealValueGrid3D, arg2: Point3D) -> float:
        """
            Get the value at the closest grid point
        
            C++ signature :
                double GetValPoint(class RDGeom::UniformRealValueGrid3D,class RDGeom::Point3D)
        """
    @staticmethod
    def SetVal(arg1: UniformRealValueGrid3D, arg2: int, arg3: float) -> None:
        """
            Set the value at the specified grid point
        
            C++ signature :
                void SetVal(class RDGeom::UniformRealValueGrid3D {lvalue},unsigned int,double)
        """
    @staticmethod
    def SetValPoint(arg1: UniformRealValueGrid3D, arg2: Point3D, arg3: float) -> None:
        """
            Set the value at grid point closest to the specified point
        
            C++ signature :
                void SetValPoint(class RDGeom::UniformRealValueGrid3D {lvalue},class RDGeom::Point3D,double)
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDGeom::UniformRealValueGrid3D)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: UniformRealValueGrid3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDGeom::UniformRealValueGrid3D & __ptr64>,class RDGeom::UniformRealValueGrid3D)
        """
    def __iand__(self, other: UniformRealValueGrid3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iand__(struct boost::python::back_reference<class RDGeom::UniformRealValueGrid3D & __ptr64>,class RDGeom::UniformRealValueGrid3D)
        """
    @typing.overload
    def __init__(self, arg1: str) -> None:
        """
            Pickle constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __init__(self) -> None:
        """
            Default constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @typing.overload
    def __init__(self, arg1: UniformRealValueGrid3D) -> None:
        """
            Copy constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,class RDGeom::UniformRealValueGrid3D)
        """
    @typing.overload
    def __init__(self, dimX: float, dimY: float, dimZ: float, spacing: float = 0.5, offSet: Point3D = None) -> typing.Any:
        """
            Constructor
        
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,double,double,double [,double=0.5 [,class RDGeom::Point3D const * __ptr64=None]])
        """
    def __ior__(self, other: UniformRealValueGrid3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ior__(struct boost::python::back_reference<class RDGeom::UniformRealValueGrid3D & __ptr64>,class RDGeom::UniformRealValueGrid3D)
        """
    def __isub__(self, other: UniformRealValueGrid3D) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDGeom::UniformRealValueGrid3D & __ptr64>,class RDGeom::UniformRealValueGrid3D)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
def ComputeDihedralAngle(pt1: Point3D, pt2: Point3D, pt3: Point3D, pt4: Point3D) -> float:
    """
        calculates the dihedral angle determined by four Point3D objects
    
        C++ signature :
            double ComputeDihedralAngle(class RDGeom::Point3D,class RDGeom::Point3D,class RDGeom::Point3D,class RDGeom::Point3D)
    """
def ComputeGridCentroid(grid: UniformGrid3D_, pt: Point3D, windowRadius: float) -> tuple:
    """
        Compute the grid point at the center of sphere around a Point3D
    
        C++ signature :
            class boost::python::tuple ComputeGridCentroid(class RDGeom::UniformGrid3D,class RDGeom::Point3D,double)
    """
def ComputeSignedDihedralAngle(pt1: Point3D, pt2: Point3D, pt3: Point3D, pt4: Point3D) -> float:
    """
        calculates the signed dihedral angle determined by four Point3D objects
    
        C++ signature :
            double ComputeSignedDihedralAngle(class RDGeom::Point3D,class RDGeom::Point3D,class RDGeom::Point3D,class RDGeom::Point3D)
    """
def FindGridTerminalPoints(grid: UniformGrid3D_, windowRadius: float, inclusionFraction: float) -> tuple:
    """
        Find a grid's terminal points (defined in the subshape algorithm).
    
        C++ signature :
            class boost::python::tuple FindGridTerminalPoints(class RDGeom::UniformGrid3D,double,double)
    """
def ProtrudeDistance(grid1: UniformGrid3D_, grid2: UniformGrid3D_) -> float:
    """
        Compute the protrude distance between two grid objects
    
        C++ signature :
            double ProtrudeDistance(class RDGeom::UniformGrid3D,class RDGeom::UniformGrid3D)
    """
def TanimotoDistance(grid1: UniformGrid3D_, grid2: UniformGrid3D_) -> float:
    """
        Compute the tanimoto distance between two grid objects
    
        C++ signature :
            double TanimotoDistance(class RDGeom::UniformGrid3D,class RDGeom::UniformGrid3D)
    """
def TverskyIndex(grid1: UniformGrid3D_, grid2: UniformGrid3D_, alpha: float, beta: float) -> float:
    """
        Compute the tversky index between two grid objects
    
        C++ signature :
            double TverskyIndex(class RDGeom::UniformGrid3D,class RDGeom::UniformGrid3D,double,double)
    """
def UniformGrid3D(dimX: float, dimY: float, dimZ: float, spacing: float = 0.5, valType: DiscreteValueType = ..., offSet: Point3D = None) -> UniformGrid3D_:
    """
        Faking the constructor
    
        C++ signature :
            class RDGeom::UniformGrid3D * __ptr64 UniformGrid3D(double,double,double [,double=0.5 [,enum RDKit::DiscreteValueVect::DiscreteValueType=rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE [,class RDGeom::Point3D const * __ptr64=None]]])
    """
def WriteGridToFile(grid: UniformGrid3D_, filename: str) -> None:
    """
        Write the grid to a grid file
    
        C++ signature :
            void WriteGridToFile(class RDGeom::UniformGrid3D,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """

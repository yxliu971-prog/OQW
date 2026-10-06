"""
Module containing the diversity and similarity pickers
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CENTROID', 'CLINK', 'ClusterMethod', 'GOWER', 'HierarchicalClusterPicker', 'LeaderPicker', 'MCQUITTY', 'MaxMinPicker', 'SLINK', 'UPGMA', 'WARD']
class ClusterMethod(Boost.Python.enum):
    CENTROID: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CENTROID
    CLINK: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CLINK
    GOWER: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.GOWER
    MCQUITTY: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.MCQUITTY
    SLINK: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.SLINK
    UPGMA: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.UPGMA
    WARD: typing.ClassVar[ClusterMethod]  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.WARD
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'WARD': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.WARD, 'SLINK': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.SLINK, 'CLINK': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CLINK, 'UPGMA': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.UPGMA, 'MCQUITTY': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.MCQUITTY, 'GOWER': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.GOWER, 'CENTROID': rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CENTROID}
    values: typing.ClassVar[dict]  # value = {1: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.WARD, 2: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.SLINK, 3: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CLINK, 4: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.UPGMA, 5: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.MCQUITTY, 6: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.GOWER, 7: rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CENTROID}
class HierarchicalClusterPicker(Boost.Python.instance):
    """
    A class for diversity picking of items using Hierarchical Clustering
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def Cluster(*args, **kwargs) -> ...:
        """
            Return a list of clusters of item from the pool using hierarchical clustering
            
            ARGUMENTS: 
              - distMat: 1D distance matrix (only the lower triangle elements)
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
            
        
            C++ signature :
                class std::vector<class std::vector<int,class std::allocator<int> >,class std::allocator<class std::vector<int,class std::allocator<int> > > > Cluster(class RDPickers::HierarchicalClusterPicker * __ptr64,class boost::python::api::object {lvalue},int,int)
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def Pick(self, distMat: typing.Any, poolSize: int, pickSize: int) -> _vectint:
        """
            Pick a diverse subset of items from a pool of items using hierarchical clustering
            
            ARGUMENTS: 
              - distMat: 1D distance matrix (only the lower triangle elements)
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > Pick(class RDPickers::HierarchicalClusterPicker * __ptr64,class boost::python::api::object {lvalue},int,int)
        """
    def __init__(self, clusterMethod: ClusterMethod) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,enum RDPickers::HierarchicalClusterPicker::ClusterMethod)
        """
class LeaderPicker(Boost.Python.instance):
    """
    A class for diversity picking of items using Roger Sayle's Leader algorithm (analogous to sphere exclusion). The algorithm is currently unpublished, but a description is available in this presentation from the 2019 RDKit UGM: https://github.com/rdkit/UGM_2019/raw/master/Presentations/Sayle_Clustering.pdf
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def LazyBitVectorPick(self, objects: typing.Any, poolSize: int, threshold: float, pickSize: int = 0, firstPicks: typing.Any = (), numThreads: int = 1) -> _vectint:
        """
            Pick a subset of items from a collection of bit vectors using Tanimoto distance. The threshold value is a *distance* (i.e. 1-similarity). Note that the numThreads argument is currently ignored.
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > LazyBitVectorPick(class RDPickers::LeaderPicker * __ptr64,class boost::python::api::object,int,double [,int=0 [,class boost::python::api::object=() [,int=1]]])
        """
    def LazyPick(self, distFunc: typing.Any, poolSize: int, threshold: float, pickSize: int = 0, firstPicks: typing.Any = (), numThreads: int = 1) -> _vectint:
        """
            Pick a subset of items from a pool of items using the user-provided function to determine distances. Note that the numThreads argument is currently ignored.
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > LazyPick(class RDPickers::LeaderPicker * __ptr64,class boost::python::api::object,int,double [,int=0 [,class boost::python::api::object=() [,int=1]]])
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MaxMinPicker(Boost.Python.instance):
    """
    A class for diversity picking of items using the MaxMin Algorithm
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def LazyBitVectorPick(self, objects: typing.Any, poolSize: int, pickSize: int, firstPicks: typing.Any = (), seed: int = -1, useCache: typing.Any = None) -> _vectint:
        """
            Pick a subset of items from a pool of bit vectors using the MaxMin Algorithm
            Ashton, M. et. al., Quant. Struct.-Act. Relat., 21 (2002), 598-604 
            ARGUMENTS:
            
              - vectors: a sequence of the bit vectors that should be picked from.
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
              - firstPicks: (optional) the first items to be picked (seeds the list)
              - seed: (optional) seed for the random number generator
              - useCache: IGNORED.
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > LazyBitVectorPick(class RDPickers::MaxMinPicker * __ptr64,class boost::python::api::object,int,int [,class boost::python::api::object=() [,int=-1 [,class boost::python::api::object=None]]])
        """
    def LazyBitVectorPickWithThreshold(self, objects: typing.Any, poolSize: int, pickSize: int, threshold: float, firstPicks: typing.Any = (), seed: int = -1) -> tuple:
        """
            Pick a subset of items from a pool of bit vectors using the MaxMin Algorithm
            Ashton, M. et. al., Quant. Struct.-Act. Relat., 21 (2002), 598-604 
            ARGUMENTS:
            
              - vectors: a sequence of the bit vectors that should be picked from.
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
              - threshold: stop picking when the distance goes below this value
              - firstPicks: (optional) the first items to be picked (seeds the list)
              - seed: (optional) seed for the random number generator
            
        
            C++ signature :
                class boost::python::tuple LazyBitVectorPickWithThreshold(class RDPickers::MaxMinPicker * __ptr64,class boost::python::api::object,int,int,double [,class boost::python::api::object=() [,int=-1]])
        """
    def LazyPick(self, distFunc: typing.Any, poolSize: int, pickSize: int, firstPicks: typing.Any = (), seed: int = -1, useCache: typing.Any = None) -> _vectint:
        """
            Pick a subset of items from a pool of items using the MaxMin Algorithm
            Ashton, M. et. al., Quant. Struct.-Act. Relat., 21 (2002), 598-604 
            ARGUMENTS:
            
              - distFunc: a function that should take two indices and return the
                          distance between those two points.
                          NOTE: the implementation caches distance values, so the
                          client code does not need to do so; indeed, it should not.
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
              - firstPicks: (optional) the first items to be picked (seeds the list)
              - seed: (optional) seed for the random number generator
              - useCache: IGNORED
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > LazyPick(class RDPickers::MaxMinPicker * __ptr64,class boost::python::api::object,int,int [,class boost::python::api::object=() [,int=-1 [,class boost::python::api::object=None]]])
        """
    def LazyPickWithThreshold(self, distFunc: typing.Any, poolSize: int, pickSize: int, threshold: float, firstPicks: typing.Any = (), seed: int = -1) -> tuple:
        """
            Pick a subset of items from a pool of items using the MaxMin Algorithm
            Ashton, M. et. al., Quant. Struct.-Act. Relat., 21 (2002), 598-604 
            ARGUMENTS:
            
              - distFunc: a function that should take two indices and return the
                          distance between those two points.
                          NOTE: the implementation caches distance values, so the
                          client code does not need to do so; indeed, it should not.
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
              - threshold: stop picking when the distance goes below this value
              - firstPicks: (optional) the first items to be picked (seeds the list)
              - seed: (optional) seed for the random number generator
            
        
            C++ signature :
                class boost::python::tuple LazyPickWithThreshold(class RDPickers::MaxMinPicker * __ptr64,class boost::python::api::object,int,int,double [,class boost::python::api::object=() [,int=-1]])
        """
    def Pick(self, distMat: typing.Any, poolSize: int, pickSize: int, firstPicks: typing.Any = (), seed: int = -1) -> _vectint:
        """
            Pick a subset of items from a pool of items using the MaxMin Algorithm
            Ashton, M. et. al., Quant. Struct.-Act. Relat., 21 (2002), 598-604 
            
            ARGUMENTS:
              - distMat: 1D distance matrix (only the lower triangle elements)
              - poolSize: number of items in the pool
              - pickSize: number of items to pick from the pool
              - firstPicks: (optional) the first items to be picked (seeds the list)
              - seed: (optional) seed for the random number generator
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > Pick(class RDPickers::MaxMinPicker * __ptr64,class boost::python::api::object,int,int [,class boost::python::api::object=() [,int=-1]])
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
CENTROID: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CENTROID
CLINK: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CLINK
GOWER: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.GOWER
MCQUITTY: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.MCQUITTY
SLINK: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.SLINK
UPGMA: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.UPGMA
WARD: ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.WARD

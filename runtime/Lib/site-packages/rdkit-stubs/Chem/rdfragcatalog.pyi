from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['FragCatGenerator', 'FragCatParams', 'FragCatalog', 'FragFPGenerator']
class FragCatGenerator(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AddFragsFromMol(self, mol: Mol, fcat: FragCatalog) -> int:
        """
            C++ signature :
                unsigned int AddFragsFromMol(class RDKit::FragCatGenerator {lvalue},class RDKit::ROMol,class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> * __ptr64)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class FragCatParams(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 104
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetFuncGroup(self, fid: int) -> rdkit.Chem.Mol:
        """
            C++ signature :
                class RDKit::ROMol const * __ptr64 GetFuncGroup(class RDKit::FragCatParams {lvalue},int)
        """
    def GetLowerFragLength(self) -> int:
        """
            C++ signature :
                unsigned int GetLowerFragLength(class RDKit::FragCatParams {lvalue})
        """
    def GetNumFuncGroups(self) -> int:
        """
            C++ signature :
                unsigned int GetNumFuncGroups(class RDKit::FragCatParams {lvalue})
        """
    def GetTolerance(self) -> float:
        """
            C++ signature :
                double GetTolerance(class RDKit::FragCatParams {lvalue})
        """
    def GetTypeString(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetTypeString(class RDKit::FragCatParams {lvalue})
        """
    def GetUpperFragLength(self) -> int:
        """
            C++ signature :
                unsigned int GetUpperFragLength(class RDKit::FragCatParams {lvalue})
        """
    def Serialize(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > Serialize(class RDKit::FragCatParams {lvalue})
        """
    def __init__(self, lLen: int, uLen: int, fgroupFilename: str, tol: float = 1e-08) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,int,int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,double=1e-08])
        """
class FragCatalog(Boost.Python.instance):
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 120
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetBitDescription(self, idx: int) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetBitDescription(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetBitDiscrims(self, idx: int) -> _vectdouble:
        """
            C++ signature :
                class std::vector<double,class std::allocator<double> > GetBitDiscrims(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetBitEntryId(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetBitEntryId(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetBitFuncGroupIds(self, idx: int) -> _vectint:
        """
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetBitFuncGroupIds(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetBitOrder(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetBitOrder(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetCatalogParams(self) -> FragCatParams:
        """
            C++ signature :
                class RDKit::FragCatParams * __ptr64 GetCatalogParams(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> {lvalue})
        """
    def GetEntryBitId(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetEntryBitId(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryDescription(self, idx: int) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetEntryDescription(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryDownIds(self, idx: int) -> _vectint:
        """
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetEntryDownIds(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryFuncGroupIds(self, idx: int) -> _vectint:
        """
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetEntryFuncGroupIds(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryOrder(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetEntryOrder(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> const * __ptr64,unsigned int)
        """
    def GetFPLength(self) -> int:
        """
            C++ signature :
                unsigned int GetFPLength(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> {lvalue})
        """
    def GetNumEntries(self) -> int:
        """
            C++ signature :
                unsigned int GetNumEntries(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> {lvalue})
        """
    def Serialize(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > Serialize(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int> {lvalue})
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int>)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __init__(self, params: FragCatParams) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class RDKit::FragCatParams * __ptr64)
        """
    @typing.overload
    def __init__(self, pickle: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
class FragFPGenerator(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetFPForMol(self, mol: Mol, fcat: FragCatalog) -> ExplicitBitVect:
        """
            C++ signature :
                class ExplicitBitVect * __ptr64 GetFPForMol(class RDKit::FragFPGenerator {lvalue},class RDKit::ROMol,class RDCatalog::HierarchCatalog<class RDKit::FragCatalogEntry,class RDKit::FragCatParams,int>)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """

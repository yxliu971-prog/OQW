from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['CreateMolCatalog', 'MolCatalog', 'MolCatalogEntry']
class MolCatalog(Boost.Python.instance):
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 120
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AddEdge(self, id1: int, id2: int) -> None:
        """
            C++ signature :
                void AddEdge(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> {lvalue},unsigned int,unsigned int)
        """
    def AddEntry(self, entry: MolCatalogEntry) -> int:
        """
            C++ signature :
                unsigned int AddEntry(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> * __ptr64,class RDKit::MolCatalogEntry * __ptr64)
        """
    def GetBitDescription(self, idx: int) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetBitDescription(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> const * __ptr64,unsigned int)
        """
    def GetBitEntryId(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetBitEntryId(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryBitId(self, idx: int) -> int:
        """
            C++ signature :
                unsigned int GetEntryBitId(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryDescription(self, idx: int) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetEntryDescription(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> const * __ptr64,unsigned int)
        """
    def GetEntryDownIds(self, idx: int) -> _vectint:
        """
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetEntryDownIds(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> const * __ptr64,unsigned int)
        """
    def GetFPLength(self) -> int:
        """
            C++ signature :
                unsigned int GetFPLength(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> {lvalue})
        """
    def GetNumEntries(self) -> int:
        """
            C++ signature :
                unsigned int GetNumEntries(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> {lvalue})
        """
    def Serialize(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > Serialize(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> {lvalue})
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int>)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
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
class MolCatalogEntry(Boost.Python.instance):
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 96
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetDescription(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetDescription(class RDKit::MolCatalogEntry {lvalue})
        """
    def GetMol(self) -> rdkit.Chem.Mol:
        """
            C++ signature :
                class RDKit::ROMol GetMol(class RDKit::MolCatalogEntry {lvalue})
        """
    def GetOrder(self) -> int:
        """
            C++ signature :
                unsigned int GetOrder(class RDKit::MolCatalogEntry {lvalue})
        """
    def SetDescription(self, val: str) -> None:
        """
            C++ signature :
                void SetDescription(class RDKit::MolCatalogEntry {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def SetMol(self, mol: Mol) -> None:
        """
            C++ signature :
                void SetMol(class RDKit::MolCatalogEntry * __ptr64,class RDKit::ROMol const * __ptr64)
        """
    def SetOrder(self, order: int) -> None:
        """
            C++ signature :
                void SetOrder(class RDKit::MolCatalogEntry {lvalue},unsigned int)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::MolCatalogEntry)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
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
def CreateMolCatalog() -> MolCatalog:
    """
        C++ signature :
            class RDCatalog::HierarchCatalog<class RDKit::MolCatalogEntry,class RDKit::MolCatalogParams,int> * __ptr64 CreateMolCatalog()
    """

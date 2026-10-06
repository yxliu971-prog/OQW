from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['PatternFingerprintTautomerTarget', 'TautomerQuery', 'TautomerQueryCanSerialize']
class TautomerQuery(Boost.Python.instance):
    """
    The Tautomer Query Class.
      Creates a query that enables structure search accounting for matching of
      Tautomeric forms
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetModifiedAtoms(self) -> UnsignedLong_Vect:
        """
            C++ signature :
                class std::vector<unsigned __int64,class std::allocator<unsigned __int64> > GetModifiedAtoms(class RDKit::TautomerQuery {lvalue})
        """
    def GetModifiedBonds(self) -> UnsignedLong_Vect:
        """
            C++ signature :
                class std::vector<unsigned __int64,class std::allocator<unsigned __int64> > GetModifiedBonds(class RDKit::TautomerQuery {lvalue})
        """
    @typing.overload
    def GetSubstructMatch(self, target: Mol, useChirality: bool = False, useQueryQueryMatches: bool = False) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatch(class RDKit::TautomerQuery,class RDKit::ROMol [,bool=False [,bool=False]])
        """
    @typing.overload
    def GetSubstructMatch(self, target: Mol, params: SubstructMatchParameters) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatch(class RDKit::TautomerQuery,class RDKit::ROMol,struct RDKit::SubstructMatchParameters)
        """
    @typing.overload
    def GetSubstructMatches(self, target: Mol, uniquify: bool = True, useChirality: bool = False, useQueryQueryMatches: bool = False, maxMatches: int = 1000) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatches(class RDKit::TautomerQuery,class RDKit::ROMol [,bool=True [,bool=False [,bool=False [,unsigned int=1000]]]])
        """
    @typing.overload
    def GetSubstructMatches(self, target: Mol, params: SubstructMatchParameters) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatches(class RDKit::TautomerQuery,class RDKit::ROMol,struct RDKit::SubstructMatchParameters)
        """
    @typing.overload
    def GetSubstructMatchesWithTautomers(self, target: Mol, uniquify: bool = True, useChirality: bool = False, useQueryQueryMatches: bool = False, maxMatches: int = 1000) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatchesWithTautomers(class RDKit::TautomerQuery,class RDKit::ROMol [,bool=True [,bool=False [,bool=False [,unsigned int=1000]]]])
        """
    @typing.overload
    def GetSubstructMatchesWithTautomers(self, target: Mol, params: SubstructMatchParameters) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetSubstructMatchesWithTautomers(class RDKit::TautomerQuery,class RDKit::ROMol,struct RDKit::SubstructMatchParameters)
        """
    def GetTautomers(self) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 GetTautomers(class RDKit::TautomerQuery)
        """
    def GetTemplateMolecule(self) -> rdkit.Chem.Mol:
        """
            C++ signature :
                class RDKit::ROMol GetTemplateMolecule(class RDKit::TautomerQuery {lvalue})
        """
    @typing.overload
    def IsSubstructOf(self, target: Mol, recursionPossible: bool = True, useChirality: bool = False, useQueryQueryMatches: bool = False) -> bool:
        """
            C++ signature :
                bool IsSubstructOf(class RDKit::TautomerQuery,class RDKit::ROMol [,bool=True [,bool=False [,bool=False]]])
        """
    @typing.overload
    def IsSubstructOf(self, target: Mol, params: SubstructMatchParameters) -> bool:
        """
            C++ signature :
                bool IsSubstructOf(class RDKit::TautomerQuery,class RDKit::ROMol,struct RDKit::SubstructMatchParameters)
        """
    def PatternFingerprintTemplate(self, fingerprintSize: int = 2048) -> ExplicitBitVect:
        """
            C++ signature :
                class ExplicitBitVect * __ptr64 PatternFingerprintTemplate(class RDKit::TautomerQuery {lvalue} [,unsigned int=2048])
        """
    def ToBinary(self) -> typing.Any:
        """
            C++ signature :
                class boost::python::api::object ToBinary(class RDKit::TautomerQuery)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::TautomerQuery)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __init__(self, arg1: Mol) -> typing.Any:
        """
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,class RDKit::ROMol)
        """
    @typing.overload
    def __init__(self, arg1: Mol, arg2: str) -> typing.Any:
        """
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,class RDKit::ROMol,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
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
def PatternFingerprintTautomerTarget(target: Mol, fingerprintSize: int = 2048) -> ExplicitBitVect:
    """
        C++ signature :
            class ExplicitBitVect * __ptr64 PatternFingerprintTautomerTarget(class RDKit::ROMol [,unsigned int=2048])
    """
def TautomerQueryCanSerialize() -> bool:
    """
        Returns True if the TautomerQuery is serializable (requires that the RDKit was built with boost::serialization)
    
        C++ signature :
            bool TautomerQueryCanSerialize()
    """

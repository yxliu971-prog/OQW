"""
Module containing functions for generalized substructure searching
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CreateExtendedQueryMol', 'ExtendedQueryMol', 'MolGetSubstructMatch', 'MolGetSubstructMatches', 'MolHasSubstructMatch', 'PatternFingerprintTarget']
class ExtendedQueryMol(Boost.Python.instance):
    """
    Extended query molecule for use in generalized substructure searching.
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def InitFromBinary(self, pkl: str) -> None:
        """
            C++ signature :
                void InitFromBinary(struct RDKit::GeneralizedSubstruct::ExtendedQueryMol {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def InitFromJSON(self, text: str) -> None:
        """
            C++ signature :
                void InitFromJSON(struct RDKit::GeneralizedSubstruct::ExtendedQueryMol {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def PatternFingerprintQuery(self, fingerprintSize: int = 2048) -> typing.Any:
        """
            C++ signature :
                class std::unique_ptr<class ExplicitBitVect,struct std::default_delete<class ExplicitBitVect> > PatternFingerprintQuery(struct RDKit::GeneralizedSubstruct::ExtendedQueryMol {lvalue} [,unsigned int=2048])
        """
    def ToBinary(self) -> typing.Any:
        """
            C++ signature :
                class boost::python::api::object ToBinary(struct RDKit::GeneralizedSubstruct::ExtendedQueryMol)
        """
    def ToJSON(self) -> str:
        """
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > ToJSON(struct RDKit::GeneralizedSubstruct::ExtendedQueryMol {lvalue})
        """
    def __init__(self, text: str, isJSON: bool = False) -> None:
        """
            constructor from either a binary string (from ToBinary()) or a JSON string.
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
        """
def CreateExtendedQueryMol(mol: Mol, doEnumeration: bool = True, doTautomers: bool = True, adjustQueryProperties: bool = False, adjustQueryParameters: AdjustQueryParameters = None) -> ExtendedQueryMol:
    """
        Creates an ExtendedQueryMol from the input molecule
        
          This takes a query molecule and, conceptually, performs the following steps to
          produce an ExtendedQueryMol:
        
            1. Enumerates features like Link Nodes and SRUs
            2. Converts everything into TautomerQueries
            3. Runs adjustQueryProperties()
        
          Each step is optional
        
    
        C++ signature :
            struct RDKit::GeneralizedSubstruct::ExtendedQueryMol * __ptr64 CreateExtendedQueryMol(class RDKit::ROMol [,bool=True [,bool=True [,bool=False [,struct RDKit::MolOps::AdjustQueryParameters * __ptr64=None]]]])
    """
def MolGetSubstructMatch(mol: Mol, query: ExtendedQueryMol, params: SubstructMatchParameters = None) -> typing.Any:
    """
        returns first match (if any) of a molecule to a generalized substructure query
    
        C++ signature :
            struct _object * __ptr64 MolGetSubstructMatch(class RDKit::ROMol,struct RDKit::GeneralizedSubstruct::ExtendedQueryMol [,struct RDKit::SubstructMatchParameters * __ptr64=None])
    """
def MolGetSubstructMatches(mol: Mol, query: ExtendedQueryMol, params: SubstructMatchParameters = None) -> typing.Any:
    """
        returns all matches (if any) of a molecule to a generalized substructure query
    
        C++ signature :
            struct _object * __ptr64 MolGetSubstructMatches(class RDKit::ROMol,struct RDKit::GeneralizedSubstruct::ExtendedQueryMol [,struct RDKit::SubstructMatchParameters * __ptr64=None])
    """
def MolHasSubstructMatch(mol: Mol, query: ExtendedQueryMol, params: SubstructMatchParameters = None) -> bool:
    """
        determines whether or not a molecule is a match to a generalized substructure query
    
        C++ signature :
            bool MolHasSubstructMatch(class RDKit::ROMol,struct RDKit::GeneralizedSubstruct::ExtendedQueryMol [,struct RDKit::SubstructMatchParameters * __ptr64=None])
    """
def PatternFingerprintTarget(target: Mol, fingerprintSize: int = 2048) -> typing.Any:
    """
        Creates a pattern fingerprint for a target molecule that is compatible with an extended query
    
        C++ signature :
            class std::unique_ptr<class ExplicitBitVect,struct std::default_delete<class ExplicitBitVect> > PatternFingerprintTarget(class RDKit::ROMol [,unsigned int=2048])
    """

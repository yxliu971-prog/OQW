"""
Module containing functions for interchange of molecules.
Note that this should be considered beta and that the format
  and API will very likely change in future releases.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['JSONParseParameters', 'JSONToMols', 'JSONWriteParameters', 'MolToJSON', 'MolsToJSON']
class JSONParseParameters(Boost.Python.instance):
    """
    Parameters controlling the JSON parser
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setattr__(arg1: typing.Any, arg2: str, arg3: typing.Any) -> None:
        """
            C++ signature :
                void __setattr__(class boost::python::api::object,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::api::object)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def parseConformers(*args, **kwargs):
        """
        parse conformers in the JSON
        """
    @parseConformers.setter
    def parseConformers(*args, **kwargs):
        ...
    @property
    def parseProperties(*args, **kwargs):
        """
        parse molecular properties in the JSON
        """
    @parseProperties.setter
    def parseProperties(*args, **kwargs):
        ...
    @property
    def setAromaticBonds(*args, **kwargs):
        """
        set bond types to aromatic for bonds flagged aromatic
        """
    @setAromaticBonds.setter
    def setAromaticBonds(*args, **kwargs):
        ...
    @property
    def strictValenceCheck(*args, **kwargs):
        """
        be strict when checking atom valences
        """
    @strictValenceCheck.setter
    def strictValenceCheck(*args, **kwargs):
        ...
    @property
    def useHCounts(*args, **kwargs):
        """
        use atomic H counts from the JSON. You may want to set this to False when parsing queries.
        """
    @useHCounts.setter
    def useHCounts(*args, **kwargs):
        ...
class JSONWriteParameters(Boost.Python.instance):
    """
    Parameters controlling the JSON writer
    """
    __instance_size__: typing.ClassVar[int] = 32
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setattr__(arg1: typing.Any, arg2: str, arg3: typing.Any) -> None:
        """
            C++ signature :
                void __setattr__(class boost::python::api::object,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::api::object)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def useRDKitExtensions(*args, **kwargs):
        """
        use RDKit extensions to the commonchem format
        """
    @useRDKitExtensions.setter
    def useRDKitExtensions(*args, **kwargs):
        ...
def JSONToMols(jsonBlock: str, params: typing.Any = None) -> tuple:
    """
        Convert JSON to a tuple of molecules
        
            ARGUMENTS:
              - jsonBlock: the molecule to work with
              - params: (optional) JSONParseParameters controlling the JSON parsing
            RETURNS:
              a tuple of Mols
        
    
        C++ signature :
            class boost::python::tuple JSONToMols(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,class boost::python::api::object=None])
    """
def MolToJSON(mol: Mol, params: typing.Any = None) -> str:
    """
        Convert a single molecule to JSON
        
            ARGUMENTS:
              - mol: the molecule to work with
            RETURNS:
              a string
        
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > MolToJSON(class RDKit::ROMol [,class boost::python::api::object=None])
    """
def MolsToJSON(mols: typing.Any, params: typing.Any = None) -> str:
    """
        Convert a set of molecules to JSON
        
            ARGUMENTS:
              - mols: the molecules to work with
            RETURNS:
              a string
        
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > MolsToJSON(class boost::python::api::object [,class boost::python::api::object=None])
    """

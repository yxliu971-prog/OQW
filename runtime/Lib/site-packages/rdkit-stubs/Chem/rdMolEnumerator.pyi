"""
Module containing classes and functions for enumerating molecules
"""
from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['Enumerate', 'EnumeratorType', 'MolEnumeratorParams']
class EnumeratorType(Boost.Python.enum):
    LinkNode: typing.ClassVar[EnumeratorType]  # value = rdkit.Chem.rdMolEnumerator.EnumeratorType.LinkNode
    PositionVariation: typing.ClassVar[EnumeratorType]  # value = rdkit.Chem.rdMolEnumerator.EnumeratorType.PositionVariation
    RepeatUnit: typing.ClassVar[EnumeratorType]  # value = rdkit.Chem.rdMolEnumerator.EnumeratorType.RepeatUnit
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'LinkNode': rdkit.Chem.rdMolEnumerator.EnumeratorType.LinkNode, 'PositionVariation': rdkit.Chem.rdMolEnumerator.EnumeratorType.PositionVariation, 'RepeatUnit': rdkit.Chem.rdMolEnumerator.EnumeratorType.RepeatUnit}
    values: typing.ClassVar[dict]  # value = {0: rdkit.Chem.rdMolEnumerator.EnumeratorType.LinkNode, 1: rdkit.Chem.rdMolEnumerator.EnumeratorType.PositionVariation, 2: rdkit.Chem.rdMolEnumerator.EnumeratorType.RepeatUnit}
class MolEnumeratorParams(Boost.Python.instance):
    """
    Molecular enumerator parameters
    """
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setattr__(arg1: typing.Any, arg2: str, arg3: typing.Any) -> None:
        """
            C++ signature :
                void __setattr__(class boost::python::api::object,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::api::object)
        """
    def SetEnumerationOperator(self, typ: EnumeratorType) -> None:
        """
            set the operator to be used for enumeration
        
            C++ signature :
                void SetEnumerationOperator(struct RDKit::MolEnumerator::MolEnumeratorParams * __ptr64,enum `anonymous namespace'::EnumeratorTypes)
        """
    @typing.overload
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @typing.overload
    def __init__(self, arg1: EnumeratorType) -> typing.Any:
        """
            C++ signature :
                void * __ptr64 __init__(class boost::python::api::object,enum `anonymous namespace'::EnumeratorTypes)
        """
    @property
    def doRandom(*args, **kwargs):
        """
        do random enumeration (not yet implemented
        """
    @doRandom.setter
    def doRandom(*args, **kwargs):
        ...
    @property
    def maxToEnumerate(*args, **kwargs):
        """
        maximum number of molecules to enumerate
        """
    @maxToEnumerate.setter
    def maxToEnumerate(*args, **kwargs):
        ...
    @property
    def randomSeed(*args, **kwargs):
        """
        seed for the random enumeration (not yet implemented
        """
    @randomSeed.setter
    def randomSeed(*args, **kwargs):
        ...
    @property
    def sanitize(*args, **kwargs):
        """
        sanitize molecules after enumeration
        """
    @sanitize.setter
    def sanitize(*args, **kwargs):
        ...
@typing.overload
def Enumerate(mol: Mol, maxPerOperation: int = 0) -> rdkit.Chem.MolBundle:
    """
        do an enumeration and return a MolBundle.
          If maxPerOperation is >0 that will be used as the maximum number of molecules which 
            can be returned by any given operation.
        Limitations:
          - the current implementation does not support molecules which include both
            SRUs and LINKNODEs
          - Overlapping SRUs, i.e. where one monomer is contained within another, are
            not supported
    
        C++ signature :
            class RDKit::MolBundle * __ptr64 Enumerate(class RDKit::ROMol [,unsigned int=0])
    """
@typing.overload
def Enumerate(mol: Mol, enumParams: MolEnumeratorParams) -> rdkit.Chem.MolBundle:
    """
        do an enumeration for the supplied parameter type and return a MolBundle
        Limitations:
          - Overlapping SRUs, i.e. where one monomer is contained within another, are
            not supported
    
        C++ signature :
            class RDKit::MolBundle * __ptr64 Enumerate(class RDKit::ROMol,struct RDKit::MolEnumerator::MolEnumeratorParams)
    """

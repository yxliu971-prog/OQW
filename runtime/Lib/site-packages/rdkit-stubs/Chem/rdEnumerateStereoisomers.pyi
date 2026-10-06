"""
Module containing functions to enumerate stereoisomers of a molecule.  Chiral centers and double bonds will be enumerated if unassigned, or, if the appropriate option is set, if assigned.  Atropisomers will only be enumerated if assigned.  There is, as yet, no means of finding  unassigned atropisomers.
"""
from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['StereoEnumerationOptions', 'StereoisomerEnumerator']
class StereoEnumerationOptions(Boost.Python.instance):
    """
    EnumerateSteroisomers options.
    """
    __instance_size__: typing.ClassVar[int] = 48
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
    def maxIsomers(*args, **kwargs):
        """
        The maximum number of isomers to yield.  If the number of possible isomers is greater than maxIsomers, a random subset will be yielded.  If 0, there is no maximum.  Since every additional stereocenter doubles the number of results (and execution time) it's important to keep an eye on this.
        """
    @maxIsomers.setter
    def maxIsomers(*args, **kwargs):
        ...
    @property
    def onlyStereoGroups(*args, **kwargs):
        """
        If true, only find stereoisomers that differ at the StereoGroups associated with the molecule.  Default=False.
        """
    @onlyStereoGroups.setter
    def onlyStereoGroups(*args, **kwargs):
        ...
    @property
    def onlyUnassigned(*args, **kwargs):
        """
        If true, stereocenters which have a specified stereochemistry will not be perturbed unless they are part of a relative stereo group.  Default=True.
        """
    @onlyUnassigned.setter
    def onlyUnassigned(*args, **kwargs):
        ...
    @property
    def randomSeed(*args, **kwargs):
        """
        Seed for random number generator.  Default=-1 means no seed.
        """
    @randomSeed.setter
    def randomSeed(*args, **kwargs):
        ...
    @property
    def tryEmbedding(*args, **kwargs):
        """
        If true, the process attempts to generate a standard RDKit distance geometry conformation for the stereoisomer.  If this fails, we assume that the stereoisomer is non-physical and don't return it.  NOTE that this is computationally expensive and is just a heuristic that could result in stereoisomers being lost.  Default=False
        """
    @tryEmbedding.setter
    def tryEmbedding(*args, **kwargs):
        ...
    @property
    def unique(*args, **kwargs):
        """
        If true, only stereoisomers that differ in canonical CXSmiles will be returned.  Default=True.
        """
    @unique.setter
    def unique(*args, **kwargs):
        ...
class StereoisomerEnumerator(Boost.Python.instance):
    """
    Stereoisomer enumerator.
    """
    @staticmethod
    def GetStereoisomerCount(arg1: StereoisomerEnumerator) -> int:
        """
            Get the number of stereoisomers.
        
            C++ signature :
                unsigned int GetStereoisomerCount(class `anonymous namespace'::LocalStereoEnumerator {lvalue})
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self, arg1: typing.Any, options: typing.Any = None, verbose: bool = True) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class boost::python::api::object {lvalue} [,class boost::python::api::object {lvalue}=None [,bool=True]])
        """
    def next(self) -> rdkit.Chem.Mol:
        """
            Get next isomer in the sequence, or None if at the end.
        
            C++ signature :
                class boost::shared_ptr<class RDKit::ROMol> next(class `anonymous namespace'::LocalStereoEnumerator {lvalue})
        """

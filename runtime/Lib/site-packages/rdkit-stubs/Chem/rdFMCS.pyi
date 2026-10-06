"""
Module containing a C++ implementation of the FMCS algorithm
"""
from __future__ import annotations
import typing
__all__: list[str] = ['AtomCompare', 'BondCompare', 'FindMCS', 'MCSAcceptance', 'MCSAtomCompare', 'MCSAtomCompareParameters', 'MCSBondCompare', 'MCSBondCompareParameters', 'MCSFinalMatchCheck', 'MCSParameters', 'MCSProgress', 'MCSProgressData', 'MCSResult', 'RingCompare']
class AtomCompare(Boost.Python.enum):
    CompareAny: typing.ClassVar[AtomCompare]  # value = rdkit.Chem.rdFMCS.AtomCompare.CompareAny
    CompareAnyHeavyAtom: typing.ClassVar[AtomCompare]  # value = rdkit.Chem.rdFMCS.AtomCompare.CompareAnyHeavyAtom
    CompareElements: typing.ClassVar[AtomCompare]  # value = rdkit.Chem.rdFMCS.AtomCompare.CompareElements
    CompareIsotopes: typing.ClassVar[AtomCompare]  # value = rdkit.Chem.rdFMCS.AtomCompare.CompareIsotopes
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'CompareAny': rdkit.Chem.rdFMCS.AtomCompare.CompareAny, 'CompareElements': rdkit.Chem.rdFMCS.AtomCompare.CompareElements, 'CompareIsotopes': rdkit.Chem.rdFMCS.AtomCompare.CompareIsotopes, 'CompareAnyHeavyAtom': rdkit.Chem.rdFMCS.AtomCompare.CompareAnyHeavyAtom}
    values: typing.ClassVar[dict]  # value = {0: rdkit.Chem.rdFMCS.AtomCompare.CompareAny, 1: rdkit.Chem.rdFMCS.AtomCompare.CompareElements, 2: rdkit.Chem.rdFMCS.AtomCompare.CompareIsotopes, 3: rdkit.Chem.rdFMCS.AtomCompare.CompareAnyHeavyAtom}
class BondCompare(Boost.Python.enum):
    CompareAny: typing.ClassVar[BondCompare]  # value = rdkit.Chem.rdFMCS.BondCompare.CompareAny
    CompareOrder: typing.ClassVar[BondCompare]  # value = rdkit.Chem.rdFMCS.BondCompare.CompareOrder
    CompareOrderExact: typing.ClassVar[BondCompare]  # value = rdkit.Chem.rdFMCS.BondCompare.CompareOrderExact
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'CompareAny': rdkit.Chem.rdFMCS.BondCompare.CompareAny, 'CompareOrder': rdkit.Chem.rdFMCS.BondCompare.CompareOrder, 'CompareOrderExact': rdkit.Chem.rdFMCS.BondCompare.CompareOrderExact}
    values: typing.ClassVar[dict]  # value = {0: rdkit.Chem.rdFMCS.BondCompare.CompareAny, 1: rdkit.Chem.rdFMCS.BondCompare.CompareOrder, 2: rdkit.Chem.rdFMCS.BondCompare.CompareOrderExact}
class MCSAcceptance(Boost.Python.instance):
    """
    Base class. Subclass and override MCSAcceptance.__call__() to define a custom boolean callback function. Returning True will cause the MCS candidate to be accepted, False to be rejected
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __call__(self) -> bool:
        """
            override to implement a custom MCS acceptance callback
        
            C++ signature :
                bool __call__(struct RDKit::PyMCSAcceptance {lvalue})
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MCSAtomCompare(Boost.Python.instance):
    """
    Base class. Subclass and override MCSAtomCompare.__call__() to define custom atom compare functions, then set MCSParameters.AtomTyper to an instance of the subclass
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def CheckAtomCharge(self, parameters: MCSAtomCompareParameters, mol1: Mol, atom1: int, mol2: Mol, atom2: int) -> bool:
        """
            Return True if both atoms have the same formal charge
        
            C++ signature :
                bool CheckAtomCharge(struct RDKit::PyMCSAtomCompare {lvalue},struct RDKit::MCSAtomCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def CheckAtomChirality(self, parameters: MCSAtomCompareParameters, mol1: Mol, atom1: int, mol2: Mol, atom2: int) -> bool:
        """
            Return True if both atoms have, or have not, a chiral tag
        
            C++ signature :
                bool CheckAtomChirality(struct RDKit::PyMCSAtomCompare {lvalue},struct RDKit::MCSAtomCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def CheckAtomRingMatch(self, parameters: MCSAtomCompareParameters, mol1: Mol, atom1: int, mol2: Mol, atom2: int) -> bool:
        """
            Return True if both atoms are, or are not, in a ring
        
            C++ signature :
                bool CheckAtomRingMatch(struct RDKit::PyMCSAtomCompare {lvalue},struct RDKit::MCSAtomCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def __call__(self, parameters: MCSAtomCompareParameters, mol1: Mol, atom1: int, mol2: Mol, atom2: int) -> bool:
        """
            override to implement custom atom comparison
        
            C++ signature :
                bool __call__(struct RDKit::PyMCSAtomCompare {lvalue},struct RDKit::MCSAtomCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MCSAtomCompareParameters(Boost.Python.instance):
    """
    Parameters controlling how atom-atom matching is done
    """
    __instance_size__: typing.ClassVar[int] = 40
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
    def CompleteRingsOnly(*args, **kwargs):
        """
        results cannot include lone ring atoms
        """
    @CompleteRingsOnly.setter
    def CompleteRingsOnly(*args, **kwargs):
        ...
    @property
    def MatchChiralTag(*args, **kwargs):
        """
        include atom chirality in the match
        """
    @MatchChiralTag.setter
    def MatchChiralTag(*args, **kwargs):
        ...
    @property
    def MatchFormalCharge(*args, **kwargs):
        """
        include formal charge in the match
        """
    @MatchFormalCharge.setter
    def MatchFormalCharge(*args, **kwargs):
        ...
    @property
    def MatchIsotope(*args, **kwargs):
        """
        use isotope atom queries in MCSResults
        """
    @MatchIsotope.setter
    def MatchIsotope(*args, **kwargs):
        ...
    @property
    def MatchValences(*args, **kwargs):
        """
        include atom valences in the match
        """
    @MatchValences.setter
    def MatchValences(*args, **kwargs):
        ...
    @property
    def MaxDistance(*args, **kwargs):
        """
        Require atoms to be within this many angstroms in 3D
        """
    @MaxDistance.setter
    def MaxDistance(*args, **kwargs):
        ...
    @property
    def RingMatchesRingOnly(*args, **kwargs):
        """
        ring atoms are only allowed to match other ring atoms
        """
    @RingMatchesRingOnly.setter
    def RingMatchesRingOnly(*args, **kwargs):
        ...
class MCSBondCompare(Boost.Python.instance):
    """
    Base class. Subclass and override MCSBondCompare.__call__() to define custom bond compare functions, then set MCSParameters.BondTyper to an instance of the subclass
    """
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def CheckBondRingMatch(self, parameters: MCSBondCompareParameters, mol1: Mol, bond1: int, mol2: Mol, bond2: int) -> bool:
        """
            Return True if both bonds are, or are not, part of a ring
        
            C++ signature :
                bool CheckBondRingMatch(struct RDKit::PyMCSBondCompare {lvalue},struct RDKit::MCSBondCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def CheckBondStereo(self, parameters: MCSBondCompareParameters, mol1: Mol, bond1: int, mol2: Mol, bond2: int) -> bool:
        """
            Return True if both bonds have, or have not, a stereo descriptor
        
            C++ signature :
                bool CheckBondStereo(struct RDKit::PyMCSBondCompare {lvalue},struct RDKit::MCSBondCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def __call__(self, parameters: MCSBondCompareParameters, mol1: Mol, bond1: int, mol2: Mol, bond2: int) -> bool:
        """
            override to implement custom bond comparison
        
            C++ signature :
                bool __call__(struct RDKit::PyMCSBondCompare {lvalue},struct RDKit::MCSBondCompareParameters,class RDKit::ROMol,unsigned int,class RDKit::ROMol,unsigned int)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MCSBondCompareParameters(Boost.Python.instance):
    """
    Parameters controlling how bond-bond matching is done
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
    def CompleteRingsOnly(*args, **kwargs):
        """
        results cannot include partial rings
        """
    @CompleteRingsOnly.setter
    def CompleteRingsOnly(*args, **kwargs):
        ...
    @property
    def MatchFusedRings(*args, **kwargs):
        """
        enforce check on ring fusion, i.e. alpha-methylnaphthalene won't match beta-methylnaphtalene, but decalin will match cyclodecane unless MatchFusedRingsStrict is True
        """
    @MatchFusedRings.setter
    def MatchFusedRings(*args, **kwargs):
        ...
    @property
    def MatchFusedRingsStrict(*args, **kwargs):
        """
        only enforced if MatchFusedRings is True; the ring fusion must be the same in both query and target, i.e. decalin won't match cyclodecane
        """
    @MatchFusedRingsStrict.setter
    def MatchFusedRingsStrict(*args, **kwargs):
        ...
    @property
    def MatchStereo(*args, **kwargs):
        """
        include bond stereo in the comparison
        """
    @MatchStereo.setter
    def MatchStereo(*args, **kwargs):
        ...
    @property
    def RingMatchesRingOnly(*args, **kwargs):
        """
        ring bonds are only allowed to match other ring bonds
        """
    @RingMatchesRingOnly.setter
    def RingMatchesRingOnly(*args, **kwargs):
        ...
class MCSFinalMatchCheck(Boost.Python.instance):
    """
    Base class. Subclass and override MCSFinalMatchCheck.__call__() to define a custom boolean callback function. Returning True will cause the growing seed to be accepted, False to be rejected
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __call__(self) -> bool:
        """
            override to implement a custom seed final match checker callback
        
            C++ signature :
                bool __call__(struct RDKit::PyMCSFinalMatchCheck {lvalue})
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MCSParameters(Boost.Python.instance):
    """
    Parameters controlling how the MCS is constructed
    """
    __instance_size__: typing.ClassVar[int] = 168
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
    def AtomCompareParameters(*args, **kwargs):
        """
        parameters for comparing atoms
        """
    @AtomCompareParameters.setter
    def AtomCompareParameters(*args, **kwargs):
        ...
    @property
    def AtomTyper(*args, **kwargs):
        """
        atom typer to be used. Must be one of the members of the rdFMCS.AtomCompare class or an instance of a user-defined subclass of rdFMCS.MCSAtomCompare
        """
    @AtomTyper.setter
    def AtomTyper(*args, **kwargs):
        ...
    @property
    def BondCompareParameters(*args, **kwargs):
        """
        parameters for comparing bonds
        """
    @BondCompareParameters.setter
    def BondCompareParameters(*args, **kwargs):
        ...
    @property
    def BondTyper(*args, **kwargs):
        """
        bond typer to be used. Must be one of the members of the rdFMCS.BondCompare class or an instance of a user-defined subclass of rdFMCS.MCSBondCompare
        """
    @BondTyper.setter
    def BondTyper(*args, **kwargs):
        ...
    @property
    def FinalMatchChecker(*args, **kwargs):
        """
        seed final match checker callback class. Must be a user-defined subclass of rdFMCS.MCSFinalMatchCheck
        """
    @FinalMatchChecker.setter
    def FinalMatchChecker(*args, **kwargs):
        ...
    @property
    def InitialSeed(*args, **kwargs):
        """
        SMILES string to be used as the seed of the MCS
        """
    @InitialSeed.setter
    def InitialSeed(*args, **kwargs):
        ...
    @property
    def MaximizeBonds(*args, **kwargs):
        """
        toggles maximizing the number of bonds (instead of the number of atoms)
        """
    @MaximizeBonds.setter
    def MaximizeBonds(*args, **kwargs):
        ...
    @property
    def ProgressCallback(*args, **kwargs):
        """
        progress callback class. Must be a user-defined subclass of rdFMCS.Progress
        """
    @ProgressCallback.setter
    def ProgressCallback(*args, **kwargs):
        ...
    @property
    def ShouldAcceptMCS(*args, **kwargs):
        """
        MCS acceptance callback class. Must be a user-defined subclass of rdFMCS.MCSAcceptance
        """
    @ShouldAcceptMCS.setter
    def ShouldAcceptMCS(*args, **kwargs):
        ...
    @property
    def StoreAll(*args, **kwargs):
        """
        toggles storage of degenerate MCSs
        """
    @StoreAll.setter
    def StoreAll(*args, **kwargs):
        ...
    @property
    def Threshold(*args, **kwargs):
        """
        fraction of the dataset that must contain the MCS
        """
    @Threshold.setter
    def Threshold(*args, **kwargs):
        ...
    @property
    def Timeout(*args, **kwargs):
        """
        timeout (in seconds) for the calculation
        """
    @Timeout.setter
    def Timeout(*args, **kwargs):
        ...
    @property
    def Verbose(*args, **kwargs):
        """
        toggles verbose mode
        """
    @Verbose.setter
    def Verbose(*args, **kwargs):
        ...
class MCSProgress(Boost.Python.instance):
    """
    Base class. Subclass and override MCSProgress.__call__() to define a custom callback function
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __call__(self, stat: typing.Any, parameters: typing.Any) -> bool:
        """
            override to implement a custom progress callback
        
            C++ signature :
                bool __call__(struct RDKit::PyMCSProgress {lvalue},struct RDKit::MCSProgressData,struct RDKit::MCSParameters)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class MCSProgressData(Boost.Python.instance):
    """
    Information about the MCS progress
    """
    __instance_size__: typing.ClassVar[int] = 40
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def numAtoms(*args, **kwargs):
        """
        number of atoms in MCS
        """
    @property
    def numBonds(*args, **kwargs):
        """
        number of bonds in MCS
        """
    @property
    def seedProcessed(*args, **kwargs):
        """
        number of processed seeds
        """
class MCSResult(Boost.Python.instance):
    """
    used to return MCS results
    """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def canceled(*args, **kwargs):
        """
        if True, the MCS calculation did not finish
        """
    @property
    def degenerateSmartsQueryMolDict(*args, **kwargs):
        """
        Dictionary collecting all degenerate (SMARTS, queryMol) pairs (empty if MCSParameters.StoreAll is False)
        """
    @property
    def numAtoms(*args, **kwargs):
        """
        number of atoms in MCS
        """
    @property
    def numBonds(*args, **kwargs):
        """
        number of bonds in MCS
        """
    @property
    def queryMol(*args, **kwargs):
        """
        query molecule for the MCS
        """
    @property
    def smartsString(*args, **kwargs):
        """
        SMARTS string for the MCS
        """
class RingCompare(Boost.Python.enum):
    IgnoreRingFusion: typing.ClassVar[RingCompare]  # value = rdkit.Chem.rdFMCS.RingCompare.IgnoreRingFusion
    PermissiveRingFusion: typing.ClassVar[RingCompare]  # value = rdkit.Chem.rdFMCS.RingCompare.PermissiveRingFusion
    StrictRingFusion: typing.ClassVar[RingCompare]  # value = rdkit.Chem.rdFMCS.RingCompare.StrictRingFusion
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'IgnoreRingFusion': rdkit.Chem.rdFMCS.RingCompare.IgnoreRingFusion, 'PermissiveRingFusion': rdkit.Chem.rdFMCS.RingCompare.PermissiveRingFusion, 'StrictRingFusion': rdkit.Chem.rdFMCS.RingCompare.StrictRingFusion}
    values: typing.ClassVar[dict]  # value = {0: rdkit.Chem.rdFMCS.RingCompare.IgnoreRingFusion, 1: rdkit.Chem.rdFMCS.RingCompare.PermissiveRingFusion, 2: rdkit.Chem.rdFMCS.RingCompare.StrictRingFusion}
@typing.overload
def FindMCS(mols: typing.Any, maximizeBonds: bool = True, threshold: float = 1.0, timeout: int = 3600, verbose: bool = False, matchValences: bool = False, ringMatchesRingOnly: bool = False, completeRingsOnly: bool = False, matchChiralTag: bool = False, atomCompare: AtomCompare = ..., bondCompare: BondCompare = ..., ringCompare: RingCompare = ..., seedSmarts: str = '') -> MCSResult:
    """
        Find the MCS for a set of molecules
    
        C++ signature :
            struct RDKit::MCSResult * __ptr64 FindMCS(class boost::python::api::object [,bool=True [,double=1.0 [,unsigned int=3600 [,bool=False [,bool=False [,bool=False [,bool=False [,bool=False [,enum RDKit::AtomComparator=rdkit.Chem.rdFMCS.AtomCompare.CompareElements [,enum RDKit::BondComparator=rdkit.Chem.rdFMCS.BondCompare.CompareOrder [,enum RDKit::RingComparator=rdkit.Chem.rdFMCS.RingCompare.IgnoreRingFusion [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='']]]]]]]]]]]])
    """
@typing.overload
def FindMCS(mols: typing.Any, parameters: MCSParameters) -> MCSResult:
    """
        Find the MCS for a set of molecules
    
        C++ signature :
            struct RDKit::MCSResult * __ptr64 FindMCS(class boost::python::api::object,class RDKit::PyMCSParameters {lvalue})
    """

"""
Module containing RDKit functionality for querying molecules.
"""
from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['AAtomQueryAtom', 'AHAtomQueryAtom', 'AtomNumEqualsQueryAtom', 'AtomNumGreaterQueryAtom', 'AtomNumLessQueryAtom', 'ExplicitDegreeEqualsQueryAtom', 'ExplicitDegreeGreaterQueryAtom', 'ExplicitDegreeLessQueryAtom', 'ExplicitValenceEqualsQueryAtom', 'ExplicitValenceGreaterQueryAtom', 'ExplicitValenceLessQueryAtom', 'FormalChargeEqualsQueryAtom', 'FormalChargeGreaterQueryAtom', 'FormalChargeLessQueryAtom', 'HCountEqualsQueryAtom', 'HCountGreaterQueryAtom', 'HCountLessQueryAtom', 'HasBitVectPropWithValueQueryAtom', 'HasBoolPropWithValueQueryAtom', 'HasBoolPropWithValueQueryBond', 'HasChiralTagQueryAtom', 'HasDoublePropWithValueQueryAtom', 'HasDoublePropWithValueQueryBond', 'HasIntPropWithValueQueryAtom', 'HasIntPropWithValueQueryBond', 'HasPropQueryAtom', 'HasPropQueryBond', 'HasStringPropWithValueQueryAtom', 'HasStringPropWithValueQueryBond', 'HybridizationEqualsQueryAtom', 'HybridizationGreaterQueryAtom', 'HybridizationLessQueryAtom', 'InNRingsEqualsQueryAtom', 'InNRingsGreaterQueryAtom', 'InNRingsLessQueryAtom', 'IsAliphaticQueryAtom', 'IsAromaticQueryAtom', 'IsBridgeheadQueryAtom', 'IsInRingQueryAtom', 'IsUnsaturatedQueryAtom', 'IsotopeEqualsQueryAtom', 'IsotopeGreaterQueryAtom', 'IsotopeLessQueryAtom', 'MAtomQueryAtom', 'MHAtomQueryAtom', 'MassEqualsQueryAtom', 'MassGreaterQueryAtom', 'MassLessQueryAtom', 'MinRingSizeEqualsQueryAtom', 'MinRingSizeGreaterQueryAtom', 'MinRingSizeLessQueryAtom', 'MissingChiralTagQueryAtom', 'NonHydrogenDegreeEqualsQueryAtom', 'NonHydrogenDegreeGreaterQueryAtom', 'NonHydrogenDegreeLessQueryAtom', 'NumAliphaticHeteroatomNeighborsEqualsQueryAtom', 'NumAliphaticHeteroatomNeighborsGreaterQueryAtom', 'NumAliphaticHeteroatomNeighborsLessQueryAtom', 'NumHeteroatomNeighborsEqualsQueryAtom', 'NumHeteroatomNeighborsGreaterQueryAtom', 'NumHeteroatomNeighborsLessQueryAtom', 'NumRadicalElectronsEqualsQueryAtom', 'NumRadicalElectronsGreaterQueryAtom', 'NumRadicalElectronsLessQueryAtom', 'QAtomQueryAtom', 'QHAtomQueryAtom', 'ReplaceAtomWithQueryAtom', 'RingBondCountEqualsQueryAtom', 'RingBondCountGreaterQueryAtom', 'RingBondCountLessQueryAtom', 'TotalDegreeEqualsQueryAtom', 'TotalDegreeGreaterQueryAtom', 'TotalDegreeLessQueryAtom', 'TotalValenceEqualsQueryAtom', 'TotalValenceGreaterQueryAtom', 'TotalValenceLessQueryAtom', 'XAtomQueryAtom', 'XHAtomQueryAtom']
def AAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when AAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 AAtomQueryAtom([ bool=False])
    """
def AHAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when AHAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 AHAtomQueryAtom([ bool=False])
    """
def AtomNumEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where AtomNum is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 AtomNumEqualsQueryAtom(int [,bool=False])
    """
def AtomNumGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where AtomNum is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 AtomNumGreaterQueryAtom(int [,bool=False])
    """
def AtomNumLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where AtomNum is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 AtomNumLessQueryAtom(int [,bool=False])
    """
def ExplicitDegreeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitDegree is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitDegreeEqualsQueryAtom(int [,bool=False])
    """
def ExplicitDegreeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitDegree is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitDegreeGreaterQueryAtom(int [,bool=False])
    """
def ExplicitDegreeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitDegree is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitDegreeLessQueryAtom(int [,bool=False])
    """
def ExplicitValenceEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitValence is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitValenceEqualsQueryAtom(int [,bool=False])
    """
def ExplicitValenceGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitValence is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitValenceGreaterQueryAtom(int [,bool=False])
    """
def ExplicitValenceLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where ExplicitValence is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 ExplicitValenceLessQueryAtom(int [,bool=False])
    """
def FormalChargeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where FormalCharge is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 FormalChargeEqualsQueryAtom(int [,bool=False])
    """
def FormalChargeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where FormalCharge is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 FormalChargeGreaterQueryAtom(int [,bool=False])
    """
def FormalChargeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where FormalCharge is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 FormalChargeLessQueryAtom(int [,bool=False])
    """
def HCountEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where HCount is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HCountEqualsQueryAtom(int [,bool=False])
    """
def HCountGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where HCount is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HCountGreaterQueryAtom(int [,bool=False])
    """
def HCountLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where HCount is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HCountLessQueryAtom(int [,bool=False])
    """
def HasBitVectPropWithValueQueryAtom(propname: str, val: ExplicitBitVect, negate: bool = False, tolerance: float = 0) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' has the specified explicit bit vector value.  The Tolerance is the allowed Tanimoto difference
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasBitVectPropWithValueQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class ExplicitBitVect [,bool=False [,float=0]])
    """
def HasBoolPropWithValueQueryAtom(propname: str, val: bool, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' has the specified boolean value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasBoolPropWithValueQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,bool=False])
    """
def HasBoolPropWithValueQueryBond(propname: str, val: bool, negate: bool = False) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' has the specified boolean value.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasBoolPropWithValueQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,bool=False])
    """
def HasChiralTagQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when HasChiralTag is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasChiralTagQueryAtom([ bool=False])
    """
def HasDoublePropWithValueQueryAtom(propname: str, val: float, negate: bool = False, tolerance: float = 0.0) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' has the specified value +- tolerance
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasDoublePropWithValueQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double [,bool=False [,double=0.0]])
    """
def HasDoublePropWithValueQueryBond(propname: str, val: float, negate: bool = False, tolerance: float = 0.0) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' has the specified value +- tolerance
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasDoublePropWithValueQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double [,bool=False [,double=0.0]])
    """
def HasIntPropWithValueQueryAtom(propname: str, val: int, negate: bool = False, tolerance: int = 0) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' has the specified int value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasIntPropWithValueQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int [,bool=False [,int=0]])
    """
def HasIntPropWithValueQueryBond(propname: str, val: int, negate: bool = False, tolerance: int = 0) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' has the specified int value.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasIntPropWithValueQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,int [,bool=False [,int=0]])
    """
def HasPropQueryAtom(propname: str, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' exists in the atom.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasPropQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
@typing.overload
def HasPropQueryBond(propname: str, negate: bool = False) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' exists in the bond.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasPropQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
@typing.overload
def HasPropQueryBond(propname: str, negate: bool = False) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' exists in the bond.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasPropQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
@typing.overload
def HasPropQueryBond(propname: str, negate: bool = False) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' exists in the bond.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasPropQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
def HasStringPropWithValueQueryAtom(propname: str, val: str, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches when the property 'propname' has the specified string value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HasStringPropWithValueQueryAtom(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
def HasStringPropWithValueQueryBond(propname: str, val: str, negate: bool = False) -> rdkit.Chem.QueryBond:
    """
        Returns a QueryBond that matches when the property 'propname' has the specified string value.
    
        C++ signature :
            class RDKit::QueryBond * __ptr64 HasStringPropWithValueQueryBond(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
    """
def HybridizationEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Hybridization is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HybridizationEqualsQueryAtom(int [,bool=False])
    """
def HybridizationGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Hybridization is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HybridizationGreaterQueryAtom(int [,bool=False])
    """
def HybridizationLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Hybridization is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 HybridizationLessQueryAtom(int [,bool=False])
    """
def InNRingsEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where InNRings is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 InNRingsEqualsQueryAtom(int [,bool=False])
    """
def InNRingsGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where InNRings is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 InNRingsGreaterQueryAtom(int [,bool=False])
    """
def InNRingsLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where InNRings is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 InNRingsLessQueryAtom(int [,bool=False])
    """
def IsAliphaticQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when IsAliphatic is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsAliphaticQueryAtom([ bool=False])
    """
def IsAromaticQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when IsAromatic is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsAromaticQueryAtom([ bool=False])
    """
def IsBridgeheadQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when IsBridgehead is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsBridgeheadQueryAtom([ bool=False])
    """
def IsInRingQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when IsInRing is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsInRingQueryAtom([ bool=False])
    """
def IsUnsaturatedQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when IsUnsaturated is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsUnsaturatedQueryAtom([ bool=False])
    """
def IsotopeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Isotope is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsotopeEqualsQueryAtom(int [,bool=False])
    """
def IsotopeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Isotope is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsotopeGreaterQueryAtom(int [,bool=False])
    """
def IsotopeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Isotope is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 IsotopeLessQueryAtom(int [,bool=False])
    """
def MAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when MAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MAtomQueryAtom([ bool=False])
    """
def MHAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when MHAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MHAtomQueryAtom([ bool=False])
    """
def MassEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Mass is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MassEqualsQueryAtom(int [,bool=False])
    """
def MassGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Mass is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MassGreaterQueryAtom(int [,bool=False])
    """
def MassLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where Mass is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MassLessQueryAtom(int [,bool=False])
    """
def MinRingSizeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where MinRingSize is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MinRingSizeEqualsQueryAtom(int [,bool=False])
    """
def MinRingSizeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where MinRingSize is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MinRingSizeGreaterQueryAtom(int [,bool=False])
    """
def MinRingSizeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where MinRingSize is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MinRingSizeLessQueryAtom(int [,bool=False])
    """
def MissingChiralTagQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when MissingChiralTag is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 MissingChiralTagQueryAtom([ bool=False])
    """
def NonHydrogenDegreeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NonHydrogenDegree is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NonHydrogenDegreeEqualsQueryAtom(int [,bool=False])
    """
def NonHydrogenDegreeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NonHydrogenDegree is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NonHydrogenDegreeGreaterQueryAtom(int [,bool=False])
    """
def NonHydrogenDegreeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NonHydrogenDegree is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NonHydrogenDegreeLessQueryAtom(int [,bool=False])
    """
def NumAliphaticHeteroatomNeighborsEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumAliphaticHeteroatomNeighbors is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumAliphaticHeteroatomNeighborsEqualsQueryAtom(int [,bool=False])
    """
def NumAliphaticHeteroatomNeighborsGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumAliphaticHeteroatomNeighbors is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumAliphaticHeteroatomNeighborsGreaterQueryAtom(int [,bool=False])
    """
def NumAliphaticHeteroatomNeighborsLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumAliphaticHeteroatomNeighbors is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumAliphaticHeteroatomNeighborsLessQueryAtom(int [,bool=False])
    """
def NumHeteroatomNeighborsEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumHeteroatomNeighbors is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumHeteroatomNeighborsEqualsQueryAtom(int [,bool=False])
    """
def NumHeteroatomNeighborsGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumHeteroatomNeighbors is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumHeteroatomNeighborsGreaterQueryAtom(int [,bool=False])
    """
def NumHeteroatomNeighborsLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumHeteroatomNeighbors is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumHeteroatomNeighborsLessQueryAtom(int [,bool=False])
    """
def NumRadicalElectronsEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumRadicalElectrons is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumRadicalElectronsEqualsQueryAtom(int [,bool=False])
    """
def NumRadicalElectronsGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumRadicalElectrons is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumRadicalElectronsGreaterQueryAtom(int [,bool=False])
    """
def NumRadicalElectronsLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where NumRadicalElectrons is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 NumRadicalElectronsLessQueryAtom(int [,bool=False])
    """
def QAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when QAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 QAtomQueryAtom([ bool=False])
    """
def QHAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when QHAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 QHAtomQueryAtom([ bool=False])
    """
def ReplaceAtomWithQueryAtom(mol: Mol, atom: Atom) -> rdkit.Chem.Atom:
    """
        Changes the given atom in the molecule to
        a query atom and returns the atom which can then be modified, for example
        with additional query constraints added.  The new atom is otherwise a copy
        of the old.
        If the atom already has a query, nothing will be changed.
    
        C++ signature :
            class RDKit::Atom * __ptr64 ReplaceAtomWithQueryAtom(class RDKit::ROMol {lvalue},class RDKit::Atom {lvalue})
    """
def RingBondCountEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where RingBondCount is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 RingBondCountEqualsQueryAtom(int [,bool=False])
    """
def RingBondCountGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where RingBondCount is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 RingBondCountGreaterQueryAtom(int [,bool=False])
    """
def RingBondCountLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where RingBondCount is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 RingBondCountLessQueryAtom(int [,bool=False])
    """
def TotalDegreeEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalDegree is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalDegreeEqualsQueryAtom(int [,bool=False])
    """
def TotalDegreeGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalDegree is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalDegreeGreaterQueryAtom(int [,bool=False])
    """
def TotalDegreeLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalDegree is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalDegreeLessQueryAtom(int [,bool=False])
    """
def TotalValenceEqualsQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalValence is equal to the target value.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalValenceEqualsQueryAtom(int [,bool=False])
    """
def TotalValenceGreaterQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalValence is equal to the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalValenceGreaterQueryAtom(int [,bool=False])
    """
def TotalValenceLessQueryAtom(val: int, negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms where TotalValence is less than the target value.
        NOTE: the direction of comparison is reversed relative to the C++ API
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 TotalValenceLessQueryAtom(int [,bool=False])
    """
def XAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when XAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 XAtomQueryAtom([ bool=False])
    """
def XHAtomQueryAtom(negate: bool = False) -> rdkit.Chem.QueryAtom:
    """
        Returns a QueryAtom that matches atoms when XHAtom is True.
    
        C++ signature :
            class RDKit::QueryAtom * __ptr64 XHAtomQueryAtom([ bool=False])
    """

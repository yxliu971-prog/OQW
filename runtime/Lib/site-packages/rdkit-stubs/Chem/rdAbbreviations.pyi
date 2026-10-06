"""
Module containing functions for working with molecular abbreviations
"""
from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['AbbreviationDefinition', 'CondenseAbbreviationSubstanceGroups', 'CondenseMolAbbreviations', 'GetDefaultAbbreviations', 'GetDefaultLinkers', 'LabelMolAbbreviations', 'ParseAbbreviations', 'ParseLinkers']
class AbbreviationDefinition(Boost.Python.instance):
    """
    Abbreviation Definition
    """
    __instance_size__: typing.ClassVar[int] = 200
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def displayLabel(*args, **kwargs):
        """
        the label in a drawing when the bond comes from the right
        """
    @displayLabel.setter
    def displayLabel(*args, **kwargs):
        ...
    @property
    def displayLabelW(*args, **kwargs):
        """
        the label in a drawing when the bond comes from the west
        """
    @displayLabelW.setter
    def displayLabelW(*args, **kwargs):
        ...
    @property
    def includesXBonds(*args, **kwargs):
        """
        whether or not the abbreviation definition includes bonds to non-abbreviation atoms
        """
    @includesXBonds.setter
    def includesXBonds(*args, **kwargs):
        ...
    @property
    def label(*args, **kwargs):
        """
        the label
        """
    @label.setter
    def label(*args, **kwargs):
        ...
    @property
    def mol(*args, **kwargs):
        """
        the query molecule (should have a dummy as the first atom if includesXBonds is true)
        """
    @mol.setter
    def mol(*args, **kwargs):
        ...
def CondenseAbbreviationSubstanceGroups(mol: Mol) -> rdkit.Chem.Mol:
    """
        Finds and replaces abbreviation (i.e. "SUP") substance groups in a molecule. The result is not sanitized.
    
        C++ signature :
            class RDKit::ROMol * __ptr64 CondenseAbbreviationSubstanceGroups(class RDKit::ROMol const * __ptr64)
    """
def CondenseMolAbbreviations(mol: Mol, abbrevs: typing.Any, maxCoverage: float = 0.4, sanitize: bool = True) -> rdkit.Chem.Mol:
    """
        Finds and replaces abbreviations in a molecule. The result is not sanitized.
    
        C++ signature :
            class RDKit::ROMol * __ptr64 CondenseMolAbbreviations(class RDKit::ROMol const * __ptr64,class boost::python::api::object [,double=0.4 [,bool=True]])
    """
def GetDefaultAbbreviations() -> ...:
    """
        returns a list of the default abbreviation definitions
    
        C++ signature :
            class std::vector<struct RDKit::Abbreviations::AbbreviationDefinition,class std::allocator<struct RDKit::Abbreviations::AbbreviationDefinition> > GetDefaultAbbreviations()
    """
def GetDefaultLinkers() -> ...:
    """
        returns a list of the default linker definitions
    
        C++ signature :
            class std::vector<struct RDKit::Abbreviations::AbbreviationDefinition,class std::allocator<struct RDKit::Abbreviations::AbbreviationDefinition> > GetDefaultLinkers()
    """
def LabelMolAbbreviations(mol: Mol, abbrevs: typing.Any, maxCoverage: float = 0.4) -> rdkit.Chem.Mol:
    """
        Finds abbreviations and adds to them to a molecule as "SUP" SubstanceGroups
    
        C++ signature :
            class RDKit::ROMol * __ptr64 LabelMolAbbreviations(class RDKit::ROMol const * __ptr64,class boost::python::api::object [,double=0.4])
    """
def ParseAbbreviations(*args, **kwargs) -> ...:
    """
        Returns a set of abbreviation definitions from a string.  Format of the text data:  A series of lines, each of which contains: label SMARTS displayLabel displayLabelW  Where label is the label used for the abbreviation, SMARTS is the SMARTS definition of the abbreviation, displayLabel is used in drawings to render the abbreviations and displayLabelW is the display label if a bond comes in from the right.  The 'displayLabel' and 'displayLabelW' fields are optional.  Use dummies in the SMARTS to indicate attachment points. The assumption is that the first atom is a dummy (one will be added if this is not true) and that the second atom is the surrogate for the rest of the group.
    
        C++ signature :
            class std::vector<struct RDKit::Abbreviations::AbbreviationDefinition,class std::allocator<struct RDKit::Abbreviations::AbbreviationDefinition> > ParseAbbreviations(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False [,bool=False]])
    """
def ParseLinkers(*args, **kwargs) -> ...:
    """
        Returns a set of linker definitions from a string.  Equivalent to calling ParseAbbreviations(text, True True).
    
        C++ signature :
            class std::vector<struct RDKit::Abbreviations::AbbreviationDefinition,class std::allocator<struct RDKit::Abbreviations::AbbreviationDefinition> > ParseLinkers(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """

"""
Module containing a C++ implementation of code for doing MMPA
"""
from __future__ import annotations
import typing
__all__: list[str] = ['FragmentMol']
@typing.overload
def FragmentMol(*args, **kwargs) -> tuple:
    """
        Does the fragmentation necessary for an MMPA analysis
    
        C++ signature :
            class boost::python::tuple FragmentMol(class RDKit::ROMol [,unsigned int=3 [,unsigned int=20 [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='[#6+0;!$(*=,#[!#6])]!@!=!#[*]' [,bool=True]]]])
    """
@typing.overload
def FragmentMol(*args, **kwargs) -> tuple:
    """
        Does the fragmentation necessary for an MMPA analysis
    
        C++ signature :
            class boost::python::tuple FragmentMol(class RDKit::ROMol,unsigned int,unsigned int,unsigned int [,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >='[#6+0;!$(*=,#[!#6])]!@!=!#[*]' [,bool=True]])
    """
@typing.overload
def FragmentMol(mol: Mol, bondsToCut: typing.Any, minCuts: int = 1, maxCuts: int = 3, resultsAsMols: bool = True) -> tuple:
    """
        Does the fragmentation necessary for an MMPA analysis
    
        C++ signature :
            class boost::python::tuple FragmentMol(class RDKit::ROMol,class boost::python::api::object [,unsigned int=1 [,unsigned int=3 [,bool=True]]])
    """

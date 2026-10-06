"""
Module containing interface to the CoordGen library.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['AddCoords', 'CoordGenParams', 'SetDefaultTemplateFileDir']
class CoordGenParams(Boost.Python.instance):
    """
    Parameters controlling coordinate generation
    """
    __instance_size__: typing.ClassVar[int] = 112
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setattr__(arg1: typing.Any, arg2: str, arg3: typing.Any) -> None:
        """
            C++ signature :
                void __setattr__(class boost::python::api::object,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::api::object)
        """
    def SetCoordMap(self, coordMap: dict) -> None:
        """
            expects a dictionary of Point2D objects with template coordinates
        
            C++ signature :
                void SetCoordMap(struct RDKit::CoordGen::CoordGenParams * __ptr64,class boost::python::dict {lvalue})
        """
    def SetTemplateMol(self, templ: Mol) -> None:
        """
            sets a molecule to be used as the template
        
            C++ signature :
                void SetTemplateMol(struct RDKit::CoordGen::CoordGenParams * __ptr64,class RDKit::ROMol const * __ptr64)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def coordgenScaling(*args, **kwargs):
        """
        scaling factor for a single bond
        """
    @coordgenScaling.setter
    def coordgenScaling(*args, **kwargs):
        ...
    @property
    def dbg_useConstrained(*args, **kwargs):
        """
        for debugging use
        """
    @dbg_useConstrained.setter
    def dbg_useConstrained(*args, **kwargs):
        ...
    @property
    def dbg_useFixed(*args, **kwargs):
        """
        for debugging use
        """
    @dbg_useFixed.setter
    def dbg_useFixed(*args, **kwargs):
        ...
    @property
    def minimizerPrecision(*args, **kwargs):
        """
        controls sketcher precision
        """
    @minimizerPrecision.setter
    def minimizerPrecision(*args, **kwargs):
        ...
    @property
    def sketcherBestPrecision(*args, **kwargs):
        """
        highest quality (and slowest) precision setting
        """
    @property
    def sketcherCoarsePrecision(*args, **kwargs):
        """
        "coarse" (fastest) precision setting, produces good-quality coordinates most of the time, this is the default setting for the RDKit
        """
    @property
    def sketcherQuickPrecision(*args, **kwargs):
        """
        faster precision setting
        """
    @property
    def sketcherStandardPrecision(*args, **kwargs):
        """
        standard quality precision setting, the default for the coordgen project
        """
    @property
    def templateFileDir(*args, **kwargs):
        """
        directory containing the templates.mae file
        """
    @templateFileDir.setter
    def templateFileDir(*args, **kwargs):
        ...
    @property
    def treatNonterminalBondsToMetalAsZOBs(*args, **kwargs):
        ...
    @treatNonterminalBondsToMetalAsZOBs.setter
    def treatNonterminalBondsToMetalAsZOBs(*args, **kwargs):
        ...
def AddCoords(mol: Mol, params: typing.Any = None) -> None:
    """
        Add 2D coordinates.
        ARGUMENTS:
           - mol: molecule to modify
           - params: (optional) parameters controlling the coordinate generation
        
        
    
        C++ signature :
            void AddCoords(class RDKit::ROMol {lvalue} [,class boost::python::api::object {lvalue}=None])
    """
def SetDefaultTemplateFileDir(dir: str) -> None:
    """
        C++ signature :
            void SetDefaultTemplateFileDir(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """

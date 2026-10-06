"""
Module containing functions to generate and work with reduced graphs
"""
from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['GenerateErGFingerprintForReducedGraph', 'GenerateMolExtendedReducedGraph', 'GetErGFingerprint']
def GenerateErGFingerprintForReducedGraph(mol: Mol, atomTypes: typing.Any = 0, fuzzIncrement: float = 0.3, minPath: int = 1, maxPath: int = 15) -> typing.Any:
    """
        Returns the ErG fingerprint vector for a reduced graph
    
        C++ signature :
            struct _object * __ptr64 GenerateErGFingerprintForReducedGraph(class RDKit::ROMol [,class boost::python::api::object=0 [,double=0.3 [,int=1 [,int=15]]]])
    """
def GenerateMolExtendedReducedGraph(mol: Mol, atomTypes: typing.Any = 0) -> rdkit.Chem.Mol:
    """
        Returns the reduced graph for a molecule
    
        C++ signature :
            class RDKit::ROMol * __ptr64 GenerateMolExtendedReducedGraph(class RDKit::ROMol [,class boost::python::api::object=0])
    """
def GetErGFingerprint(mol: Mol, atomTypes: typing.Any = 0, fuzzIncrement: float = 0.3, minPath: int = 1, maxPath: int = 15) -> typing.Any:
    """
        Returns the ErG fingerprint vector for a molecule
    
        C++ signature :
            struct _object * __ptr64 GetErGFingerprint(class RDKit::ROMol [,class boost::python::api::object=0 [,double=0.3 [,int=1 [,int=15]]]])
    """

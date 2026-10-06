"""
Module containing classes and functions for working with Sybyl line notation (SLN).
"""
from __future__ import annotations
import rdkit.Chem
__all__: list[str] = ['MolFromQuerySLN', 'MolFromSLN']
def MolFromQuerySLN(SLN: str, mergeHs: bool = True, debugParser: bool = False) -> rdkit.Chem.Mol:
    """
        Construct a query molecule from an SLN string.
        
          ARGUMENTS:
        
            - SLN: the SLN string
        
            - mergeHs: (optional) toggles the merging of explicit Hs in the query into the attached
              heavy atoms. Defaults to False.
        
          RETURNS:
        
            a Mol object suitable for using in substructure queries, None on failure.
        
        
    
        C++ signature :
            class RDKit::ROMol * __ptr64 MolFromQuerySLN(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=True [,bool=False]])
    """
def MolFromSLN(SLN: str, sanitize: bool = True, debugParser: bool = False) -> rdkit.Chem.Mol:
    """
        Construct a molecule from an SLN string.
        
            ARGUMENTS:
        
            - SLN: the SLN string
        
            - sanitize: (optional) toggles sanitization of the molecule.
              Defaults to True.
        
          RETURNS:
        
            a Mol object, None on failure.
        
          NOTE: the SLN should not contain query information or properties. To build a
            query from SLN, use MolFromQuerySLN.
        
        
    
        C++ signature :
            class RDKit::ROMol * __ptr64 MolFromSLN(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=True [,bool=False]])
    """

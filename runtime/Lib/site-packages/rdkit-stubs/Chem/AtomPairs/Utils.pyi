from __future__ import annotations
import math as math
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
import warnings as warnings
__all__: list[str] = ['BitsInCommon', 'Chem', 'CosineSimilarity', 'DiceSimilarity', 'Dot', 'ExplainAtomCode', 'math', 'rdMolDescriptors', 'warnings']
def BitsInCommon(v1, v2):
    """
     Returns the number of bits in common between two vectors
    
        **Arguments**:
    
          - two vectors (sequences of bit ids)
    
        **Returns**: an integer
    
        **Notes**
    
          - the vectors must be sorted
    
          - duplicate bit IDs are counted more than once
    
        >>> BitsInCommon( (1,2,3,4,10), (2,4,6) )
        2
    
        Here's how duplicates are handled:
    
        >>> BitsInCommon( (1,2,2,3,4), (2,2,4,5,6) )
        3
    
        
    """
def CosineSimilarity(v1, v2):
    """
     Implements the Cosine similarity metric.
         This is the recommended metric in the LaSSI paper
    
        **Arguments**:
    
          - two vectors (sequences of bit ids)
    
        **Returns**: a float.
    
        **Notes**
    
          - the vectors must be sorted
    
        >>> print('%.3f'%CosineSimilarity( (1,2,3,4,10), (2,4,6) ))
        0.516
        >>> print('%.3f'%CosineSimilarity( (1,2,2,3,4), (2,2,4,5,6) ))
        0.714
        >>> print('%.3f'%CosineSimilarity( (1,2,2,3,4), (1,2,2,3,4) ))
        1.000
        >>> print('%.3f'%CosineSimilarity( (1,2,2,3,4), (5,6,7) ))
        0.000
        >>> print('%.3f'%CosineSimilarity( (1,2,2,3,4), () ))
        0.000
    
        
    """
def DiceSimilarity(v1, v2, bounds = None):
    """
     Implements the DICE similarity metric.
         This is the recommended metric in both the Topological torsions
         and Atom pairs papers.
    
        **Arguments**:
    
          - two vectors (sequences of bit ids)
    
        **Returns**: a float.
    
        **Notes**
    
          - the vectors must be sorted
    
    
        >>> DiceSimilarity( (1,2,3), (1,2,3) )
        1.0
        >>> DiceSimilarity( (1,2,3), (5,6) )
        0.0
        >>> DiceSimilarity( (1,2,3,4), (1,3,5,7) )
        0.5
        >>> DiceSimilarity( (1,2,3,4,5,6), (1,3) )
        0.5
    
        Note that duplicate bit IDs count multiple times:
    
        >>> DiceSimilarity( (1,1,3,4,5,6), (1,1) )
        0.5
    
        but only if they are duplicated in both vectors:
    
        >>> DiceSimilarity( (1,1,3,4,5,6), (1,) )==2./7
        True
    
        edge case
    
        >>> DiceSimilarity( (), () )
        0.0
    
        and bounds check
    
        >>> DiceSimilarity( (1,1,3,4), (1,1))
        0.666...
        >>> DiceSimilarity( (1,1,3,4), (1,1), bounds=0.3)
        0.666...
        >>> DiceSimilarity( (1,1,3,4), (1,1), bounds=0.33)
        0.666...
        >>> DiceSimilarity( (1,1,3,4,5,6), (1,1), bounds=0.34)
        0.0
    
        
    """
def Dot(v1, v2):
    """
     Returns the Dot product between two vectors:
    
        **Arguments**:
    
          - two vectors (sequences of bit ids)
    
        **Returns**: an integer
    
        **Notes**
    
          - the vectors must be sorted
    
          - duplicate bit IDs are counted more than once
    
        >>> Dot( (1,2,3,4,10), (2,4,6) )
        2
    
        Here's how duplicates are handled:
    
        >>> Dot( (1,2,2,3,4), (2,2,4,5,6) )
        5
        >>> Dot( (1,2,2,3,4), (2,4,5,6) )
        2
        >>> Dot( (1,2,2,3,4), (5,6) )
        0
        >>> Dot( (), (5,6) )
        0
    
        
    """
def ExplainAtomCode(code, branchSubtract = 0, includeChirality = False):
    """
    
    
        **Arguments**:
    
          - the code to be considered
    
          - branchSubtract: (optional) the constant that was subtracted off
            the number of neighbors before integrating it into the code.
            This is used by the topological torsions code.
    
          - includeChirality: (optional) Determines whether or not chirality
            was included when generating the atom code.
    
        >>> m = Chem.MolFromSmiles('C=CC(=O)O')
        >>> code = GetAtomCode(m.GetAtomWithIdx(0))
        >>> ExplainAtomCode(code)
        ('C', 1, 1)
        >>> code = GetAtomCode(m.GetAtomWithIdx(1))
        >>> ExplainAtomCode(code)
        ('C', 2, 1)
        >>> code = GetAtomCode(m.GetAtomWithIdx(2))
        >>> ExplainAtomCode(code)
        ('C', 3, 1)
        >>> code = GetAtomCode(m.GetAtomWithIdx(3))
        >>> ExplainAtomCode(code)
        ('O', 1, 1)
        >>> code = GetAtomCode(m.GetAtomWithIdx(4))
        >>> ExplainAtomCode(code)
        ('O', 1, 0)
    
        we can do chirality too, that returns an extra element in the tuple:
    
        >>> m = Chem.MolFromSmiles('C[C@H](F)Cl')
        >>> code = GetAtomCode(m.GetAtomWithIdx(1))
        >>> ExplainAtomCode(code)
        ('C', 3, 0)
        >>> code = GetAtomCode(m.GetAtomWithIdx(1),includeChirality=True)
        >>> ExplainAtomCode(code,includeChirality=True)
        ('C', 3, 0, 'R')
    
        note that if we don't ask for chirality, we get the right answer even if
        the atom code was calculated with chirality:
    
        >>> ExplainAtomCode(code)
        ('C', 3, 0)
    
        non-chiral atoms return '' in the 4th field:
    
        >>> code = GetAtomCode(m.GetAtomWithIdx(0),includeChirality=True)
        >>> ExplainAtomCode(code,includeChirality=True)
        ('C', 1, 0, '')
    
        Obviously switching the chirality changes the results:
    
        >>> m = Chem.MolFromSmiles('C[C@@H](F)Cl')
        >>> code = GetAtomCode(m.GetAtomWithIdx(1),includeChirality=True)
        >>> ExplainAtomCode(code,includeChirality=True)
        ('C', 3, 0, 'S')
    
        
    """
def _runDoctests(verbose = None):
    ...

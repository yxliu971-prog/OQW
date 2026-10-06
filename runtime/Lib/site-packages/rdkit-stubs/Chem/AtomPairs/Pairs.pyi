"""
 Contains an implementation of Atom-pair fingerprints, as
described in:

R.E. Carhart, D.H. Smith, R. Venkataraghavan;
"Atom Pairs as Molecular Features in Structure-Activity Studies:
Definition and Applications" JCICS 25, 64-73 (1985).

The fingerprints can be accessed through the following functions:
- GetAtomPairFingerprint
- GetHashedAtomPairFingerprint (identical to GetAtomPairFingerprint)
- GetAtomPairFingerprintAsIntVect
- GetAtomPairFingerprintAsBitVect

"""
from __future__ import annotations
from rdkit.Chem.AtomPairs import Utils
from rdkit.Chem import rdMolDescriptors
from rdkit import DataStructs
__all__: list[str] = ['DataStructs', 'ExplainPairScore', 'GetAtomPairFingerprintAsBitVect', 'Utils', 'fpLen', 'numFpBits', 'numPathBits', 'pyScorePair', 'rdMolDescriptors']
def ExplainPairScore(score, includeChirality = False):
    """
    
      >>> from rdkit import Chem
      >>> m = Chem.MolFromSmiles('C=CC')
      >>> score = pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(1), 1)
      >>> ExplainPairScore(score)
      (('C', 1, 1), 1, ('C', 2, 1))
      >>> score = pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(2), 2)
      >>> ExplainPairScore(score)
      (('C', 1, 0), 2, ('C', 1, 1))
      >>> score = pyScorePair(m.GetAtomWithIdx(1), m.GetAtomWithIdx(2), 1)
      >>> ExplainPairScore(score)
      (('C', 1, 0), 1, ('C', 2, 1))
      >>> score = pyScorePair(m.GetAtomWithIdx(2), m.GetAtomWithIdx(1), 1)
      >>> ExplainPairScore(score)
      (('C', 1, 0), 1, ('C', 2, 1))
    
      We can optionally deal with chirality too
      >>> m = Chem.MolFromSmiles('C[C@H](F)Cl')
      >>> score = pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(1), 1)
      >>> ExplainPairScore(score)
      (('C', 1, 0), 1, ('C', 3, 0))
      >>> score = pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(1), 1, includeChirality=True)
      >>> ExplainPairScore(score, includeChirality=True)
      (('C', 1, 0, ''), 1, ('C', 3, 0, 'R'))
      >>> m = Chem.MolFromSmiles('F[C@@H](Cl)[C@H](F)Cl')
      >>> score = pyScorePair(m.GetAtomWithIdx(1), m.GetAtomWithIdx(3), 1, includeChirality=True)
      >>> ExplainPairScore(score, includeChirality=True)
      (('C', 3, 0, 'R'), 1, ('C', 3, 0, 'S'))
    
      
    """
def GetAtomPairFingerprintAsBitVect(mol):
    """
     Returns the Atom-pair fingerprint for a molecule as
      a SparseBitVect. Note that this doesn't match the standard
      definition of atom pairs, which uses counts of the
      pairs, not just their presence.
    
      **Arguments**:
    
        - mol: a molecule
    
      **Returns**: a SparseBitVect
    
      >>> from rdkit import Chem
      >>> m = Chem.MolFromSmiles('CCC')
      >>> v = [pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(1), 1),
      ...      pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(2), 2),
      ...     ]
      >>> v.sort()
      >>> fp = GetAtomPairFingerprintAsBitVect(m)
      >>> list(fp.GetOnBits()) == v
      True
    
      
    """
def _runDoctests(verbose = None):
    ...
def pyScorePair(at1, at2, dist, atomCodes = None, includeChirality = False):
    """
     Returns a score for an individual atom pair.
    
      >>> from rdkit import Chem
      >>> m = Chem.MolFromSmiles('CCCCC')
      >>> c1 = Utils.GetAtomCode(m.GetAtomWithIdx(0))
      >>> c2 = Utils.GetAtomCode(m.GetAtomWithIdx(1))
      >>> c3 = Utils.GetAtomCode(m.GetAtomWithIdx(2))
      >>> t = 1 | min(c1,c2) << numPathBits | max(c1,c2) << (rdMolDescriptors.AtomPairsParameters.codeSize + numPathBits)
      >>> pyScorePair(m.GetAtomWithIdx(0), m.GetAtomWithIdx(1), 1)==t
      1
      >>> pyScorePair(m.GetAtomWithIdx(1), m.GetAtomWithIdx(0), 1)==t
      1
      >>> t = 2 | min(c1,c3) << numPathBits | max(c1,c3) << (rdMolDescriptors.AtomPairsParameters.codeSize + numPathBits)
      >>> pyScorePair(m.GetAtomWithIdx(0),m.GetAtomWithIdx(2),2)==t
      1
      >>> pyScorePair(m.GetAtomWithIdx(0),m.GetAtomWithIdx(2),2,
      ...  atomCodes=(Utils.GetAtomCode(m.GetAtomWithIdx(0)), Utils.GetAtomCode(m.GetAtomWithIdx(2)))) == t
      1
    
      
    """
_maxPathLen: int = 31
fpLen: int = 8388608
numFpBits: int = 23
numPathBits: int = 5

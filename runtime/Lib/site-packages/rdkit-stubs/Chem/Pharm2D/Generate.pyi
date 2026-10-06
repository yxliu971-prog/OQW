"""
 generation of 2D pharmacophores

**Notes**

  - The terminology for this gets a bit rocky, so here's a glossary of what
    terms used here mean:

      1) *N-point pharmacophore* a combination of N features along with
         distances between them.

      2) *N-point proto-pharmacophore*: a combination of N feature
         definitions without distances.  Each N-point
         proto-pharmacophore defines a manifold of potential N-point
         pharmacophores.

      3) *N-point scaffold*: a collection of the distances defining
         an N-point pharmacophore without feature identities.

  See Docs/Chem/Pharm2D.triangles.jpg for an illustration of the way
  pharmacophores are broken into triangles and labelled.

  See Docs/Chem/Pharm2D.signatures.jpg for an illustration of bit
  numbering

"""
from __future__ import annotations
from rdkit.Chem.Pharm2D import SigFactory
from rdkit.Chem.Pharm2D import Utils
import rdkit.RDLogger
__all__: list[str] = ['Gen2DFingerprint', 'SigFactory', 'Utils', 'logger']
def Gen2DFingerprint(mol, sigFactory, perms = None, dMat = None, bitInfo = None):
    """
     generates a 2D fingerprint for a molecule using the
       parameters in _sig_
    
       **Arguments**
    
         - mol: the molecule for which the signature should be generated
    
         - sigFactory : the SigFactory object with signature parameters
           NOTE: no preprocessing is carried out for _sigFactory_.
                 It *must* be pre-initialized.
    
         - perms: (optional) a sequence of permutation indices limiting which
           pharmacophore combinations are allowed
    
         - dMat: (optional) the distance matrix to be used
    
         - bitInfo: (optional) used to return the atoms involved in the bits
    
      
    """
def _ShortestPathsMatch(match, featureSet, sig, dMat, sigFactory):
    """
      Internal use only
    
      
    """
_verbose: int = 0
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>

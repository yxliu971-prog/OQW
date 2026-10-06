"""
 utility functionality for clustering molecules using fingerprints
 includes a command line app for clustering


Sample Usage:
  python ClusterMols.py  -d data.gdb -t daylight_sig     --idName="CAS_TF" -o clust1.pkl     --actTable="dop_test" --actName="moa_quant"

"""
from __future__ import annotations
import numpy as numpy
import pickle as pickle
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem.Fingerprints.FingerprintMols import error
from rdkit.Chem.Fingerprints.FingerprintMols import message
from rdkit.Chem.Fingerprints import MolSimilarity
from rdkit import DataStructs
from rdkit.ML.Cluster import Murtagh
__all__: list[str] = ['ClusterFromDetails', 'ClusterPoints', 'DataStructs', 'FingerprintMols', 'GetDistanceMatrix', 'MolSimilarity', 'Murtagh', 'error', 'message', 'numpy', 'pickle']
def ClusterFromDetails(details):
    """
     Returns the cluster tree
    
      
    """
def ClusterPoints(data, metric, algorithmId, haveLabels = False, haveActs = True, returnDistances = False):
    ...
def GetDistanceMatrix(data, metric, isSimilarity = 1):
    """
     data should be a list of tuples with fingerprints in position 1
       (the rest of the elements of the tuple are not important)
    
        Returns the symmetric distance matrix
        (see ML.Cluster.Resemblance for layout documentation)
    
      
    """
_usageDoc: str = "\nUsage: ClusterMols.py [args] <fName>\n\n  If <fName> is provided and no tableName is specified (see below),\n  data will be read from the text file <fName>.  Text files delimited\n  with either commas (extension .csv) or tabs (extension .txt) are\n  supported.\n\n  Command line arguments are:\n\n    - -d _dbName_: set the name of the database from which\n      to pull input fingerprint information.\n\n    - -t _tableName_: set the name of the database table\n      from which to pull input fingerprint information\n\n    - --idName=val: sets the name of the id column in the input\n      database.  Default is *ID*.\n\n    - -o _outFileName_:  name of the output file (output will\n      be a pickle (.pkl) file with the cluster tree)\n\n    - --actTable=val: name of table containing activity values\n     (used to color points in the cluster tree).\n\n    - --actName=val: name of column with activities in the activity\n      table.  The values in this column should either be integers or\n      convertible into integers.\n\n    - --SLINK: use the single-linkage clustering algorithm\n      (default is Ward's minimum variance)\n\n    - --CLINK: use the complete-linkage clustering algorithm\n      (default is Ward's minimum variance)\n\n    - --UPGMA: use the group-average clustering algorithm\n      (default is Ward's minimum variance)\n\n    - --dice: use the DICE similarity metric instead of Tanimoto\n\n    - --cosine: use the cosine similarity metric instead of Tanimoto\n\n    - --fpColName=val: name to use for the column which stores\n      fingerprints (in pickled format) in the input db table.\n      Default is *AutoFragmentFP*\n\n    - --minPath=val:  minimum path length to be included in\n      fragment-based fingerprints. Default is *2*.\n\n    - --maxPath=val:  maximum path length to be included in\n      fragment-based fingerprints. Default is *7*.\n\n    - --nBitsPerHash: number of bits to be set in the output\n      fingerprint for each fragment. Default is *4*.\n\n    - --discrim: use of path-based discriminators to hash bits.\n      Default is *false*.\n\n    - -V: include valence information in the fingerprints\n      Default is *false*.\n\n    - -H: include Hs in the fingerprint\n      Default is *false*.\n\n    - --useMACCS: use the public MACCS keys to do the fingerprinting\n      (instead of a daylight-type fingerprint)\n\n\n"

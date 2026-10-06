"""
 Interface to the C++ Murtagh hierarchic clustering code

"""
from __future__ import annotations
import numpy as numpy
from rdkit.ML.Cluster import Clusters
__all__: list[str] = ['CENTROID', 'CLINK', 'ClusterData', 'Clusters', 'GOWER', 'MCQUITTY', 'SLINK', 'UPGMA', 'WARDS', 'methods', 'numpy']
def ClusterData(data, nPts, method, isDistData = 0):
    """
      clusters the data points passed in and returns the cluster tree
    
          **Arguments**
    
            - data: a list of lists (or array, or whatever) with the input
              data (see discussion of _isDistData_ argument for the exception)
    
            - nPts: the number of points to be used
    
            - method: determines which clustering algorithm should be used.
                The defined constants for these are:
                'WARDS, SLINK, CLINK, UPGMA'
    
            - isDistData: set this toggle when the data passed in is a
                distance matrix.  The distance matrix should be stored
                symmetrically so that _LookupDist (above) can retrieve
                the results:
                  for i<j: d_ij = dists[j*(j-1)//2 + i]
    
    
          **Returns**
    
            - a single entry list with the cluster tree
        
    """
def _LookupDist(dists, i, j, n):
    """
     *Internal Use Only*
    
         returns the distance between points i and j in the symmetric
         distance matrix _dists_
    
        
    """
def _ToClusters(data, nPts, ia, ib, crit, isDistData = 0):
    """
     *Internal Use Only*
    
          Converts the results of the Murtagh clustering code into
          a cluster tree, which is returned in a single-entry list
    
        
    """
CENTROID: int = 7
CLINK: int = 3
GOWER: int = 6
MCQUITTY: int = 5
SLINK: int = 2
UPGMA: int = 4
WARDS: int = 1
methods: list = [("Ward's Minimum Variance", 1, "Ward's Minimum Variance"), ('Average Linkage', 4, 'Group Average Linkage (UPGMA)'), ('Single Linkage', 2, 'Single Linkage (SLINK)'), ('Complete Linkage', 3, 'Complete Linkage (CLINK)'), ('Centroid', 7, 'Centroid method')]

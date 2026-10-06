"""
 Implementation of the clustering algorithm published in:
  Butina JCICS 39 747-750 (1999)

"""
from __future__ import annotations
import numpy as np
__all__: list[str] = ['ClusterData', 'EuclideanDist', 'compute_distance_matrix', 'np']
def ClusterData(data, nPts, distThresh, isDistData = False, distFunc = EuclideanDist, reordering = False):
    """
      clusters the data points passed in and returns the list of clusters
    
        **Arguments**
    
          - data: a list, tuple, or numpy array of items with the input data
            (see discussion of _isDistData_ argument for the exception)
    
          - nPts: the number of points to be used
    
          - distThresh: elements within this range of each other are considered
            to be neighbors
    
          - isDistData: set this toggle when the data passed in is a
              distance matrix.  The distance matrix should be stored 
              in one of two formats: as an nxn NumPy array, or as a 
              symmetrically stored list or 1D array generated using a 
              similar process to the example below:
    
                dists = []
                for i in range(nPts):
                  for j in range(i):
                    dists.append( distfunc(i,j) )
    
          - distFunc: a function to calculate distances between points.
               Receives 2 points as arguments, should return a float
    
          - reordering: if this toggle is set, the number of neighbors is updated
               for the unassigned molecules after a new cluster is created such
               that always the molecule with the largest number of unassigned
               neighbors is selected as the next cluster center.
    
        **Returns**
    
          - a tuple of tuples containing information about the clusters:
             ( (cluster1_elem1, cluster1_elem2, ...),
               (cluster2_elem1, cluster2_elem2, ...),
               ...
             )
             The first element for each cluster is its centroid.
    
      
    """
def EuclideanDist(pi, pj):
    """
    Calculate the Euclidean distance between two points.
    """
def compute_distance_matrix(data, n_pts, dist_func):
    """
    Compute the distance matrix for the given data.
    """

from __future__ import annotations
import numpy as numpy
from rdkit.ML.Cluster import Murtagh
__all__: list[str] = ['Murtagh', 'clusters', 'd', 'dist', 'dists', 'i', 'j', 'numpy']
clusters: list  # value = [<rdkit.ML.Cluster.Clusters.Cluster object>]
d: numpy.ndarray  # value = array([[10.,  5.],...
dist: numpy.float64  # value = np.float64(650.0)
dists: numpy.ndarray  # value = array([325., 425., 200., 500., 125.,  25.,  50., 325., 625., 650.])
i: int = 4
j: int = 3

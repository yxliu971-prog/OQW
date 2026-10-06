from __future__ import annotations
from rdkit.SimDivFilters.rdSimDivPickers import ClusterMethod
from rdkit.SimDivFilters.rdSimDivPickers import HierarchicalClusterPicker
from rdkit.SimDivFilters.rdSimDivPickers import LeaderPicker
from rdkit.SimDivFilters.rdSimDivPickers import MaxMinPicker
from rdkit import rdBase
from .rdSimDivPickers import *
__all__: list[str] = ['CENTROID', 'CLINK', 'ClusterMethod', 'GOWER', 'HierarchicalClusterPicker', 'LeaderPicker', 'MCQUITTY', 'MaxMinPicker', 'SLINK', 'UPGMA', 'WARD', 'rdBase', 'rdSimDivPickers']
CENTROID: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CENTROID
CLINK: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.CLINK
GOWER: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.GOWER
MCQUITTY: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.MCQUITTY
SLINK: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.SLINK
UPGMA: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.UPGMA
WARD: rdSimDivPickers.ClusterMethod  # value = rdkit.SimDivFilters.rdSimDivPickers.ClusterMethod.WARD

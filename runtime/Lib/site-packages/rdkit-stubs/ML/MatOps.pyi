"""
 Matrix operations which may or may not come in handy some day


  **NOTE**: the two functions defined here have been moved to ML.Data.Stats

"""
from __future__ import annotations
from rdkit.ML.Data import Stats
from rdkit.ML.Data.Stats import FormCovarianceMatrix
from rdkit.ML.Data.Stats import PrincipalComponents
from rdkit.ML import files
import sys as sys
__all__: list[str] = ['FormCovarianceMatrix', 'PrincipalComponents', 'Stats', 'files', 'sys']

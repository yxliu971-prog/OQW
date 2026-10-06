"""
 Information Theory functionality

"""
from __future__ import annotations
from rdkit.ML.InfoTheory.rdInfoTheory import BitCorrMatGenerator
from rdkit.ML.InfoTheory.rdInfoTheory import InfoBitRanker
from rdkit.ML.InfoTheory.rdInfoTheory import InfoType
from .rdInfoTheory import *
__all__: list[str] = ['BIASCHISQUARE', 'BIASENTROPY', 'BitCorrMatGenerator', 'CHISQUARE', 'ENTROPY', 'InfoBitRanker', 'InfoType', 'rdInfoTheory']
BIASCHISQUARE: rdInfoTheory.InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASCHISQUARE
BIASENTROPY: rdInfoTheory.InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASENTROPY
CHISQUARE: rdInfoTheory.InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.CHISQUARE
ENTROPY: rdInfoTheory.InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.ENTROPY

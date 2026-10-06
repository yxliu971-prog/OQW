from __future__ import annotations
from rdkit.Dbase import DbConnection
from rdkit.ML.Data import Quantize
__all__: list[str] = ['DbConnection', 'Quantize', 'Usage', 'runIt']
def Usage():
    ...
def runIt(namesAndTypes, dbConnect, nBounds, resCol, typesToDo = ['float']):
    ...

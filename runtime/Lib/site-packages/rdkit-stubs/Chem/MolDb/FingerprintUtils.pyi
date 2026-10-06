from __future__ import annotations
import pickle as pickle
from rdkit import Chem
from rdkit import DataStructs
import rdkit.DataStructs.cDataStructs
import typing
__all__: list[str] = ['BuildAtomPairFP', 'BuildAvalonFP', 'BuildMorganFP', 'BuildPharm2DFP', 'BuildRDKitFP', 'BuildSigFactory', 'BuildTorsionsFP', 'Chem', 'DataStructs', 'DepickleFP', 'LayeredOptions', 'pickle', 'similarityMethods', 'supportedSimilarityMethods']
class LayeredOptions:
    fpSize: typing.ClassVar[int] = 1024
    loadLayerFlags: typing.ClassVar[int] = 4294967295
    maxPath: typing.ClassVar[int] = 6
    minPath: typing.ClassVar[int] = 1
    nWords: typing.ClassVar[int] = 32
    searchLayerFlags: typing.ClassVar[int] = 7
    wordSize: typing.ClassVar[int] = 32
    @staticmethod
    def GetFingerprint(mol, query = True):
        ...
    @staticmethod
    def GetQueryText(mol, query = True):
        ...
    @staticmethod
    def GetWords(mol, query = True):
        ...
def BuildAtomPairFP(mol):
    ...
def BuildAvalonFP(mol, smiles = None):
    ...
def BuildMorganFP(mol):
    ...
def BuildPharm2DFP(mol):
    ...
def BuildRDKitFP(mol):
    ...
def BuildSigFactory(options = None, fdefFile = None, bins = [(2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 100)], skipFeats = ('LumpedHydrophobe', 'ZnBinder')):
    ...
def BuildTorsionsFP(mol):
    ...
def DepickleFP(pkl, similarityMethod):
    ...
similarityMethods: dict = {'RDK': rdkit.DataStructs.cDataStructs.ExplicitBitVect, 'AtomPairs': rdkit.DataStructs.cDataStructs.IntSparseIntVect, 'TopologicalTorsions': rdkit.DataStructs.cDataStructs.LongSparseIntVect, 'Pharm2D': rdkit.DataStructs.cDataStructs.SparseBitVect, 'Gobbi2D': rdkit.DataStructs.cDataStructs.SparseBitVect, 'Morgan': rdkit.DataStructs.cDataStructs.UIntSparseIntVect, 'Avalon': rdkit.DataStructs.cDataStructs.ExplicitBitVect}
supportedSimilarityMethods: list = ['RDK', 'AtomPairs', 'TopologicalTorsions', 'Pharm2D', 'Gobbi2D', 'Morgan', 'Avalon']

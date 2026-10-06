from __future__ import annotations
from rdkit.Chem.FeatMaps import FeatMapPoint
from rdkit.Chem.FeatMaps import FeatMaps
from rdkit import Geometry
import re as re
__all__: list[str] = ['FeatMapParseError', 'FeatMapParser', 'FeatMapPoint', 'FeatMaps', 'Geometry', 're']
class FeatMapParseError(ValueError):
    pass
class FeatMapParser:
    data = None
    def Parse(self, featMap = None):
        ...
    def ParseFeatPointBlock(self):
        ...
    def ParseParamBlock(self):
        ...
    def SetData(self, data):
        ...
    def _NextLine(self):
        ...
    def __init__(self, file = None, data = None):
        ...
    def _parsePoint(self, txt):
        ...

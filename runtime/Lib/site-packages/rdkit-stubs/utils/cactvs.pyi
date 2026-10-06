from PIL import Image
from __future__ import annotations
import os as os
from rdkit import RDConfig
import sys as sys
import tempfile as tempfile
__all__: list[str] = ['Image', 'RDConfig', 'SmilesToGif', 'SmilesToImage', 'os', 'sys', 'tempfile']
def SmilesToGif(smiles, fileNames, size = (200, 200), cmd = None, dblSize = 0, frame = 0):
    ...
def SmilesToImage(smiles, **kwargs):
    ...

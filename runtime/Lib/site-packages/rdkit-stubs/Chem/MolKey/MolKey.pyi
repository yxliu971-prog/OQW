from __future__ import annotations
import base64 as base64
from collections import namedtuple
import hashlib as hashlib
import logging as logging
import os as os
from rdkit.Avalon import pyAvalonTools
from rdkit import Chem
from rdkit.Chem.MolKey import InchiInfo
from rdkit import RDConfig
import re as re
import tempfile as tempfile
import typing
import uuid as uuid
__all__: list[str] = ['BAD_SET', 'BadMoleculeException', 'CHIRAL_POS', 'CheckCTAB', 'Chem', 'ERROR_DICT', 'ErrorBitsToText', 'GET_STEREO_RE', 'GetInchiForCTAB', 'GetKeyForCTAB', 'INCHI_COMPUTATION_ERROR', 'INCHI_READWRITE_ERROR', 'InchiInfo', 'InchiResult', 'MOL_KEY_VERSION', 'MolIdentifierException', 'MolKeyResult', 'NULL_MOL', 'NULL_SMILES_RE', 'PATTERN_NULL_MOL', 'RDConfig', 'RDKIT_CONVERSION_ERROR', 'T_NULL_MOL', 'base64', 'hashlib', 'initStruchk', 'logging', 'namedtuple', 'os', 'pyAvalonTools', 're', 'stereo_code_dict', 'tempfile', 'uuid']
class BadMoleculeException(Exception):
    pass
class InchiResult(tuple):
    """
    InchiResult(error, inchi, fixed_ctab)
    """
    __match_args__: typing.ClassVar[tuple] = ('error', 'inchi', 'fixed_ctab')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('error', 'inchi', 'fixed_ctab')
    @staticmethod
    def __new__(_cls, error, inchi, fixed_ctab):
        """
        Create new instance of InchiResult(error, inchi, fixed_ctab)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new InchiResult object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new InchiResult object replacing specified fields with new values
        """
class MolIdentifierException(Exception):
    pass
class MolKeyResult(tuple):
    """
    MolKeyResult(mol_key, error, inchi, fixed_ctab, stereo_code, stereo_comment)
    """
    __match_args__: typing.ClassVar[tuple] = ('mol_key', 'error', 'inchi', 'fixed_ctab', 'stereo_code', 'stereo_comment')
    __slots__: typing.ClassVar[tuple] = tuple()
    _field_defaults: typing.ClassVar[dict] = {}
    _fields: typing.ClassVar[tuple] = ('mol_key', 'error', 'inchi', 'fixed_ctab', 'stereo_code', 'stereo_comment')
    @staticmethod
    def __new__(_cls, mol_key, error, inchi, fixed_ctab, stereo_code, stereo_comment):
        """
        Create new instance of MolKeyResult(mol_key, error, inchi, fixed_ctab, stereo_code, stereo_comment)
        """
    @classmethod
    def _make(cls, iterable):
        """
        Make a new MolKeyResult object from a sequence or iterable
        """
    def __getnewargs__(self):
        """
        Return self as a plain tuple.  Used by copy and pickle.
        """
    def __repr__(self):
        """
        Return a nicely formatted representation string
        """
    def _asdict(self):
        """
        Return a new dict which maps field names to their values.
        """
    def _replace(self, **kwds):
        """
        Return a new MolKeyResult object replacing specified fields with new values
        """
def CheckCTAB(ctab, isSmiles = True):
    ...
def ErrorBitsToText(err):
    """
     returns a list of error bit descriptions for the error code provided 
    """
def GetInchiForCTAB(ctab):
    """
    
        >>> from rdkit.Chem.MolKey import MolKey
        >>> from rdkit.Avalon import pyAvalonTools
        >>> res = MolKey.GetInchiForCTAB(pyAvalonTools.Generate2DCoords('c1cn[nH]c1C(Cl)Br',True))
        >>> res.inchi
        'InChI=1/C4H4BrClN2/c5-4(6)3-1-2-7-8-3/h1-2,4H,(H,7,8)/t4?/f/h8H'
        >>> res = MolKey.GetInchiForCTAB(pyAvalonTools.Generate2DCoords('c1c[nH]nc1C(Cl)Br',True))
        >>> res.inchi
        'InChI=1/C4H4BrClN2/c5-4(6)3-1-2-7-8-3/h1-2,4H,(H,7,8)/t4?/f/h7H'
        >>>
        
    """
def GetKeyForCTAB(ctab, stereo_info = None, stereo_comment = None, logger = None):
    """
    
        >>> from rdkit.Chem.MolKey import MolKey
        >>> from rdkit.Avalon import pyAvalonTools
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1ccccc1C(F)Cl', True))
        >>> res.mol_key
        '1|L7676nfGsSIU33wkx//NCg=='
        >>> res.stereo_code
        'R_ONE'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1ccccc1[C@H](F)Cl', True))
        >>> res.mol_key
        '1|Aj38EIxf13RuPDQG2A0UMw=='
        >>> res.stereo_code
        'S_ABS'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1ccccc1[C@@H](F)Cl', True))
        >>> res.mol_key
        '1|9ypfMrhxn1w0ncRooN5HXw=='
        >>> res.stereo_code
        'S_ABS'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1cccc(C(Br)Cl)c1[C@@H](F)Cl', True))
        >>> res.mol_key
        '1|c96jMSlbn7O9GW5d5uB9Mw=='
        >>> res.stereo_code
        'S_PART'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1cccc([C@H](Br)Cl)c1[C@@H](F)Cl', True))
        >>> res.mol_key
        '1|+B+GCEardrJteE8xzYdGLA=='
        >>> res.stereo_code
        'S_ABS'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1cccc(C(Br)Cl)c1C(F)Cl', True))
        >>> res.mol_key
        '1|5H9R3LvclagMXHp3Clrc/g=='
        >>> res.stereo_code
        'S_UNKN'
        >>> res = MolKey.GetKeyForCTAB(pyAvalonTools.Generate2DCoords('c1cccc(C(Br)Cl)c1C(F)Cl',True), stereo_info='S_REL')
        >>> res.mol_key
        '1|cqKWVsUEY6QNpGCbDaDTYA=='
        >>> res.stereo_code
        'S_REL'
        >>> res.inchi
        'InChI=1/C8H6BrCl2F/c9-7(10)5-3-1-2-4-6(5)8(11)12/h1-4,7-8H/t7?,8?'
    
        
    """
def _ctab_has_atoms(ctab_lines):
    """
     look at atom count position (line 4, characters 0:3)
        Return True if the count is > 0, False if 0.
        Throw BadMoleculeException if there are no characters
        at the required position or if they cannot be converted
        to a positive integer
        
    """
def _ctab_remove_chiral_flag(ctab_lines):
    """
     read the chiral flag (line 4, characters 12:15)
        and set it to 0. Return True if it was 1, False if 0.
        Throw BadMoleculeException if there are no characters
        at the required position or if they where not 0 or 1
        
    """
def _fix_all(pat, sbt, my_string):
    ...
def _fix_chemdraw_header(my_string):
    ...
def _fix_line_ends(my_string):
    ...
def _get_bad_mol_identification_string(ctab, stereo_category, extra_stereo):
    ...
def _get_chiral_identification_string(n_def, n_udf):
    ...
def _get_identification_string(err, ctab, inchi, stereo_category = None, extra_stereo = None):
    ...
def _get_null_mol_identification_string(extra_stereo):
    ...
def _identify(err, ctab, inchi, stereo_category, extra_structure_desc = None):
    """
     Compute the molecule key based on the inchi string,
        stereo category as well as extra structure
        information 
    """
def _make_racemate_inchi(inchi):
    """
     Normalize the stereo information (t-layer) to one selected isomer. 
    """
def _runDoctests(verbose = None):
    ...
def initStruchk(configDir = None, logFile = None):
    ...
BAD_SET: int = 986019
CHIRAL_POS: int = 12
ERROR_DICT: dict = {'BAD_MOLECULE': 1, 'ALIAS_CONVERSION_FAILED': 2, 'TRANSFORMED': 4, 'FRAGMENTS_FOUND': 8, 'EITHER_WARNING': 16, 'STEREO_ERROR': 32, 'DUBIOUS_STEREO_REMOVED': 64, 'ATOM_CLASH': 128, 'ATOM_CHECK_FAILED': 256, 'SIZE_CHECK_FAILED': 512, 'RECHARGED': 1024, 'STEREO_FORCED_BAD': 2048, 'STEREO_TRANSFORMED': 4096, 'TEMPLATE_TRANSFORMED': 8192, 'INCHI_COMPUTATION_ERROR': 65536, 'RDKIT_CONVERSION_ERROR': 131072, 'INCHI_READWRITE_ERROR': 262144, 'NULL_MOL': 524288}
GET_STEREO_RE: re.Pattern  # value = re.compile('^InChI=1S(.*?)/(t.*?)/m\\d/s1(.*$)')
INCHI_COMPUTATION_ERROR: int = 65536
INCHI_READWRITE_ERROR: int = 262144
MOL_KEY_VERSION: str = '1'
NULL_MOL: int = 524288
NULL_SMILES_RE: re.Pattern  # value = re.compile('^\\s*$|^\\s*NO_STRUCTURE\\s*$', re.IGNORECASE)
PATTERN_NULL_MOL: str = '^([\\s0]+[1-9]+[\\s]+V[\\w]*)'
RDKIT_CONVERSION_ERROR: int = 131072
T_NULL_MOL: tuple = (524288, '')
__initCalled: bool = False
stereo_code_dict: dict = {'DEFAULT': 0, 'S_ACHIR': 1, 'S_ABS': 2, 'S_REL': 3, 'S_PART': 4, 'S_UNKN': 5, 'S_ABS_ACHIR': 6, 'R_ONE': 11, 'R_REL': 12, 'R_OTHER': 13, 'MX_ENANT': 21, 'MX_DIAST': 22, 'MX_SP2': 31, 'MX_DIAST_ABS': 32, 'MX_DIAST_REL': 33, 'OTHER': 100, 'UNDEFINED': 200}

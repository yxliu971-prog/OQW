"""

Generate a unique hash code for a molecule based on chemistry. If two
molecules are chemically "the same", they should have the same hash.

Using molhash adds value beyond using SMILES because it:

* Ignores SMILES features that are not chemically meaningful
(e.g. atom map numbers)
* Canonicalizes enhanced stereochemistry groups. For example
`C[C@H](O)CC |&1:1|` and `C[C@@H](O)CC |&1:1|` have the same
molhash
* Canonicalizes S group data (for example, polymer data)

There are two hash schemes, the default, and one in which
tautomers are considered equivalent.

"""
from __future__ import annotations
import enum as enum
import hashlib as hashlib
import json as json
import logging as logging
from rdkit import Chem
from rdkit.Chem import rdMolHash
import rdkit.Chem.rdchem
import re as re
import typing
__all__: list[str] = ['ATOM_PROP_MAP_NUMBER', 'Chem', 'DEFAULT_CXFLAG', 'EMPTY_MOL_TAUTOMER_HASH', 'ENHANCED_STEREO_GROUP_REGEX', 'ENHANCED_STEREO_GROUP_WEIGHTS', 'EnhancedStereoUpdateMode', 'GetMolHash', 'GetMolLayers', 'GetNoStereoLayers', 'GetStereoTautomerHash', 'HashLayer', 'HashScheme', 'enum', 'hashlib', 'json', 'logger', 'logging', 'rdMolHash', 're']
class EnhancedStereoUpdateMode(enum.Enum):
    ADD_WEIGHTS: typing.ClassVar[EnhancedStereoUpdateMode]  # value = <EnhancedStereoUpdateMode.ADD_WEIGHTS: 1>
    REMOVE_WEIGHTS: typing.ClassVar[EnhancedStereoUpdateMode]  # value = <EnhancedStereoUpdateMode.REMOVE_WEIGHTS: 2>
class HashLayer(enum.Enum):
    """
    
        :cvar CANONICAL_SMILES: RDKit canonical SMILES (excluding enhanced stereo)
        :cvar ESCAPE: arbitrary other information to be incorporated
        :cvar FORMULA: a simple molecular formula for the molecule
        :cvar NO_STEREO_SMILES: RDKit canonical SMILES with all stereo removed
        :cvar SGROUP_DATA: canonicalization of all SGroups data present
        :cvar TAUTOMER_HASH: SMILES-like representation for a generic tautomer form
        :cvar NO_STEREO_TAUTOMER_HASH: the above tautomer hash lacking all stereo
        
    """
    CANONICAL_SMILES: typing.ClassVar[HashLayer]  # value = <HashLayer.CANONICAL_SMILES: 1>
    ESCAPE: typing.ClassVar[HashLayer]  # value = <HashLayer.ESCAPE: 2>
    FORMULA: typing.ClassVar[HashLayer]  # value = <HashLayer.FORMULA: 3>
    NO_STEREO_SMILES: typing.ClassVar[HashLayer]  # value = <HashLayer.NO_STEREO_SMILES: 4>
    NO_STEREO_TAUTOMER_HASH: typing.ClassVar[HashLayer]  # value = <HashLayer.NO_STEREO_TAUTOMER_HASH: 5>
    SGROUP_DATA: typing.ClassVar[HashLayer]  # value = <HashLayer.SGROUP_DATA: 6>
    TAUTOMER_HASH: typing.ClassVar[HashLayer]  # value = <HashLayer.TAUTOMER_HASH: 7>
class HashScheme(enum.Enum):
    """
    
        Which hash layers to use to when deduplicating molecules
    
        Typically the "ALL_LAYERS" scheme is used, but some users may want
        the "TAUTOMER_INSENSITIVE_LAYERS" scheme.
    
        :cvar ALL_LAYERS: most strict hash scheme utilizing all layers
        :cvar STEREO_INSENSITIVE_LAYERS: excludes stereo sensitive layers
        :cvar TAUTOMER_INSENSITIVE_LAYERS: excludes tautomer sensitive layers
        
    """
    ALL_LAYERS: typing.ClassVar[HashScheme]  # value = <HashScheme.ALL_LAYERS: (<HashLayer.CANONICAL_SMILES: 1>, <HashLayer.ESCAPE: 2>, <HashLayer.FORMULA: 3>, <HashLayer.NO_STEREO_SMILES: 4>, <HashLayer.NO_STEREO_TAUTOMER_HASH: 5>, <HashLayer.SGROUP_DATA: 6>, <HashLayer.TAUTOMER_HASH: 7>)>
    STEREO_INSENSITIVE_LAYERS: typing.ClassVar[HashScheme]  # value = <HashScheme.STEREO_INSENSITIVE_LAYERS: (<HashLayer.ESCAPE: 2>, <HashLayer.FORMULA: 3>, <HashLayer.NO_STEREO_SMILES: 4>, <HashLayer.NO_STEREO_TAUTOMER_HASH: 5>, <HashLayer.SGROUP_DATA: 6>)>
    TAUTOMER_INSENSITIVE_LAYERS: typing.ClassVar[HashScheme]  # value = <HashScheme.TAUTOMER_INSENSITIVE_LAYERS: (<HashLayer.ESCAPE: 2>, <HashLayer.FORMULA: 3>, <HashLayer.NO_STEREO_TAUTOMER_HASH: 5>, <HashLayer.SGROUP_DATA: 6>, <HashLayer.TAUTOMER_HASH: 7>)>
def GetMolHash(all_layers, hash_scheme: HashScheme = ...) -> str:
    """
    
        Generate a molecular hash using a specified set of layers.
    
        :param all_layers: a dictionary of layers
        :param hash_scheme: enum encoding information layers for the hash
        :return: hash for the given scheme constructed from the input layers
        
    """
def GetMolLayers(original_molecule: rdkit.Chem.rdchem.Mol, data_field_names: typing.Optional[typing.Iterable] = None, escape: typing.Optional[str] = None, cxflag = 1089, enable_tautomer_hash_v2 = False) -> typing.Dict[rdkit.Chem.RegistrationHash.HashLayer, str]:
    """
    
        Generate layers of data about that could be used to identify a molecule
    
        :param original_molecule: molecule to obtain canonicalization layers from
        :param data_field_names: optional sequence of names of SGroup DAT fields which
           will be included in the hash.
        :param escape: optional field which can contain arbitrary information
        :param enable_tautomer_hash_v2: use v2 of the tautomer hash
        :return: dictionary of HashLayer enum to calculated hash
        
    """
def GetNoStereoLayers(mol, enable_tautomer_hash_v2 = False):
    ...
def GetStereoTautomerHash(molecule, cxflag = 1089, enable_tautomer_hash_v2 = False):
    ...
def _CanonicalizeCOPSGroup(sg, atRanks, sortAtomAndBondOrder):
    """
    
        NOTES: if sortAtomAndBondOrder is true then the atom and bond lists will be sorted.
        This assumes that the ordering of those lists is not important
        
    """
def _CanonicalizeDataSGroup(sg, atRanks, bndOrder, fieldNames = ('Atrop'), sortAtomAndBondOrder = True):
    """
    
        NOTES: if sortAtomAndBondOrder is true then the atom and bond lists will
        be sorted. This assumes that the order of the atoms in that list is not
        important
    
        
    """
def _CanonicalizeSGroups(mol, dataFieldNames = None, sortAtomAndBondOrder = True):
    """
    
        NOTES: if sortAtomAndBondOrder is true then the atom and bond lists will be sorted.
        This assumes that the ordering of those lists is not important
        
    """
def _CanonicalizeSRUSGroup(mol, sg, atRanks, bndOrder, sortAtomAndBondOrder):
    """
    
        NOTES: if sortAtomAndBondOrder is true then the atom and bond lists will be sorted.
        This assumes that the ordering of those lists is not important
    
        
    """
def _GetCanonicalAtomRanksAndBonds(mol, useSmilesOrdering = True):
    """
    
        returns a 2-tuple with:
    
        1. the canonical ranks of a molecule's atoms
        2. the bonds expressed as (canonical_atom_rank_1,canonical_atom_rank_2) where
           canonical_atom_rank_1 < canonical_atom_rank_2
    
        If useSmilesOrdering is True then the atom indices here correspond to the order of
        the atoms in the canonical SMILES, otherwise just the canonical atom order is used.
        useSmilesOrdering=True is a bit slower, but it allows the output to be linked to the
        canonical SMILES, which can be useful.
    
        
    """
def _GetCanononicalBondRep(bond, atomRanks):
    ...
def _RemoveUnnecessaryHs(rdk_mol, preserve_stereogenic_hs = False):
    """
    
        removes hydrogens that are not necessary for the registration hash, and
        preserves hydrogen isotopes
        
    """
def _StripAtomMapLabels(mol):
    ...
ATOM_PROP_MAP_NUMBER: str = 'molAtomMapNumber'
DEFAULT_CXFLAG: int = 1089
EMPTY_MOL_TAUTOMER_HASH: str = '_0_0'
ENHANCED_STEREO_GROUP_REGEX: re.Pattern  # value = re.compile('((?:a|[&o]\\d+):\\d+(?:,\\d+)*)')
ENHANCED_STEREO_GROUP_WEIGHTS: dict  # value = {rdkit.Chem.rdchem.StereoGroupType.STEREO_AND: 1000, rdkit.Chem.rdchem.StereoGroupType.STEREO_OR: 2000, rdkit.Chem.rdchem.StereoGroupType.STEREO_ABSOLUTE: 3000}
logger: logging.Logger  # value = <Logger rdkit.Chem.RegistrationHash (WARNING)>

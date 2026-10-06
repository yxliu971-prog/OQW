from __future__ import annotations
from collections import namedtuple
from contextlib import closing
import os as os
from rdkit import Chem
from rdkit.Chem.rdmolfiles import SDMolSupplier
from rdkit.Chem.rdmolfiles import SmilesMolSupplier
from rdkit import RDConfig
import re as re
import typing
__all__: list[str] = ['Chem', 'InputFormat', 'RDConfig', 'SDMolSupplier', 'SaltRemover', 'SmilesMolSupplier', 'closing', 'namedtuple', 'os', 're']
class InputFormat:
    MOL: typing.ClassVar[str] = 'mol'
    SMARTS: typing.ClassVar[str] = 'smarts'
    SMILES: typing.ClassVar[str] = 'smiles'
class SaltRemover:
    defnFilename: typing.ClassVar[str] = 'C:/rdkit/build/temp.win-amd64-cpython-312/Release/rdkit_install\\share/RDKit\\Data\\Salts.txt'
    def StripMol(self, mol, dontRemoveEverything = False, sanitize = True):
        """
        
        
                >>> remover = SaltRemover(defnData="[Cl,Br]")
                >>> len(remover.salts)
                1
        
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl')
                >>> res = remover.StripMol(mol)
                >>> res is not None
                True
                >>> res.GetNumAtoms()
                4
        
                Notice that all salts are removed:
        
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl.Cl.Br')
                >>> res = remover.StripMol(mol)
                >>> res.GetNumAtoms()
                4
        
                Matching (e.g. "salt-like") atoms in the molecule are unchanged:
        
                >>> mol = Chem.MolFromSmiles('CN(Br)Cl')
                >>> res = remover.StripMol(mol)
                >>> res.GetNumAtoms()
                4
        
                >>> mol = Chem.MolFromSmiles('CN(Br)Cl.Cl')
                >>> res = remover.StripMol(mol)
                >>> res.GetNumAtoms()
                4
        
                Charged salts are handled reasonably:
        
                >>> mol = Chem.MolFromSmiles('C[NH+](C)(C).[Cl-]')
                >>> res = remover.StripMol(mol)
                >>> res.GetNumAtoms()
                4
        
        
                Watch out for this case (everything removed):
        
                >>> remover = SaltRemover()
                >>> len(remover.salts)>1
                True
                >>> mol = Chem.MolFromSmiles('CC(=O)O.[Na]')
                >>> res = remover.StripMol(mol)
                >>> res.GetNumAtoms()
                0
        
                dontRemoveEverything helps with this by leaving the last salt:
        
                >>> res = remover.StripMol(mol,dontRemoveEverything=True)
                >>> res.GetNumAtoms()
                4
        
                but in cases where the last salts are the same, it can't choose
                between them, so it returns all of them:
        
                >>> mol = Chem.MolFromSmiles('Cl.Cl')
                >>> res = remover.StripMol(mol,dontRemoveEverything=True)
                >>> res.GetNumAtoms()
                2
        
                
        """
    def StripMolWithDeleted(self, mol, dontRemoveEverything = False):
        """
        
                Strips given molecule and returns it, with the fragments which have been deleted.
        
                >>> remover = SaltRemover(defnData="[Cl,Br]")
                >>> len(remover.salts)
                1
        
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl.Br')
                >>> res, deleted = remover.StripMolWithDeleted(mol)
                >>> Chem.MolToSmiles(res)
                'CN(C)C'
                >>> [Chem.MolToSmarts(m) for m in deleted]
                ['[Cl,Br]']
        
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl')
                >>> res, deleted = remover.StripMolWithDeleted(mol)
                >>> res.GetNumAtoms()
                4
                >>> len(deleted)
                1
                >>> deleted[0].GetNumAtoms()
                1
                >>> Chem.MolToSmarts(deleted[0])
                '[Cl,Br]'
        
                Multiple occurrences of 'Cl' and without tuple destructuring
                
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl.Cl')
                >>> tup = remover.StripMolWithDeleted(mol)
        
                >>> tup.mol.GetNumAtoms()
                4
                >>> len(tup.deleted)
                1
                >>> tup.deleted[0].GetNumAtoms()
                1
                >>> Chem.MolToSmarts(deleted[0])
                '[Cl,Br]'
                
        """
    def _StripMol(self, mol, dontRemoveEverything = False, sanitize = True):
        ...
    def __call__(self, mol, dontRemoveEverything = False):
        """
        
        
                >>> remover = SaltRemover(defnData="[Cl,Br]")
                >>> len(remover.salts)
                1
                >>> Chem.MolToSmarts(remover.salts[0])
                '[Cl,Br]'
        
                >>> mol = Chem.MolFromSmiles('CN(C)C.Cl')
                >>> res = remover(mol)
                >>> res is not None
                True
                >>> res.GetNumAtoms()
                4
        
                
        """
    def __init__(self, defnFilename = None, defnData = None, defnFormat = 'smarts', useChirality = False):
        ...
    def _initPatterns(self):
        """
        
        
                >>> remover = SaltRemover()
                >>> len(remover.salts)>0
                True
        
                Default input format is SMARTS
                >>> remover = SaltRemover(defnData="[Cl,Br]")
                >>> len(remover.salts)
                1
        
                >>> remover = SaltRemover(defnData="[Na+]\\nCC(=O)O", defnFormat=InputFormat.SMILES)
                >>> len(remover.salts)
                2
        
                >>> from rdkit import RDLogger
                >>> RDLogger.DisableLog('rdApp.error')
                >>> remover = SaltRemover(defnData="[Cl,fail]")
                Traceback (most recent call last):
                  ...
                ValueError: [Cl,fail]
        
                >>> RDLogger.EnableLog('rdApp.error')
                
        """
def _getSmartsSaltsFromFile(filename):
    """
    
        Extracts SMARTS salts from given file object.
        
    """
def _getSmartsSaltsFromStream(stream):
    """
    
        Yields extracted SMARTS salts from given stream.
        
    """
def _runDoctests(verbose = None):
    ...
def _smartsFromSmartsLine(line):
    """
    
        Converts given line into a molecule using 'Chem.MolFromSmarts'.
        
    """

from __future__ import annotations
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Crippen
from rdkit.Chem import Descriptors
from rdkit.Chem import Lipinski
from rdkit.Dbase.DbConnection import DbConnect
from rdkit.Dbase import DbModule
import rdkit.RDLogger
from rdkit import RDLogger as logging
import re as re
__all__: list[str] = ['AllChem', 'Chem', 'ConvertRows', 'Crippen', 'DbConnect', 'DbModule', 'Descriptors', 'Lipinski', 'LoadDb', 'ProcessMol', 'logger', 'logging', 're']
def ConvertRows(rows, globalProps, defaultVal, skipSmiles):
    ...
def LoadDb(suppl, dbName, nameProp = '_Name', nameCol = 'compound_id', silent = False, redraw = False, errorsTo = None, keepHs = False, defaultVal = 'N/A', skipProps = False, regName = 'molecules', skipSmiles = False, maxRowsCached = -1, uniqNames = False, addComputedProps = False, lazySupplier = False, startAnew = True):
    ...
def ProcessMol(mol, typeConversions, globalProps, nDone, nameProp = '_Name', nameCol = 'compound_id', redraw = False, keepHs = False, skipProps = False, addComputedProps = False, skipSmiles = False, uniqNames = None, namesSeen = None):
    ...
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>

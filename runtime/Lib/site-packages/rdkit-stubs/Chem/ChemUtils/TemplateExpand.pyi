from __future__ import annotations
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.ChemUtils.AlignDepict import AlignDepict
from rdkit.Chem import Crippen
import rdkit.RDLogger
from rdkit import RDLogger as logging
import sys as sys
__all__: list[str] = ['AlignDepict', 'AllChem', 'Chem', 'ConstructSidechains', 'Crippen', 'Explode', 'MoveDummyNeighborsToBeginning', 'Usage', 'logger', 'logging', 'nDumped', 'sys']
def ConstructSidechains(suppl, sma = None, replace = True, useAll = False):
    ...
def Explode(template, sidechains, outF, autoNames = True, do3D = False, useTethers = False):
    ...
def MoveDummyNeighborsToBeginning(mol, useAll = False):
    ...
def Usage():
    ...
def _exploder(mol, depth, sidechains, core, chainIndices, autoNames = True, templateName = '', resetCounter = True, do3D = False, useTethers = False):
    ...
_greet: str = 'This is TemplateExpand version 0.8.0'
_usage: str = '\nUsage: TemplateExpand [options] template <sidechains>\n\n Unless otherwise indicated, the template and sidechains are assumed to be\n   Smiles\n\n Each sidechain entry should be:\n   [-r] SMARTS filename\n     The SMARTS pattern is used to recognize the attachment point,\n     if the -r argument is not provided, then atoms matching the pattern\n     will be removed from the sidechains.\n   or\n   -n filename\n     where the attachment atom is the first atom in each molecule\n   The filename provides the list of potential sidechains.\n\n options:\n   -o filename.sdf:      provides the name of the output file, otherwise\n                         stdout is used\n\n   --sdf :               expect the sidechains to be in SD files\n\n   --moltemplate:        the template(s) are in a mol/SD file, new depiction(s)\n                         will not be generated unless the --redraw argument is also\n                         provided\n\n   --smilesFileTemplate: extract the template(s) from a SMILES file instead of \n                         expecting SMILES on the command line.\n\n   --redraw:             generate a new depiction for the molecular template(s)\n\n   --useall:\n     or\n   --useallmatches:      generate a product for each possible match of the attachment\n                         pattern to each sidechain. If this is not provided, the first\n                         match (not canonically defined) will be used.\n\n   --force:              by default, the program prompts the user if the library is \n                         going to contain more than 1000 compounds. This argument \n                         disables the prompt.\n   \n   --templateSmarts="smarts":  provides a space-delimited list containing the SMARTS \n                               patterns to be used to recognize attachment points in\n                               the template\n             \n   --autoNames:          when set this toggle causes the resulting compounds to be named\n                         based on there sequence id in the file, e.g. \n                         "TemplateEnum: Mol_1", "TemplateEnum: Mol_2", etc.\n                         otherwise the names of the template and building blocks (from\n                         the input files) will be combined to form a name for each\n                         product molecule.\n\n   --3D :                Generate 3d coordinates for the product molecules instead of 2d coordinates,\n                         requires the --moltemplate option\n\n   --tether :            refine the 3d conformations using a tethered minimization\n\n\n'
_version: str = '0.8.0'
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>
nDumped: int = 0

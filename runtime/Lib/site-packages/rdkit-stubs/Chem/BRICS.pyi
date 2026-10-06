from __future__ import annotations
import copy as copy
from rdkit import Chem
from rdkit.Chem import rdChemReactions as Reactions
import rdkit.Chem.rdChemReactions
import rdkit.Chem.rdchem
from rdkit import RDRandom as random
import re as re
import sys as sys
__all__: list[str] = ['BRICSBuild', 'BRICSDecompose', 'BreakBRICSBonds', 'Chem', 'FindBRICSBonds', 'Reactions', 'bType', 'bnd', 'bondMatchers', 'compats', 'copy', 'defn', 'dummyPattern', 'e1', 'e2', 'env', 'environMatchers', 'environs', 'g1', 'g2', 'gp', 'i', 'i1', 'i2', 'j', 'labels', 'patt', 'ps', 'r1', 'r2', 'random', 're', 'reactionDefs', 'reactions', 'reverseReactions', 'rs', 'rxn', 'rxnSet', 'sma', 'smartsGps', 'sys', 't', 'tmp']
def BRICSBuild(fragments, onlyCompleteMols = True, seeds = None, uniquify = True, scrambleReagents = True, maxDepth = 3):
    """
     Build new molecules from BRICS fragments.
      
      
      Arguments:
        - fragments: a sequence of BRICS fragments to use for building new molecules.
        - onlyCompleteMols: if True, only molecules without attachment points will be yielded.
        - seeds: an optional list of seed molecules to use as starting points.
        - uniquify: if True, only unique molecules (determined by canonical SMILES) will be yielded.
        - scrambleReagents: if True, the order of reagents will be randomized before enumeration.
        - maxDepth: the maximum depth of the building process.
    
      Returns:
        a generator that yields the produced molecules.
    
        >>> from rdkit import Chem
        >>> frags = ['[14*]c1ccccn1', '[16*]c1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]']
        >>> frags = [Chem.MolFromSmiles(x) for x in frags]
        >>> res = BRICSBuild(frags, scrambleReagents=False)
        >>> type(res)
        <class 'generator'>
        >>> res = sorted(Chem.MolToSmiles(x) for x in res)
        >>> len(res)  
        21  
        >>> res[:3]
        ['CCCOCCC', 'CCCOCc1cccc(-c2ccccn2)c1', 'CCCOCc1ccccn1']
    
      
    """
def BRICSDecompose(mol, allNodes = None, minFragmentSize = 1, onlyUseReactions = None, silent = True, keepNonLeafNodes = False, singlePass = False, returnMols = False):
    """
     returns the BRICS decomposition for a molecule
    
        >>> from rdkit import Chem
        >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
        >>> res = list(BRICSDecompose(m))
        >>> sorted(res)
        ['[14*]c1ccccn1', '[16*]c1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]']
    
        >>> res = list(BRICSDecompose(m,returnMols=True))
        >>> res[0]
        <rdkit.Chem.rdchem.Mol object ...>
        >>> smis = [Chem.MolToSmiles(x,True) for x in res]
        >>> sorted(smis)
        ['[14*]c1ccccn1', '[16*]c1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]']
    
        nexavar, an example from the paper (corrected):
    
        >>> m = Chem.MolFromSmiles('CNC(=O)C1=NC=CC(OC2=CC=C(NC(=O)NC3=CC(=C(Cl)C=C3)C(F)(F)F)C=C2)=C1')
        >>> res = list(BRICSDecompose(m))
        >>> sorted(res)
        ['[1*]C([1*])=O', '[1*]C([6*])=O', '[14*]c1cc([16*])ccn1', '[16*]c1ccc(Cl)c([16*])c1', '[16*]c1ccc([16*])cc1', '[3*]O[3*]', '[5*]NC', '[5*]N[5*]', '[8*]C(F)(F)F']
    
        it's also possible to keep pieces that haven't been fully decomposed:
    
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True))
        >>> sorted(res)
        ['CCCOCC', '[3*]OCC', '[3*]OCCC', '[3*]O[3*]', '[4*]CC', '[4*]CCC']
    
        >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
        >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True))
        >>> sorted(res)
        ['CCCOCc1cccc(-c2ccccn2)c1', '[14*]c1ccccn1', '[16*]c1cccc(-c2ccccn2)c1', '[16*]c1cccc(COCCC)c1', '[16*]c1cccc([16*])c1', '[3*]OCCC', '[3*]OC[8*]', '[3*]OCc1cccc(-c2ccccn2)c1', '[3*]OCc1cccc([16*])c1', '[3*]O[3*]', '[4*]CCC', '[4*]C[8*]', '[4*]Cc1cccc(-c2ccccn2)c1', '[4*]Cc1cccc([16*])c1', '[8*]COCCC']
    
        or to only do a single pass of decomposition:
    
        >>> m = Chem.MolFromSmiles('CCCOCc1cc(c2ncccc2)ccc1')
        >>> res = list(BRICSDecompose(m,singlePass=True))
        >>> sorted(res)
        ['CCCOCc1cccc(-c2ccccn2)c1', '[14*]c1ccccn1', '[16*]c1cccc(-c2ccccn2)c1', '[16*]c1cccc(COCCC)c1', '[3*]OCCC', '[3*]OCc1cccc(-c2ccccn2)c1', '[4*]CCC', '[4*]Cc1cccc(-c2ccccn2)c1', '[8*]COCCC']
    
        setting a minimum size for the fragments:
    
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True,minFragmentSize=2))
        >>> sorted(res)
        ['CCCOCC', '[3*]OCC', '[3*]OCCC', '[4*]CC', '[4*]CCC']
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> res = list(BRICSDecompose(m,keepNonLeafNodes=True,minFragmentSize=3))
        >>> sorted(res)
        ['CCCOCC', '[3*]OCC', '[4*]CCC']
        >>> res = list(BRICSDecompose(m,minFragmentSize=2))
        >>> sorted(res)
        ['[3*]OCC', '[3*]OCCC', '[4*]CC', '[4*]CCC']
    
    
        
    """
def BreakBRICSBonds(mol, bonds = None, sanitize = True, silent = True):
    """
     breaks the BRICS bonds in a molecule and returns the results
    
        >>> from rdkit import Chem
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> m2=BreakBRICSBonds(m)
        >>> Chem.MolToSmiles(m2,True)
        '[3*]O[3*].[4*]CC.[4*]CCC'
    
        a more complicated case:
    
        >>> m = Chem.MolFromSmiles('CCCOCCC(=O)c1ccccc1')
        >>> m2=BreakBRICSBonds(m)
        >>> Chem.MolToSmiles(m2,True)
        '[16*]c1ccccc1.[3*]O[3*].[4*]CCC.[4*]CCC([6*])=O'
    
    
        can also specify a limited set of bonds to work with:
    
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> m2 = BreakBRICSBonds(m,[((3, 2), ('3', '4'))])
        >>> Chem.MolToSmiles(m2,True)
        '[3*]OCC.[4*]CCC'
    
        this can be used as an alternate approach for doing a BRICS decomposition by
        following BreakBRICSBonds with a call to Chem.GetMolFrags:
    
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> m2=BreakBRICSBonds(m)
        >>> frags = Chem.GetMolFrags(m2,asMols=True)
        >>> [Chem.MolToSmiles(x,True) for x in frags]
        ['[4*]CCC', '[3*]O[3*]', '[4*]CC']
    
        
    """
def FindBRICSBonds(mol, randomizeOrder = False, silent = True):
    """
     returns the bonds in a molecule that BRICS would cleave
    
        >>> from rdkit import Chem
        >>> m = Chem.MolFromSmiles('CCCOCC')
        >>> res = list(FindBRICSBonds(m))
        >>> res
        [((3, 2), ('3', '4')), ((3, 4), ('3', '4'))]
    
        a more complicated case:
    
        >>> m = Chem.MolFromSmiles('CCCOCCC(=O)c1ccccc1')
        >>> res = list(FindBRICSBonds(m))
        >>> res
        [((3, 2), ('3', '4')), ((3, 4), ('3', '4')), ((6, 8), ('6', '16'))]
    
        we can also randomize the order of the results:
    
        >>> random.seed(23)
        >>> res = list(FindBRICSBonds(m,randomizeOrder=True))
        >>> sorted(res)
        [((3, 2), ('3', '4')), ((3, 4), ('3', '4')), ((6, 8), ('6', '16'))]
    
        Note that this is a generator function :
    
        >>> res = FindBRICSBonds(m)
        >>> res
        <generator object ...>
        >>> next(res)
        ((3, 2), ('3', '4'))
    
        >>> m = Chem.MolFromSmiles('CC=CC')
        >>> res = list(FindBRICSBonds(m))
        >>> sorted(res)
        [((1, 2), ('7', '7'))]
    
        make sure we don't match ring bonds:
    
        >>> m = Chem.MolFromSmiles('O=C1NCCC1')
        >>> list(FindBRICSBonds(m))
        []
    
        another nice one, make sure environment 8 doesn't match something connected
        to a ring atom:
    
        >>> m = Chem.MolFromSmiles('CC1(C)CCCCC1')
        >>> list(FindBRICSBonds(m))
        []
    
        
    """
def _test():
    ...
bType: str = '-'
bnd: str = '-'
bondMatchers: list  # value = [[('1', '3', '-', <rdkit.Chem.rdchem.Mol object>), ('1', '5', '-', <rdkit.Chem.rdchem.Mol object>), ('1', '10', '-', <rdkit.Chem.rdchem.Mol object>)], [('3', '4', '-', <rdkit.Chem.rdchem.Mol object>), ('3', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('3', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('3', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('3', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('4', '5', '-', <rdkit.Chem.rdchem.Mol object>), ('4', '11', '-', <rdkit.Chem.rdchem.Mol object>)], [('5', '12', '-', <rdkit.Chem.rdchem.Mol object>), ('5', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('5', '16', '-', <rdkit.Chem.rdchem.Mol object>), ('5', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('5', '15', '-', <rdkit.Chem.rdchem.Mol object>)], [('6', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('6', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('6', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('6', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('7a', '7b', '=', <rdkit.Chem.rdchem.Mol object>)], [('8', '9', '-', <rdkit.Chem.rdchem.Mol object>), ('8', '10', '-', <rdkit.Chem.rdchem.Mol object>), ('8', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('8', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('8', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('8', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('9', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('9', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('9', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('9', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('10', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('10', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('10', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('10', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('11', '13', '-', <rdkit.Chem.rdchem.Mol object>), ('11', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('11', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('11', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('13', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('13', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('13', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('14', '14', '-', <rdkit.Chem.rdchem.Mol object>), ('14', '15', '-', <rdkit.Chem.rdchem.Mol object>), ('14', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('15', '16', '-', <rdkit.Chem.rdchem.Mol object>)], [('16', '16', '-', <rdkit.Chem.rdchem.Mol object>)]]
compats: list = [('16', '16', '-')]
defn: str = '[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[16*]-[*:1].[16*]-[*:2]'
dummyPattern: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
e1: str = '[c;$(c(:c):c)]'
e2: str = '[c;$(c(:c):c)]'
env: str = 'L16b'
environMatchers: dict  # value = {'L1': <rdkit.Chem.rdchem.Mol object>, 'L3': <rdkit.Chem.rdchem.Mol object>, 'L4': <rdkit.Chem.rdchem.Mol object>, 'L5': <rdkit.Chem.rdchem.Mol object>, 'L6': <rdkit.Chem.rdchem.Mol object>, 'L7a': <rdkit.Chem.rdchem.Mol object>, 'L7b': <rdkit.Chem.rdchem.Mol object>, '#L8': <rdkit.Chem.rdchem.Mol object>, 'L8': <rdkit.Chem.rdchem.Mol object>, 'L9': <rdkit.Chem.rdchem.Mol object>, 'L10': <rdkit.Chem.rdchem.Mol object>, 'L11': <rdkit.Chem.rdchem.Mol object>, 'L12': <rdkit.Chem.rdchem.Mol object>, 'L13': <rdkit.Chem.rdchem.Mol object>, 'L14': <rdkit.Chem.rdchem.Mol object>, 'L14b': <rdkit.Chem.rdchem.Mol object>, 'L15': <rdkit.Chem.rdchem.Mol object>, 'L16': <rdkit.Chem.rdchem.Mol object>, 'L16b': <rdkit.Chem.rdchem.Mol object>}
environs: dict = {'L1': '[C;D3]([#0,#6,#7,#8])(=O)', 'L3': '[O;D2]-;!@[#0,#6,#1]', 'L4': '[C;!D1;!$(C=*)]-;!@[#6]', 'L5': '[N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]', 'L6': '[C;D3;!R](=O)-;!@[#0,#6,#7,#8]', 'L7a': '[C;D2,D3]-[#6]', 'L7b': '[C;D2,D3]-[#6]', '#L8': '[C;!R;!D1]-;!@[#6]', 'L8': '[C;!R;!D1;!$(C!-*)]', 'L9': '[n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]', 'L10': '[N;R;$(N(@C(=O))@[C,N,O,S])]', 'L11': '[S;D2](-;!@[#0,#6])', 'L12': '[S;D4]([#6,#0])(=O)(=O)', 'L13': '[C;$(C(-;@[C,N,O,S])-;@[N,O,S])]', 'L14': '[c;$(c(:[c,n,o,s]):[n,o,s])]', 'L14b': '[c;$(c(:[c,n,o,s]):[n,o,s])]', 'L15': '[C;$(C(-;@C)-;@C)]', 'L16': '[c;$(c(:c):c)]', 'L16b': '[c;$(c(:c):c)]'}
g1: str = '16'
g2: str = '16'
gp: list = ['[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[16*]-[*:1].[16*]-[*:2]']
i: int = 13
i1: str = '16'
i2: str = '16'
j: int = 0
labels: list = ['16', '16']
patt: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
ps: str = '[16*]-[*:1].[16*]-[*:2]'
r1: str = '[c;$(c(:c):c)]'
r2: str = '[c;$(c(:c):c)]'
reactionDefs: tuple = ([('1', '3', '-'), ('1', '5', '-'), ('1', '10', '-')], [('3', '4', '-'), ('3', '13', '-'), ('3', '14', '-'), ('3', '15', '-'), ('3', '16', '-')], [('4', '5', '-'), ('4', '11', '-')], [('5', '12', '-'), ('5', '14', '-'), ('5', '16', '-'), ('5', '13', '-'), ('5', '15', '-')], [('6', '13', '-'), ('6', '14', '-'), ('6', '15', '-'), ('6', '16', '-')], [('7a', '7b', '=')], [('8', '9', '-'), ('8', '10', '-'), ('8', '13', '-'), ('8', '14', '-'), ('8', '15', '-'), ('8', '16', '-')], [('9', '13', '-'), ('9', '14', '-'), ('9', '15', '-'), ('9', '16', '-')], [('10', '13', '-'), ('10', '14', '-'), ('10', '15', '-'), ('10', '16', '-')], [('11', '13', '-'), ('11', '14', '-'), ('11', '15', '-'), ('11', '16', '-')], [('13', '14', '-'), ('13', '15', '-'), ('13', '16', '-')], [('14', '14', '-'), ('14', '15', '-'), ('14', '16', '-')], [('15', '16', '-')], [('16', '16', '-')])
reactions: tuple  # value = ([<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>], [<rdkit.Chem.rdChemReactions.ChemicalReaction object>])
reverseReactions: list  # value = [<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>]
rs: str = '[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]'
rxn: rdkit.Chem.rdChemReactions.ChemicalReaction  # value = <rdkit.Chem.rdChemReactions.ChemicalReaction object>
rxnSet: list = ['[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[16*]-[*:1].[16*]-[*:2]']
sma: str = '[16*]-[*:1].[16*]-[*:2]>>[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]'
smartsGps: tuple = (['[$([C;D3]([#0,#6,#7,#8])(=O)):1]-;!@[$([O;D2]-;!@[#0,#6,#1]):2]>>[1*]-[*:1].[3*]-[*:2]', '[$([C;D3]([#0,#6,#7,#8])(=O)):1]-;!@[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):2]>>[1*]-[*:1].[5*]-[*:2]', '[$([C;D3]([#0,#6,#7,#8])(=O)):1]-;!@[$([N;R;$(N(@C(=O))@[C,N,O,S])]):2]>>[1*]-[*:1].[10*]-[*:2]'], ['[$([O;D2]-;!@[#0,#6,#1]):1]-;!@[$([C;!D1;!$(C=*)]-;!@[#6]):2]>>[3*]-[*:1].[4*]-[*:2]', '[$([O;D2]-;!@[#0,#6,#1]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[3*]-[*:1].[13*]-[*:2]', '[$([O;D2]-;!@[#0,#6,#1]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[3*]-[*:1].[14*]-[*:2]', '[$([O;D2]-;!@[#0,#6,#1]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[3*]-[*:1].[15*]-[*:2]', '[$([O;D2]-;!@[#0,#6,#1]):1]-;!@[$([c;$(c(:c):c)]):2]>>[3*]-[*:1].[16*]-[*:2]'], ['[$([C;!D1;!$(C=*)]-;!@[#6]):1]-;!@[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):2]>>[4*]-[*:1].[5*]-[*:2]', '[$([C;!D1;!$(C=*)]-;!@[#6]):1]-;!@[$([S;D2](-;!@[#0,#6])):2]>>[4*]-[*:1].[11*]-[*:2]'], ['[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):1]-;!@[$([S;D4]([#6,#0])(=O)(=O)):2]>>[5*]-[*:1].[12*]-[*:2]', '[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[5*]-[*:1].[14*]-[*:2]', '[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[5*]-[*:1].[16*]-[*:2]', '[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[5*]-[*:1].[13*]-[*:2]', '[$([N;!D1;!$(N=*);!$(N-[!#6;!#16;!#0;!#1]);!$([N;R]@[C;R]=O)]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[5*]-[*:1].[15*]-[*:2]'], ['[$([C;D3;!R](=O)-;!@[#0,#6,#7,#8]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[6*]-[*:1].[13*]-[*:2]', '[$([C;D3;!R](=O)-;!@[#0,#6,#7,#8]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[6*]-[*:1].[14*]-[*:2]', '[$([C;D3;!R](=O)-;!@[#0,#6,#7,#8]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[6*]-[*:1].[15*]-[*:2]', '[$([C;D3;!R](=O)-;!@[#0,#6,#7,#8]):1]-;!@[$([c;$(c(:c):c)]):2]>>[6*]-[*:1].[16*]-[*:2]'], ['[$([C;D2,D3]-[#6]):1]=;!@[$([C;D2,D3]-[#6]):2]>>[7*]-[*:1].[7*]-[*:2]'], ['[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]):2]>>[8*]-[*:1].[9*]-[*:2]', '[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([N;R;$(N(@C(=O))@[C,N,O,S])]):2]>>[8*]-[*:1].[10*]-[*:2]', '[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[8*]-[*:1].[13*]-[*:2]', '[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[8*]-[*:1].[14*]-[*:2]', '[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[8*]-[*:1].[15*]-[*:2]', '[$([C;!R;!D1;!$(C!-*)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[8*]-[*:1].[16*]-[*:2]'], ['[$([n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[9*]-[*:1].[13*]-[*:2]', '[$([n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[9*]-[*:1].[14*]-[*:2]', '[$([n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[9*]-[*:1].[15*]-[*:2]', '[$([n;+0;$(n(:[c,n,o,s]):[c,n,o,s])]):1]-;!@[$([c;$(c(:c):c)]):2]>>[9*]-[*:1].[16*]-[*:2]'], ['[$([N;R;$(N(@C(=O))@[C,N,O,S])]):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[10*]-[*:1].[13*]-[*:2]', '[$([N;R;$(N(@C(=O))@[C,N,O,S])]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[10*]-[*:1].[14*]-[*:2]', '[$([N;R;$(N(@C(=O))@[C,N,O,S])]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[10*]-[*:1].[15*]-[*:2]', '[$([N;R;$(N(@C(=O))@[C,N,O,S])]):1]-;!@[$([c;$(c(:c):c)]):2]>>[10*]-[*:1].[16*]-[*:2]'], ['[$([S;D2](-;!@[#0,#6])):1]-;!@[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):2]>>[11*]-[*:1].[13*]-[*:2]', '[$([S;D2](-;!@[#0,#6])):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[11*]-[*:1].[14*]-[*:2]', '[$([S;D2](-;!@[#0,#6])):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[11*]-[*:1].[15*]-[*:2]', '[$([S;D2](-;!@[#0,#6])):1]-;!@[$([c;$(c(:c):c)]):2]>>[11*]-[*:1].[16*]-[*:2]'], ['[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[13*]-[*:1].[14*]-[*:2]', '[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[13*]-[*:1].[15*]-[*:2]', '[$([C;$(C(-;@[C,N,O,S])-;@[N,O,S])]):1]-;!@[$([c;$(c(:c):c)]):2]>>[13*]-[*:1].[16*]-[*:2]'], ['[$([c;$(c(:[c,n,o,s]):[n,o,s])]):1]-;!@[$([c;$(c(:[c,n,o,s]):[n,o,s])]):2]>>[14*]-[*:1].[14*]-[*:2]', '[$([c;$(c(:[c,n,o,s]):[n,o,s])]):1]-;!@[$([C;$(C(-;@C)-;@C)]):2]>>[14*]-[*:1].[15*]-[*:2]', '[$([c;$(c(:[c,n,o,s]):[n,o,s])]):1]-;!@[$([c;$(c(:c):c)]):2]>>[14*]-[*:1].[16*]-[*:2]'], ['[$([C;$(C(-;@C)-;@C)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[15*]-[*:1].[16*]-[*:2]'], ['[$([c;$(c(:c):c)]):1]-;!@[$([c;$(c(:c):c)]):2]>>[16*]-[*:1].[16*]-[*:2]'])
t: rdkit.Chem.rdChemReactions.ChemicalReaction  # value = <rdkit.Chem.rdChemReactions.ChemicalReaction object>
tmp: list  # value = [('16', '16', '-', <rdkit.Chem.rdchem.Mol object>)]

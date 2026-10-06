"""
 Implementation of the RECAP algorithm from Lewell et al. JCICS *38* 511-522 (1998)

The published algorithm is implemented more or less without
modification. The results are returned as a hierarchy of nodes instead
of just as a set of fragments. The hope is that this will allow a bit
more flexibility in working with the results.

For example:
>>> from rdkit import Chem
>>> from rdkit.Chem import Recap
>>> m = Chem.MolFromSmiles('C1CC1Oc1ccccc1-c1ncc(OC)cc1')
>>> res = Recap.RecapDecompose(m)
>>> res
<...Chem.Recap.RecapHierarchyNode object at ...>
>>> sorted(res.children.keys())
['*C1CC1', '*c1ccc(OC)cn1', '*c1ccccc1-c1ccc(OC)cn1', '*c1ccccc1OC1CC1']
>>> sorted(res.GetAllChildren().keys())
['*C1CC1', '*c1ccc(OC)cn1', '*c1ccccc1*', '*c1ccccc1-c1ccc(OC)cn1', '*c1ccccc1OC1CC1']

To get the standard set of RECAP results, use GetLeaves():
>>> leaves=res.GetLeaves()
>>> sorted(leaves.keys())
['*C1CC1', '*c1ccc(OC)cn1', '*c1ccccc1*']
>>> leaf = leaves['*C1CC1']
>>> leaf.mol
<...Chem.rdchem.Mol object at ...>


"""
from __future__ import annotations
from rdkit import Chem
from rdkit.Chem import rdChemReactions as Reactions
import sys as sys
import typing
import unittest as unittest
import weakref as weakref
__all__: list[str] = ['Chem', 'Reactions', 'RecapDecompose', 'RecapHierarchyNode', 'TestCase', 'reactionDefs', 'reactions', 'sys', 'unittest', 'weakref']
class RecapHierarchyNode:
    """
     This class is used to hold the Recap hiearchy
        
    """
    children = None
    mol = None
    parents = None
    smiles = None
    def GetAllChildren(self):
        """
         returns a dictionary, keyed by SMILES, of children 
        """
    def GetLeaves(self):
        """
         returns a dictionary, keyed by SMILES, of leaf (terminal) nodes 
        """
    def __del__(self):
        ...
    def __init__(self, mol):
        ...
    def _gacRecurse(self, res, terminalOnly = False):
        ...
    def getUltimateParents(self):
        """
         returns all the nodes in the hierarchy tree that contain this
                    node as a child
                
        """
class TestCase(unittest.case.TestCase):
    _classSetupFailed: typing.ClassVar[bool] = False
    _class_cleanups: typing.ClassVar[list] = list()
    def test1(self):
        ...
    def test2(self):
        ...
    def test3(self):
        ...
    def testAmideRxn(self):
        ...
    def testAmineRxn(self):
        ...
    def testAromCAromCRxn(self):
        ...
    def testAromNAliphCRxn(self):
        ...
    def testAromNAromCRxn(self):
        ...
    def testEsterRxn(self):
        ...
    def testEtherRxn(self):
        ...
    def testLactamNAliphCRxn(self):
        ...
    def testMinFragmentSize(self):
        ...
    def testOlefinRxn(self):
        ...
    def testSFNetIssue1801871(self):
        ...
    def testSFNetIssue1804418(self):
        ...
    def testSFNetIssue1881803(self):
        ...
    def testSulfonamideRxn(self):
        ...
    def testUreaRxn(self):
        ...
def RecapDecompose(mol, allNodes = None, minFragmentSize = 0, onlyUseReactions = None):
    """
     returns the recap decomposition for a molecule 
    """
reactionDefs: tuple = ('[#7;+0;D2,D3:1]!@C(!@=O)!@[#7;+0;D2,D3:2]>>*[#7:1].[#7:2]*', '[C;!$(C([#7])[#7]):1](=!@[O:2])!@[#7;+0;!D1:3]>>*[C:1]=[O:2].*[#7:3]', '[C:1](=!@[O:2])!@[O;+0:3]>>*[C:1]=[O:2].[O:3]*', '[N;!D1;+0;!$(N-C=[#7,#8,#15,#16])](-!@[*:1])-!@[*:2]>>*[*:1].[*:2]*', '[#7;R;D3;+0:1]-!@[*:2]>>*[#7:1].[*:2]*', '[#6:1]-!@[O;+0]-!@[#6:2]>>[#6:1]*.*[#6:2]', '[C:1]=!@[C:2]>>[C:1]*.*[C:2]', '[n;+0:1]-!@[C:2]>>[n:1]*.[C:2]*', '[O:3]=[C:4]-@[N;+0:1]-!@[C:2]>>[O:3]=[C:4]-[N:1]*.[C:2]*', '[c:1]-!@[c:2]>>[c:1]*.*[c:2]', '[n;+0:1]-!@[c:2]>>[n:1]*.*[c:2]', '[#7;+0;D2,D3:1]-!@[S:2](=[O:3])=[O:4]>>[#7:1]*.*[S:2](=[O:3])=[O:4]')
reactions: tuple  # value = (<rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>, <rdkit.Chem.rdChemReactions.ChemicalReaction object>)

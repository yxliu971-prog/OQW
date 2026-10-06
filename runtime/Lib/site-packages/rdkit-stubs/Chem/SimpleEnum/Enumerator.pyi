from __future__ import annotations
import os as os
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import rdChemReactions
from rdkit import RDConfig
__all__: list[str] = ['AllChem', 'Chem', 'EnumerateReaction', 'PreprocessReaction', 'RDConfig', 'os', 'rdChemReactions']
def EnumerateReaction(reaction, bbLists, uniqueProductsOnly = False, funcGroupFilename = 'C:/rdkit/build/temp.win-amd64-cpython-312/Release/rdkit_install\\share/RDKit\\Data\\Functional_Group_Hierarchy.txt', propName = 'molFileValue'):
    """
    
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'boronic1.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> reacts1 = ['Brc1ccccc1', 'Brc1ncccc1', 'Brc1cnccc1']
      >>> reacts1 = [Chem.MolFromSmiles(x) for x in reacts1]
      >>> reacts2 = ['CCB(O)O', 'CCCB(O)O']
      >>> reacts2 = [Chem.MolFromSmiles(x) for x in reacts2]
    
      >>> prods = EnumerateReaction(rxn, (reacts1, reacts2))
      >>> prods = list(prods)
    
      This is a bit nasty because of the symmetry of the boronic acid:
    
      >>> len(prods)
      12
    
      >>> smis = list(set([Chem.MolToSmiles(x[0]) for x in prods]))
      >>> smis.sort()
      >>> len(smis)
      6
      >>> print(smis)
      ['CCCc1ccccc1', 'CCCc1ccccn1', 'CCCc1cccnc1', 'CCc1ccccc1', 'CCc1ccccn1', 'CCc1cccnc1']
    
      The nastiness can be avoided at the cost of some memory by asking for only unique products:
    
      >>> prods = EnumerateReaction(rxn, (reacts1, reacts2), uniqueProductsOnly=True)
      >>> prods = list(prods)
      >>> len(prods)
      6
      >>> print(sorted([Chem.MolToSmiles(x[0]) for x in prods]))
      ['CCCc1ccccc1', 'CCCc1ccccn1', 'CCCc1cccnc1', 'CCc1ccccc1', 'CCc1ccccn1', 'CCc1cccnc1']
    
    
      
    """
def PreprocessReaction(reaction, funcGroupFilename = None, propName = 'molFileValue'):
    """
    
      >>> from rdkit.Chem import AllChem
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'boronic1.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> nWarn, nError, nReacts, nProds, reactantLabels = PreprocessReaction(rxn)
      >>> nWarn
      0
      >>> nError
      0
      >>> nReacts
      2
      >>> nProds
      1
      >>> reactantLabels
      (((0, 'halogen.bromine.aromatic'),), ((1, 'boronicacid'),))
    
      If there are functional group labels in the input reaction (via atoms with molFileValue
      properties), the corresponding atoms will have queries added to them so that they only
      match such things. We can see this here:
    
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> r1 = rxn.GetReactantTemplate(0)
      >>> m1 = Chem.MolFromSmiles('CCBr')
      >>> m2 = Chem.MolFromSmiles('c1ccccc1Br')
    
      These both match because the reaction file itself just has R1-Br:
    
      >>> m1.HasSubstructMatch(r1)
      True
      >>> m2.HasSubstructMatch(r1)
      True
    
      After preprocessing, we only match the aromatic Br:
    
      >>> d = PreprocessReaction(rxn)
      >>> m1.HasSubstructMatch(r1)
      False
      >>> m2.HasSubstructMatch(r1)
      True
    
      We also support or queries in the values field (separated by commas):
    
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'azide_reaction.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> reactantLabels = PreprocessReaction(rxn)[-1]
      >>> reactantLabels
      (((1, 'azide'),), ((1, 'carboxylicacid,acidchloride'),))
      >>> m1 = Chem.MolFromSmiles('CC(=O)O')
      >>> m2 = Chem.MolFromSmiles('CC(=O)Cl')
      >>> m3 = Chem.MolFromSmiles('CC(=O)N')
      >>> r2 = rxn.GetReactantTemplate(1)
      >>> m1.HasSubstructMatch(r2)
      True
      >>> m2.HasSubstructMatch(r2)
      True
      >>> m3.HasSubstructMatch(r2)
      False
    
      unrecognized final group types are returned as None:
    
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'bad_value1.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
      Traceback (most recent call last):
        File "/usr/prog/python/2.6.6_gnu/lib/python2.6/doctest.py", line 1253, in __run
          compileflags, 1) in test.globs
        File "<doctest __main__.PreprocessReaction[36]>", line 1, in <module>
          nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
        File "Enumerator.py", line 105, in PreprocessReaction
          reactantLabels = reaction.AddRecursiveQueriesToReaction(queryDict, propName='molFileValue', getLabels=True)
      KeyError: 'boromicacid'
    
      One unrecognized group type in a comma-separated list makes the whole thing fail:
    
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'bad_value2.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
      Traceback (most recent call last):
        File "/usr/prog/python/2.6.6_gnu/lib/python2.6/doctest.py", line 1253, in __run
          compileflags, 1) in test.globs
        File "<doctest __main__.PreprocessReaction[36]>", line 1, in <module>
          nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
        File "Enumerator.py", line 105, in PreprocessReaction
          reactantLabels = reaction.AddRecursiveQueriesToReaction(queryDict, propName='molFileValue', getLabels=True)
      KeyError: 'carboxylicacid,acidchlroide'
      >>> testFile = os.path.join(RDConfig.RDCodeDir, 'Chem', 'SimpleEnum', 'test_data', 'bad_value3.rxn')
      >>> rxn = AllChem.ReactionFromRxnFile(testFile)
      >>> rxn.Initialize()
      >>> nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
      Traceback (most recent call last):
        File "/usr/prog/python/2.6.6_gnu/lib/python2.6/doctest.py", line 1253, in __run
          compileflags, 1) in test.globs
        File "<doctest __main__.PreprocessReaction[36]>", line 1, in <module>
          nWarn,nError,nReacts,nProds,reactantLabels = PreprocessReaction(rxn)
        File "Enumerator.py", line 105, in PreprocessReaction
          reactantLabels = reaction.AddRecursiveQueriesToReaction(queryDict, propName='molFileValue', getLabels=True)
      KeyError: 'carboxyliccaid,acidchloride'
      >>> rxn = rdChemReactions.ChemicalReaction()
      >>> rxn.Initialize()
      >>> nWarn, nError, nReacts, nProds, reactantLabels = PreprocessReaction(rxn)
      >>> reactantLabels
      ()
      >>> reactantLabels == ()
      True
      
    """
def _runDoctests(verbose = None):
    ...

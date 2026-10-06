"""
  command line utility for working with FragmentCatalogs (CASE-type analysis)

**Usage**

  BuildFragmentCatalog [optional args] <filename>

 filename, the name of a delimited text file containing InData, is required
 for some modes of operation (see below)

**Command Line Arguments**

 - -n *maxNumMols*:  specify the maximum number of molecules to be processed

 - -b: build the catalog and OnBitLists
    *requires InData*

 - -s: score compounds
    *requires InData and a Catalog, can use OnBitLists*

 - -g: calculate info gains
    *requires Scores*

 - -d: show details about high-ranking fragments
    *requires a Catalog and Gains*

 - --catalog=*filename*: filename with the pickled catalog.
    If -b is provided, this file will be overwritten.

 - --onbits=*filename*: filename to hold the pickled OnBitLists.
   If -b is provided, this file will be overwritten

 - --scores=*filename*: filename to hold the text score data.
   If -s is provided, this file will be overwritten

 - --gains=*filename*: filename to hold the text gains data.
   If -g is provided, this file will be overwritten

 - --details=*filename*: filename to hold the text details data.
   If -d is provided, this file will be overwritten.

 - --minPath=2: specify the minimum length for a path

 - --maxPath=6: specify the maximum length for a path

 - --smiCol=1: specify which column in the input data file contains
     SMILES

 - --actCol=-1: specify which column in the input data file contains
     activities

 - --nActs=2: specify the number of possible activity values

 - --nBits=-1: specify the maximum number of bits to show details for

"""
from __future__ import annotations
import numpy as numpy
import os as os
import pickle as pickle
from rdkit.Chem import FragmentCatalog
from rdkit.Dbase.DbConnection import DbConnect
from rdkit.ML import InfoTheory
from rdkit import RDConfig
import sys as sys
import typing
__all__: list[str] = ['BuildCatalog', 'CalcGains', 'CalcGainsFromFps', 'DbConnect', 'FragmentCatalog', 'InfoTheory', 'OutputGainsData', 'ParseArgs', 'ProcessGainsData', 'RDConfig', 'RunDetails', 'ScoreFromLists', 'ScoreMolecules', 'ShowDetails', 'SupplierFromDetails', 'Usage', 'message', 'numpy', 'os', 'pickle', 'sys']
class RunDetails:
    actCol: typing.ClassVar[int] = -1
    biasList = None
    catalogName = None
    dbName: typing.ClassVar[str] = ''
    delim: typing.ClassVar[str] = ','
    detailsName = None
    doBuild: typing.ClassVar[int] = 0
    doDetails: typing.ClassVar[int] = 0
    doGains: typing.ClassVar[int] = 0
    doScore: typing.ClassVar[int] = 0
    doSigs: typing.ClassVar[int] = 0
    fpName = None
    gainsName = None
    hasTitle: typing.ClassVar[int] = 1
    inFileName = None
    maxPath: typing.ClassVar[int] = 6
    minPath: typing.ClassVar[int] = 2
    nActs: typing.ClassVar[int] = 2
    nBits: typing.ClassVar[int] = -1
    nameCol: typing.ClassVar[int] = -1
    numMols: typing.ClassVar[int] = -1
    onBitsName = None
    scoresName = None
    smiCol: typing.ClassVar[int] = 1
    tableName = None
    topN: typing.ClassVar[int] = -1
def BuildCatalog(suppl, maxPts = -1, groupFileName = None, minPath = 2, maxPath = 6, reportFreq = 10):
    """
     builds a fragment catalog from a set of molecules in a delimited text block
    
          **Arguments**
    
            - suppl: a mol supplier
    
            - maxPts: (optional) if provided, this will set an upper bound on the
              number of points to be considered
    
            - groupFileName: (optional) name of the file containing functional group
              information
    
            - minPath, maxPath: (optional) names of the minimum and maximum path lengths
              to be considered
    
            - reportFreq: (optional) how often to display status information
    
          **Returns**
    
            a FragmentCatalog
    
        
    """
def CalcGains(suppl, catalog, topN = -1, actName = '', acts = None, nActs = 2, reportFreq = 10, biasList = None, collectFps = 0):
    """
     calculates info gains by constructing fingerprints
          *DOC*
    
          Returns a 2-tuple:
             1) gains matrix
             2) list of fingerprints
    
        
    """
def CalcGainsFromFps(suppl, fps, topN = -1, actName = '', acts = None, nActs = 2, reportFreq = 10, biasList = None):
    """
     calculates info gains from a set of fingerprints
    
          *DOC*
    
        
    """
def OutputGainsData(outF, gains, cat, nActs = 2):
    ...
def ParseArgs(details):
    ...
def ProcessGainsData(inF, delim = ',', idCol = 0, gainCol = 1):
    """
     reads a list of ids and info gains out of an input file
    
        
    """
def ScoreFromLists(bitLists, suppl, catalog, maxPts = -1, actName = '', acts = None, nActs = 2, reportFreq = 10):
    """
      similar to _ScoreMolecules()_, but uses pre-calculated bit lists
          for the molecules (this speeds things up a lot)
    
    
          **Arguments**
    
            - bitLists: sequence of on bit sequences for the input molecules
    
            - suppl: the input supplier (we read activities from here)
    
            - catalog: the FragmentCatalog
    
            - maxPts: (optional) the maximum number of molecules to be
              considered
    
            - actName: (optional) the name of the molecule's activity property.
              If this is not provided, the molecule's last property will be used.
    
            - nActs: (optional) number of possible activity values
    
            - reportFreq: (optional) how often to display status information
    
          **Returns**
    
             the results table (a 3D array of ints nBits x 2 x nActs)
    
        
    """
def ScoreMolecules(suppl, catalog, maxPts = -1, actName = '', acts = None, nActs = 2, reportFreq = 10):
    """
     scores the compounds in a supplier using a catalog
    
          **Arguments**
    
            - suppl: a mol supplier
    
            - catalog: the FragmentCatalog
    
            - maxPts: (optional) the maximum number of molecules to be
              considered
    
            - actName: (optional) the name of the molecule's activity property.
              If this is not provided, the molecule's last property will be used.
    
            - acts: (optional) a sequence of activity values (integers).
              If not provided, the activities will be read from the molecules.
    
            - nActs: (optional) number of possible activity values
    
            - reportFreq: (optional) how often to display status information
    
          **Returns**
    
            a 2-tuple:
    
              1) the results table (a 3D array of ints nBits x 2 x nActs)
    
              2) a list containing the on bit lists for each molecule
    
        
    """
def ShowDetails(catalog, gains, nToDo = -1, outF = ..., idCol = 0, gainCol = 1, outDelim = ','):
    """
    
         gains should be a sequence of sequences.  The idCol entry of each
         sub-sequence should be a catalog ID.  _ProcessGainsData()_ provides
         suitable input.
    
        
    """
def SupplierFromDetails(details):
    ...
def Usage():
    ...
def message(msg, dest = ...):
    ...

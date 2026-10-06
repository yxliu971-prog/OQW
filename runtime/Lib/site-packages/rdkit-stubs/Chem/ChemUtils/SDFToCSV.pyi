from __future__ import annotations
import argparse as argparse
import csv as csv
import os as os
from rdkit import Chem
import sys as sys
__all__: list[str] = ['Chem', 'Convert', 'argparse', 'csv', 'existingFile', 'initParser', 'main', 'os', 'sys']
def Convert(suppl, outFile, keyCol = None, stopAfter = -1, includeChirality = False, smilesFrom = ''):
    ...
def existingFile(filename):
    """
     'type' for argparse - check that filename exists 
    """
def initParser():
    """
     Initialize the parser for the CLI 
    """
def main():
    """
     Main application 
    """

"""
 The "parser" for compound descriptors.

I almost hesitate to document this, because it's not the prettiest
thing the world has ever seen... but it does work (for at least some
definitions of the word).

Rather than getting into the whole mess of writing a parser for the
compound descriptor expressions, I'm just using string substitutions
and python's wonderful ability to *eval* code.

It would probably be a good idea at some point to replace this with a
real parser, if only for the flexibility and intelligent error
messages that would become possible.

The general idea is that we're going to deal with expressions where
atomic descriptors have some kind of method applied to them which
reduces them to a single number for the entire composition.  Compound
descriptors (those applicable to the compound as a whole) are not
operated on by anything in particular (except for standard math stuff).

Here's the general flow of things:

  1) Composition descriptor references ($a, $b, etc.) are replaced with the
     corresponding descriptor names using string substitution.
     (*_SubForCompoundDescriptors*)

  2) Atomic descriptor references ($1, $2, etc) are replaced with lookups
     into the atomic dict with "DEADBEEF" in place of the atom name.
     (*_SubForAtomicVars*)

  3) Calls to Calculator Functions are augmented with a reference to
     the composition and atomic dictionary
     (*_SubMethodArgs*)

**NOTE:**

  anytime we don't know the answer for a descriptor, rather than
  throwing a (completely incomprehensible) exception, we just return
  -666.  So bad descriptor values should stand out like sore thumbs.

"""
from __future__ import annotations
from math import acos
from math import acosh
from math import asin
from math import asinh
from math import atan
from math import atan2
from math import atanh
from math import cbrt
from math import ceil
from math import comb
from math import copysign
from math import cos
from math import cosh
from math import degrees
from math import dist
from math import erf
from math import erfc
from math import exp
from math import exp2
from math import expm1
from math import fabs
from math import factorial
from math import floor
from math import fmod
from math import frexp
from math import fsum
from math import gamma
from math import gcd
from math import hypot
from math import isclose
from math import isfinite
from math import isinf
from math import isnan
from math import isqrt
from math import lcm
from math import ldexp
from math import lgamma
from math import log
from math import log10
from math import log1p
from math import log2
from math import modf
from math import nextafter
from math import perm
from math import pow
from math import prod
from math import radians
from math import remainder
from math import sin
from math import sinh
from math import sqrt
from math import sumprod
from math import tan
from math import tanh
from math import trunc
from math import ulp
from rdkit import RDConfig
__all__: list[str] = ['AVG', 'CalcMultipleCompoundsDescriptor', 'CalcSingleCompoundDescriptor', 'DEV', 'HAS', 'MAX', 'MEAN', 'MIN', 'RDConfig', 'SUM', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'knownMethods', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
def CalcMultipleCompoundsDescriptor(composVect, argVect, atomDict, propDictList):
    """
     calculates the value of the descriptor for a list of compounds
    
        **ARGUMENTS:**
    
          - composVect: a vector of vector/tuple containing the composition
             information.
             See _CalcSingleCompoundDescriptor()_ for an explanation of the elements.
    
          - argVect: a vector/tuple with three elements:
    
               1) AtomicDescriptorNames:  a list/tuple of the names of the
                 atomic descriptors being used. These determine the
                 meaning of $1, $2, etc. in the expression
    
               2) CompoundDsscriptorNames:  a list/tuple of the names of the
                 compound descriptors being used. These determine the
                 meaning of $a, $b, etc. in the expression
    
               3) Expr: a string containing the expression to be used to
                 evaluate the final result.
    
          - atomDict:
               a dictionary of atomic descriptors.  Each atomic entry is
               another dictionary containing the individual descriptors
               and their values
    
          - propVectList:
             a vector of vectors of descriptors for the composition.
    
        **RETURNS:**
    
          a vector containing the values of the descriptor for each
          compound.  Any given entry will be -666 if problems were
          encountered
    
      
    """
def CalcSingleCompoundDescriptor(compos, argVect, atomDict, propDict):
    """
     calculates the value of the descriptor for a single compound
    
        **ARGUMENTS:**
    
          - compos: a vector/tuple containing the composition
             information... in the form:
             '[("Fe",1.),("Pt",2.),("Rh",0.02)]'
    
          - argVect: a vector/tuple with three elements:
    
               1) AtomicDescriptorNames:  a list/tuple of the names of the
                 atomic descriptors being used. These determine the
                 meaning of $1, $2, etc. in the expression
    
               2) CompoundDescriptorNames:  a list/tuple of the names of the
                 compound descriptors being used. These determine the
                 meaning of $a, $b, etc. in the expression
    
               3) Expr: a string containing the expression to be used to
                 evaluate the final result.
    
          - atomDict:
               a dictionary of atomic descriptors.  Each atomic entry is
               another dictionary containing the individual descriptors
               and their values
    
          - propVect:
               a list of descriptors for the composition.
    
        **RETURNS:**
    
          the value of the descriptor, -666 if a problem was encountered
    
        **NOTE:**
    
          - because it takes rather a lot of work to get everything set
              up to calculate a descriptor, if you are calculating the
              same descriptor for multiple compounds, you probably want to
              be calling _CalcMultipleCompoundsDescriptor()_.
    
      
    """
def DEV(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        calculates the average deviation of a descriptor across a composition
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - compos: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          a float
    
      
    """
def HAS(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        does a string search
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - composList: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          1 or 0
    
      
    """
def MAX(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        calculates the maximum value of a descriptor across a composition
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - compos: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          a float
    
      
    """
def MEAN(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        calculates the average of a descriptor across a composition
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - compos: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          a float
    
      
    """
def MIN(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        calculates the minimum value of a descriptor across a composition
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - compos: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          a float
    
      
    """
def SUM(strArg, composList, atomDict):
    """
     *Calculator Method*
    
        calculates the sum of a descriptor across a composition
    
        **Arguments**
    
          - strArg: the arguments in string form
    
          - compos: the composition vector
    
          - atomDict: the atomic dictionary
    
        **Returns**
    
          a float
    
      
    """
def _SubForAtomicVars(cExpr, varList, dictName):
    """
     replace atomic variables with the appropriate dictionary lookup
    
       *Not intended for client use*
    
      
    """
def _SubForCompoundDescriptors(cExpr, varList, dictName):
    """
     replace compound variables with the appropriate list index
    
       *Not intended for client use*
    
      
    """
def _SubMethodArgs(cExpr, knownMethods):
    """
     alters the arguments of calls to calculator methods
    
      *Not intended for client use*
    
      This is kind of putrid (and the code ain't so pretty either)
      The general idea is that the various special methods for atomic
      descriptors need two extra arguments (the composition and the atomic
      dict).  Rather than make the user type those in, we just find
      invocations of these methods and fill out the function calls using
      string replacements.
      
    """
def _exampleCode():
    ...
__DEBUG: bool = False
e: float = 2.718281828459045
inf: float  # value = inf
knownMethods: list = ['SUM', 'MIN', 'MAX', 'MEAN', 'AVG', 'DEV', 'HAS']
nan: float  # value = nan
pi: float = 3.141592653589793
tau: float = 6.283185307179586
AVG = MEAN

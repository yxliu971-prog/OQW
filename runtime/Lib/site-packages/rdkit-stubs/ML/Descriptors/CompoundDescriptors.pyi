"""
 descriptor calculator for compounds defined by a composition alone
  (only the composition is required)

"""
from __future__ import annotations
from rdkit.ML.Descriptors import Descriptors
import rdkit.ML.Descriptors.Descriptors
from rdkit.ML.Descriptors import Parser
from rdkit import RDConfig
from rdkit.utils import chemutils
__all__: list[str] = ['CompoundDescriptorCalculator', 'Descriptors', 'GetAllDescriptorNames', 'Parser', 'RDConfig', 'chemutils', 'countOptions']
class CompoundDescriptorCalculator(rdkit.ML.Descriptors.Descriptors.DescriptorCalculator):
    """
     used for calculating descriptors
    
       This is the central point for descriptor calculation
    
       **Notes**
    
       - There are two kinds of descriptors this cares about:
    
          1) *Simple Descriptors* can be calculated solely using atomic descriptor
             values and the composition of the compound.  The full list of possible
             simple descriptors is determined by the types of *Calculator Methods*
             (see below) and the contents of an atomic database.
    
             Simple Descriptors can be marked as *nonZeroDescriptors*.  These are used
             to winnow out atom types where particular atomic descriptors are zero
             (usually indicating that the value is unknown)
    
             Simple Descriptors are maintained locally in the _simpleList_
    
          2) *Compound Descriptors* may rely upon more complicated computation schemes
             and descriptors for the compound as a whole (e.g. structural variables, etc.).
             The full list of compound descriptors is limitless.  They are calculated using
             the _ML.Descriptors.Parser_ module.
    
             Compound Descriptors are maintained locally in the _compoundList_
    
       - This class has a some special methods which are labelled as *Calculator Method*
         These are used internally to take atomic descriptors and reduce them to a single
         simple descriptor value for a composition.  They are primarily intended for internal use.
    
       - a *composition vector* is a list of 2-tuples: '[(atom1name,atom1Num),...]'
         where atom1Num is the contribution of the atom to the stoichiometry of the
         compound. No assumption is made about the stoichiometries (i.e. they don't
         have to be either integral or all sum to one).
    
      
    """
    def BuildAtomDict(self):
        """
         builds the local atomic dict
        
             We don't want to keep around all descriptor values for all atoms, so this
             method takes care of only pulling out the descriptors in which we are
             interested.
        
             **Notes**
        
               - this uses _chemutils.GetAtomicData_ to actually pull the data
        
            
        """
    def CalcCompoundDescriptorsForComposition(self, compos = '', composList = None, propDict = {}):
        """
         calculates all simple descriptors for a given composition
        
              **Arguments**
        
                - compos: a string representation of the composition
        
                - composList: a *composVect*
        
                - propDict: a dictionary containing the properties of the composition
                  as a whole (e.g. structural variables, etc.)
        
                The client must provide either _compos_ or _composList_.  If both are
                provided, _composList_ takes priority.
        
              **Returns**
                the list of descriptor values
        
              **Notes**
        
                - when _compos_ is provided, this uses _chemutils.SplitComposition_
                  to split the composition into its individual pieces
        
            
        """
    def CalcDescriptors(self, composVect, propDict):
        """
         calculates all descriptors for a given composition
        
              **Arguments**
        
                - compos: a string representation of the composition
        
                - propDict: a dictionary containing the properties of the composition
                  as a whole (e.g. structural variables, etc.). These are used to
                  generate Compound Descriptors
        
              **Returns**
                the list of all descriptor values
        
              **Notes**
        
                - this uses _chemutils.SplitComposition_
                  to split the composition into its individual pieces
        
            
        """
    def CalcDescriptorsForComposition(self, composVect, propDict):
        """
         calculates all descriptors for a given composition
        
              **Arguments**
        
                - compos: a string representation of the composition
        
                - propDict: a dictionary containing the properties of the composition
                  as a whole (e.g. structural variables, etc.). These are used to
                  generate Compound Descriptors
        
              **Returns**
                the list of all descriptor values
        
              **Notes**
        
                - this uses _chemutils.SplitComposition_
                  to split the composition into its individual pieces
        
            
        """
    def CalcSimpleDescriptorsForComposition(self, compos = '', composList = None):
        """
         calculates all simple descriptors for a given composition
        
              **Arguments**
        
                - compos: a string representation of the composition
        
                - composList: a *composVect*
        
                The client must provide either _compos_ or _composList_.  If both are
                provided, _composList_ takes priority.
        
              **Returns**
                the list of descriptor values
        
              **Notes**
        
                - when _compos_ is provided, this uses _chemutils.SplitComposition_
                  to split the composition into its individual pieces
        
                - if problems are encountered because of either an unknown descriptor or
                  atom type, a _KeyError_ will be raised.
        
            
        """
    def DEV(self, desc, compos):
        """
         *Calculator Method*
        
              average deviation of the descriptor values across the composition
        
              **Arguments**
        
                - desc: the name of the descriptor
        
                - compos: the composition vector
        
              **Returns**
        
                a float
        
            
        """
    def GetDescriptorNames(self):
        """
         returns a list of the names of the descriptors this calculator generates
        
            
        """
    def MAX(self, desc, compos):
        """
         *Calculator Method*
        
              maximum of the descriptor values across the composition
        
              **Arguments**
        
                - desc: the name of the descriptor
        
                - compos: the composition vector
        
              **Returns**
        
                a float
        
            
        """
    def MEAN(self, desc, compos):
        """
         *Calculator Method*
        
              averages the descriptor values across the composition
        
              **Arguments**
        
                - desc: the name of the descriptor
        
                - compos: the composition vector
        
              **Returns**
        
                a float
        
            
        """
    def MIN(self, desc, compos):
        """
         *Calculator Method*
        
              minimum of the descriptor values across the composition
        
              **Arguments**
        
                - desc: the name of the descriptor
        
                - compos: the composition vector
        
              **Returns**
        
                a float
        
            
        """
    def ProcessCompoundList(self):
        """
         Adds entries from the _compoundList_ to the list of _requiredDescriptors_
        
              Each compound descriptor is surveyed.  Any atomic descriptors it requires
              are added to the list of _requiredDescriptors_ to be pulled from the database.
        
            
        """
    def ProcessSimpleList(self):
        """
         Handles the list of simple descriptors
        
              This constructs the list of _nonZeroDescriptors_ and _requiredDescriptors_.
        
              There's some other magic going on that I can't decipher at the moment.
        
            
        """
    def SUM(self, desc, compos):
        """
         *Calculator Method*
        
              sums the descriptor values across the composition
        
              **Arguments**
        
                - desc: the name of the descriptor
        
                - compos: the composition vector
        
              **Returns**
        
                a float
        
            
        """
    def __init__(self, simpleList, compoundList = None, dbName = None, dbTable = 'atomic_data', dbUser = 'sysdba', dbPassword = 'masterkey'):
        """
         Constructor
        
              **Arguments**
        
                - simpleList: list of simple descriptors to be calculated
                      (see below for format)
        
                - compoundList: list of compound descriptors to be calculated
                      (see below for format)
        
                - dbName: name of the atomic database to be used
        
                - dbTable: name the table in _dbName_ which has atomic data
        
                - dbUser: user name for DB access
        
                - dbPassword: password for DB access
        
              **Note**
        
                - format of simpleList:
                   a list of 2-tuples containing:
        
                      1) name of the atomic descriptor
        
                      2) a list of operations on that descriptor (e.g. NonZero, Max, etc.)
                         These must correspond to the *Calculator Method* names above.
        
                - format of compoundList:
                   a list of 2-tuples containing:
        
                      1) name of the descriptor to be calculated
        
                      2) list of selected atomic descriptor names (define $1, $2, etc.)
        
                      3) list of selected compound descriptor names (define $a, $b, etc.)
        
                      4) text formula defining the calculation (see _Parser_)
        
            
        """
def GetAllDescriptorNames(db, tbl1, tbl2, user = 'sysdba', password = 'masterkey'):
    """
     gets possible descriptor names from a database
    
        **Arguments**
    
          - db: the name of the database to use
    
          - tbl1: the name of the table to be used for reading descriptor values
    
          - tbl2: the name of the table to be used for reading notes about the
            descriptors (*descriptions of the descriptors if you like*)
    
          - user: the user name for DB access
    
          - password: the password for DB access
    
        **Returns**
    
          a 2-tuple containing:
    
            1) a list of column names
    
            2) a list of column descriptors
    
        **Notes**
    
          - this uses _Dbase.DbInfo_  and Dfunctionality for querying the database
    
          - it is assumed that tbl2 includes 'property' and 'notes' columns
    
      
    """
def _exampleCode():
    ...
countOptions: list = [('NVAL', 'total number of valence electrons'), ('NVAL_NO_FULL_F', 'number of valence electrons neglecting filled f shells'), ('NVAL_NO_FULL_D', 'number of valence electrons neglecting filled d shells'), ('NVAL_NO_FULL', 'number of valence electrons neglecting filled f and d shells')]

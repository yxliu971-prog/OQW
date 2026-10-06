"""
Module containing functionality from the Avalon toolkit.

The functions currently exposed are:
  - GetCanonSmiles()   : return the canonical smiles for a molecule
  - GetAvalonFP()      : return the Avalon fingerprint for a molecule as
                         an RDKit ExplicitBitVector
  - GetAvalonCountFP()      : return the Avalon fingerprint for a molecule as
                              an RDKit SparseIntVector
  - Generate2DCoords() : use the Avalon coordinate generator to create
                         a set of 2D coordinates for a molecule
Each function can be called with either an RDKit molecule or some
molecule data as text (e.g. a SMILES or an MDL mol block).

See the individual docstrings for more information.
"""
from __future__ import annotations
import typing
__all__: list[str] = ['CheckMolecule', 'CheckMoleculeString', 'CloseCheckMolFiles', 'Generate2DCoords', 'GetAvalonCountFP', 'GetAvalonFP', 'GetAvalonFPAsWords', 'GetCanonSmiles', 'GetCheckMolLog', 'InitializeCheckMol', 'StruChkFlag', 'StruChkResult', 'avalonSSSBits', 'avalonSimilarityBits']
class StruChkFlag(Boost.Python.enum):
    __slots__: typing.ClassVar[tuple] = tuple()
    alias_conversion_failed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.alias_conversion_failed
    atom_check_failed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_check_failed
    atom_clash: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_clash
    bad_molecule: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.bad_molecule
    dubious_stereo_removed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.dubious_stereo_removed
    either_warning: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.either_warning
    fragments_found: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.fragments_found
    names: typing.ClassVar[dict]  # value = {'bad_molecule': rdkit.Avalon.pyAvalonTools.StruChkFlag.bad_molecule, 'alias_conversion_failed': rdkit.Avalon.pyAvalonTools.StruChkFlag.alias_conversion_failed, 'transformed': rdkit.Avalon.pyAvalonTools.StruChkFlag.transformed, 'fragments_found': rdkit.Avalon.pyAvalonTools.StruChkFlag.fragments_found, 'either_warning': rdkit.Avalon.pyAvalonTools.StruChkFlag.either_warning, 'stereo_error': rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_error, 'dubious_stereo_removed': rdkit.Avalon.pyAvalonTools.StruChkFlag.dubious_stereo_removed, 'atom_clash': rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_clash, 'atom_check_failed': rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_check_failed, 'size_check_failed': rdkit.Avalon.pyAvalonTools.StruChkFlag.size_check_failed, 'recharged': rdkit.Avalon.pyAvalonTools.StruChkFlag.recharged, 'stereo_forced_bad': rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_forced_bad, 'stereo_transformed': rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_transformed, 'template_transformed': rdkit.Avalon.pyAvalonTools.StruChkFlag.template_transformed}
    recharged: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.recharged
    size_check_failed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.size_check_failed
    stereo_error: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_error
    stereo_forced_bad: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_forced_bad
    stereo_transformed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_transformed
    template_transformed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.template_transformed
    transformed: typing.ClassVar[StruChkFlag]  # value = rdkit.Avalon.pyAvalonTools.StruChkFlag.transformed
    values: typing.ClassVar[dict]  # value = {1: rdkit.Avalon.pyAvalonTools.StruChkFlag.bad_molecule, 2: rdkit.Avalon.pyAvalonTools.StruChkFlag.alias_conversion_failed, 4: rdkit.Avalon.pyAvalonTools.StruChkFlag.transformed, 8: rdkit.Avalon.pyAvalonTools.StruChkFlag.fragments_found, 16: rdkit.Avalon.pyAvalonTools.StruChkFlag.either_warning, 32: rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_error, 64: rdkit.Avalon.pyAvalonTools.StruChkFlag.dubious_stereo_removed, 128: rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_clash, 256: rdkit.Avalon.pyAvalonTools.StruChkFlag.atom_check_failed, 512: rdkit.Avalon.pyAvalonTools.StruChkFlag.size_check_failed, 1024: rdkit.Avalon.pyAvalonTools.StruChkFlag.recharged, 2048: rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_forced_bad, 4096: rdkit.Avalon.pyAvalonTools.StruChkFlag.stereo_transformed, 8192: rdkit.Avalon.pyAvalonTools.StruChkFlag.template_transformed}
class StruChkResult(Boost.Python.enum):
    __slots__: typing.ClassVar[tuple] = tuple()
    bad_set: typing.ClassVar[StruChkResult]  # value = rdkit.Avalon.pyAvalonTools.StruChkResult.bad_set
    names: typing.ClassVar[dict]  # value = {'success': rdkit.Avalon.pyAvalonTools.StruChkResult.success, 'bad_set': rdkit.Avalon.pyAvalonTools.StruChkResult.bad_set, 'transformed_set': rdkit.Avalon.pyAvalonTools.StruChkResult.transformed_set}
    success: typing.ClassVar[StruChkResult]  # value = rdkit.Avalon.pyAvalonTools.StruChkResult.success
    transformed_set: typing.ClassVar[StruChkResult]  # value = rdkit.Avalon.pyAvalonTools.StruChkResult.transformed_set
    values: typing.ClassVar[dict]  # value = {0: rdkit.Avalon.pyAvalonTools.StruChkResult.success, 2979: rdkit.Avalon.pyAvalonTools.StruChkResult.bad_set, 29788: rdkit.Avalon.pyAvalonTools.StruChkResult.transformed_set}
@typing.overload
def CheckMolecule(molstring: str, isSmiles: bool) -> tuple:
    """
        check a molecule passed in as a string.
        If the isSmiles argument is true, the string should represent the SMILES encoding
        of the molecule, otherwise it should be encoded as an MDL molfile.
        The first member of the return tuple contains the bit-encoded corrections made to the molecule.
        If possible, the molecule (corrected when appropriate) is returned as the second member of 
        the return tuple. Otherwise, None is returned.
    
        C++ signature :
            class boost::python::tuple CheckMolecule(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool)
    """
@typing.overload
def CheckMolecule(mol: typing.Any) -> tuple:
    """
        check a molecule passed in as an RDKit molecule.
        The first member of the return tuple contains the bit-encoded corrections made to the molecule.
        If possible, the molecule (corrected when appropriate) is returned as the second member of 
        the return tuple. Otherwise, None is returned.
    
        C++ signature :
            class boost::python::tuple CheckMolecule(class RDKit::ROMol {lvalue})
    """
def CheckMoleculeString(molstring: str, isSmiles: bool) -> tuple:
    """
        check a molecule passed in as a string and returns the result as a string.
        If the isSmiles argument is true, the string should represent the SMILES encoding
        of the molecule, otherwise it should be encoded as an MDL molfile.
        The first member of the return tuple contains the bit-encoded corrections made to the molecule.
        If possible, a corrected CTAB for the molecule is returned as the second member of 
        the return tuple.
    
        C++ signature :
            class boost::python::tuple CheckMoleculeString(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool)
    """
def CloseCheckMolFiles() -> None:
    """
        close open files used by molecule-checking functions.
    
        C++ signature :
            void CloseCheckMolFiles()
    """
@typing.overload
def Generate2DCoords(mol: typing.Any, clearConfs: bool = True) -> int:
    """
        Generates 2d coordinates for an RDKit molecule
    
        C++ signature :
            unsigned int Generate2DCoords(class RDKit::ROMol {lvalue} [,bool=True])
    """
@typing.overload
def Generate2DCoords(molData: str, isSmiles: bool) -> str:
    """
        returns an MDL mol block with 2D coordinates for some molecule data.
        If the isSmiles argument is true, the data is assumed to be SMILES, otherwise
        MDL mol data is assumed.
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > Generate2DCoords(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool)
    """
@typing.overload
def GetAvalonCountFP(mol: typing.Any, nBits: int = 512, isQuery: bool = False, bitFlags: int = 15761407) -> typing.Any:
    """
        returns the Avalon count fingerprint for an RDKit molecule
    
        C++ signature :
            class RDKit::SparseIntVect<unsigned int> * __ptr64 GetAvalonCountFP(class RDKit::ROMol [,unsigned int=512 [,bool=False [,unsigned int=15761407]]])
    """
@typing.overload
def GetAvalonCountFP(molData: str, isSmiles: bool, nBits: int = 512, isQuery: bool = False, bitFlags: int = 15761407) -> typing.Any:
    """
        returns the Avalon count fingerprint for some molecule data.
        If the isSmiles argument is true, the data is assumed to be SMILES, otherwise
        MDL mol data is assumed.
    
        C++ signature :
            class RDKit::SparseIntVect<unsigned int> * __ptr64 GetAvalonCountFP(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,unsigned int=512 [,bool=False [,unsigned int=15761407]]])
    """
@typing.overload
def GetAvalonFP(mol: typing.Any, nBits: int = 512, isQuery: bool = False, resetVect: bool = False, bitFlags: int = 15761407) -> typing.Any:
    """
        returns the Avalon fingerprint for an RDKit molecule
    
        C++ signature :
            class ExplicitBitVect * __ptr64 GetAvalonFP(class RDKit::ROMol [,unsigned int=512 [,bool=False [,bool=False [,unsigned int=15761407]]]])
    """
@typing.overload
def GetAvalonFP(molData: str, isSmiles: bool, nBits: int = 512, isQuery: bool = False, resetVect: bool = False, bitFlags: int = 15761407) -> typing.Any:
    """
        returns the Avalon fingerprint for some molecule data.
        If the isSmiles argument is true, the data is assumed to be SMILES, otherwise
        MDL mol data is assumed.
    
        C++ signature :
            class ExplicitBitVect * __ptr64 GetAvalonFP(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,unsigned int=512 [,bool=False [,bool=False [,unsigned int=15761407]]]])
    """
@typing.overload
def GetAvalonFPAsWords(mol: typing.Any, nBits: int = 512, isQuery: bool = False, resetVect: bool = False, bitFlags: int = 15761407) -> list:
    """
        returns the Avalon fingerprint for an RDKit molecule as a list of ints
    
        C++ signature :
            class boost::python::list GetAvalonFPAsWords(class RDKit::ROMol [,unsigned int=512 [,bool=False [,bool=False [,unsigned int=15761407]]]])
    """
@typing.overload
def GetAvalonFPAsWords(molData: str, isSmiles: bool, nBits: int = 512, isQuery: bool = False, resetVect: bool = False, bitFlags: int = 15761407) -> list:
    """
        returns the Avalon fingerprint for some molecule data as a list of ints.
        If the isSmiles argument is true, the data is assumed to be SMILES, otherwise
        MDL mol data is assumed.
    
        C++ signature :
            class boost::python::list GetAvalonFPAsWords(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,unsigned int=512 [,bool=False [,bool=False [,unsigned int=15761407]]]])
    """
@typing.overload
def GetCanonSmiles(mol: typing.Any, flags: int = -1) -> str:
    """
        returns canonical smiles for an RDKit molecule
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetCanonSmiles(class RDKit::ROMol {lvalue} [,int=-1])
    """
@typing.overload
def GetCanonSmiles(molData: str, isSmiles: bool, flags: int = -1) -> str:
    """
        Returns canonical smiles for some molecule data.
        If the isSmiles argument is true, the data is assumed to be SMILES, otherwise
        MDL mol data is assumed.
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetCanonSmiles(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,bool [,int=-1])
    """
def GetCheckMolLog() -> str:
    """
        Returns the Struchk log for the last molecules processed.
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetCheckMolLog()
    """
def InitializeCheckMol(options: str = '') -> int:
    """
        initializes the structure checker.
        The argument should contain option lines separated by embedded newlines.An empty string will be used if the argument is omitted.An non-zero error code is returned in case of failure.
    
        C++ signature :
            int InitializeCheckMol([ class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >=''])
    """
avalonSSSBits: int = 32767
avalonSimilarityBits: int = 15761407

"""
Module containing functions to align a molecule to a second molecule
"""
from __future__ import annotations
import typing
__all__: list[str] = ['AlignMol', 'AlignMolConformers', 'BestAlignmentParams', 'CalcRMS', 'GetAlignmentTransform', 'GetAllConformerBestRMS', 'GetBestAlignmentTransform', 'GetBestRMS', 'GetCrippenO3A', 'GetCrippenO3AForProbeConfs', 'GetO3A', 'GetO3AForProbeConfs', 'O3A', 'RandomTransform']
class BestAlignmentParams(Boost.Python.instance):
    """
    Parameters controlling RMSD alignment
    """
    __instance_size__: typing.ClassVar[int] = 80
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def __setattr__(arg1: typing.Any, arg2: str, arg3: typing.Any) -> None:
        """
            C++ signature :
                void __setattr__(class boost::python::api::object,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class boost::python::api::object)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    @property
    def ignoreHs(*args, **kwargs):
        """
        if true, hydrogens will be ignored in the alignment
        """
    @ignoreHs.setter
    def ignoreHs(*args, **kwargs):
        ...
    @property
    def map(*args, **kwargs):
        """
        the atom-atom mapping(s) used in the alignment
        """
    @map.setter
    def map(*args, **kwargs):
        ...
    @property
    def maxMatches(*args, **kwargs):
        """
        maximum number of substructure matches to consider
        """
    @maxMatches.setter
    def maxMatches(*args, **kwargs):
        ...
    @property
    def numThreads(*args, **kwargs):
        """
        number of threads to use
        """
    @numThreads.setter
    def numThreads(*args, **kwargs):
        ...
    @property
    def symmetrizeConjugatedTerminalGroups(*args, **kwargs):
        """
        if true, conjugated terminal functional groups (like nitro or carboxylate) will be considered symmetrically.
        """
    @symmetrizeConjugatedTerminalGroups.setter
    def symmetrizeConjugatedTerminalGroups(*args, **kwargs):
        ...
    @property
    def weights(*args, **kwargs):
        """
        the weights used in the alignment
        """
    @weights.setter
    def weights(*args, **kwargs):
        ...
class O3A(Boost.Python.instance):
    """
    Open3DALIGN object
    """
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def Align(self) -> float:
        """
            aligns probe molecule onto reference molecule
        
            C++ signature :
                double Align(class RDKit::MolAlign::PyO3A {lvalue})
        """
    def Matches(self) -> list:
        """
            returns the AtomMap as found by Open3DALIGN
        
            C++ signature :
                class boost::python::list Matches(class RDKit::MolAlign::PyO3A {lvalue})
        """
    def Score(self) -> float:
        """
            returns the O3AScore of the alignment
        
            C++ signature :
                double Score(class RDKit::MolAlign::PyO3A {lvalue})
        """
    def Trans(self) -> typing.Any:
        """
            returns the transformation which aligns probe molecule onto reference molecule
        
            C++ signature :
                struct _object * __ptr64 Trans(class RDKit::MolAlign::PyO3A {lvalue})
        """
    def Weights(self) -> list:
        """
            returns the weight vector as found by Open3DALIGN
        
            C++ signature :
                class boost::python::list Weights(class RDKit::MolAlign::PyO3A {lvalue})
        """
def AlignMol(prbMol: Mol, refMol: Mol, prbCid: int = -1, refCid: int = -1, atomMap: typing.Any = [], weights: typing.Any = [], reflect: bool = False, maxIters: int = 50) -> float:
    """
        Optimally (minimum RMSD) align a molecule to another molecule
             
              The 3D transformation required to align the specied conformation in the probe molecule
              to a specified conformation in the reference molecule is computed so that the root mean
              squared distance between a specified set of atoms is minimized. 
              This transform is then applied to the specified conformation in the probe molecule
             
             ARGUMENTS
              - prbMol    molecule that is to be aligned
              - refMol    molecule used as the reference for the alignment
              - prbCid    ID of the conformation in the probe to be used 
                               for the alignment (defaults to first conformation)
              - refCid    ID of the conformation in the ref molecule to which 
                               the alignment is computed (defaults to first conformation)
              - atomMap   a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                               used to compute the alignments. If this mapping is 
                               not specified an attempt is made to generate one by
                               substructure matching
              - weights   Optionally specify weights for each of the atom pairs
              - reflect   if true reflect the conformation of the probe molecule
              - maxIters  maximum number of iterations used in minimizing the RMSD
               
              RETURNS
              RMSD value
            
        
    
        C++ signature :
            double AlignMol(class RDKit::ROMol {lvalue},class RDKit::ROMol [,int=-1 [,int=-1 [,class boost::python::api::object=[] [,class boost::python::api::object=[] [,bool=False [,unsigned int=50]]]]]])
    """
def AlignMolConformers(mol: Mol, atomIds: typing.Any = [], confIds: typing.Any = [], weights: typing.Any = [], reflect: bool = False, maxIters: int = 50, RMSlist: typing.Any = None) -> None:
    """
        Align conformations in a molecule to each other
             
              The first conformation in the molecule is used as the reference
             
             ARGUMENTS
              - mol          molecule of interest
              - atomIds      List of atom ids to use a points for alignment - defaults to all atoms
              - confIds      Ids of conformations to align - defaults to all conformers 
              - weights      Optionally specify weights for each of the atom pairs
              - reflect      if true reflect the conformation of the probe molecule
              - maxIters     maximum number of iterations used in minimizing the RMSD
              - RMSlist      if provided, fills in the RMS values between the reference
        		     conformation and the other aligned conformations
               
            
        
    
        C++ signature :
            void AlignMolConformers(class RDKit::ROMol {lvalue} [,class boost::python::api::object=[] [,class boost::python::api::object=[] [,class boost::python::api::object=[] [,bool=False [,unsigned int=50 [,class boost::python::api::object=None]]]]]])
    """
def CalcRMS(prbMol: Mol, refMol: Mol, prbId: int = -1, refId: int = -1, map: typing.Any = None, maxMatches: int = 1000000, symmetrizeConjugatedTerminalGroups: bool = True, weights: typing.Any = []) -> float:
    """
        Returns the RMS between two molecules, taking symmetry into account.
               In contrast to getBestRMS, the RMS is computed 'in place', i.e.
               probe molecules are not aligned to the reference ahead of the
               RMS calculation. This is useful, for example, to compute
               the RMSD between docking poses and the co-crystallized ligand.
              
               Note:
               This function will attempt to match all permutations of matching atom
               orders in both molecules, for some molecules it will lead to
               'combinatorial explosion' especially if hydrogens are present.
              
               ARGUMENTS
                - prbMol:      the molecule to be aligned to the reference
                - refMol:      the reference molecule
                - prbCId:      (optional) probe conformation to use
                - refCId:      (optional) reference conformation to use
                - map:         (optional) a list of lists of (probeAtomId, refAtomId)
                               tuples with the atom-atom mappings of the two
                               molecules. If not provided, these will be generated
                               using a substructure search.
                - maxMatches:  (optional) if map isn't specified, this will be
                               the max number of matches found in a SubstructMatch()
                - symmetrizeConjugatedTerminalGroups:  (optional) if set, conjugated
                               terminal functional groups (like nitro or carboxylate)
                               will be considered symmetrically
                - weights:     (optional) weights for mapping
               
              RETURNS
              The best RMSD found
            
        
    
        C++ signature :
            double CalcRMS(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,int=-1 [,int=-1 [,class boost::python::api::object=None [,int=1000000 [,bool=True [,class boost::python::api::object=[]]]]]]])
    """
def GetAlignmentTransform(prbMol: Mol, refMol: Mol, prbCid: int = -1, refCid: int = -1, atomMap: typing.Any = [], weights: typing.Any = [], reflect: bool = False, maxIters: int = 50) -> typing.Any:
    """
        Compute the transformation required to align a molecule
             
              The 3D transformation required to align the specied conformation in the probe molecule
              to a specified conformation in the reference molecule is computed so that the root mean
              squared distance between a specified set of atoms is minimized
             
             ARGUMENTS
              - prbMol    molecule that is to be aligned
              - refMol    molecule used as the reference for the alignment
              - prbCid    ID of the conformation in the probe to be used 
                               for the alignment (defaults to first conformation)
              - refCid    ID of the conformation in the ref molecule to which 
                               the alignment is computed (defaults to first conformation)
              - atomMap   a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                               used to compute the alignments. If this mapping is 
                               not specified an attempt is made to generate one by
                               substructure matching
              - weights   Optionally specify weights for each of the atom pairs
              - reflect   if true reflect the conformation of the probe molecule
              - maxIters  maximum number of iterations used in minimizing the RMSD
               
              RETURNS
              a tuple of (RMSD value, transform matrix) 
            
        
    
        C++ signature :
            struct _object * __ptr64 GetAlignmentTransform(class RDKit::ROMol,class RDKit::ROMol [,int=-1 [,int=-1 [,class boost::python::api::object=[] [,class boost::python::api::object=[] [,bool=False [,unsigned int=50]]]]]])
    """
@typing.overload
def GetAllConformerBestRMS(mol: Mol, numThreads: int = 1, map: typing.Any = None, maxMatches: int = 1000000, symmetrizeConjugatedTerminalGroups: bool = True, weights: typing.Any = []) -> tuple:
    """
        Returns the symmetric distance matrix between the conformers of a molecule.
               getBestRMS() is used to calculate the inter-conformer distances
        
               ARGUMENTS
                - mol:       the molecule to be considered
                - numThreads:  (optional) number of threads to use
                - map:         (optional) a list of lists of (probeAtomId,refAtomId)
                               tuples with the atom-atom mappings of the two
                               molecules. If not provided, these will be generated
                               using a substructure search.
                - maxMatches:  (optional) if map isn't specified, this will be
                               the max number of matches found in a SubstructMatch()
                - symmetrizeConjugatedTerminalGroups:  (optional) if set, conjugated
                               terminal functional groups (like nitro or carboxylate)
                               will be considered symmetrically
                - weights:     (optional) weights for mapping
               
              RETURNS
              A tuple with the best RMSDS. The ordering is [(1,0),(2,0),(2,1),(3,0),... etc]
          
    
        C++ signature :
            class boost::python::tuple GetAllConformerBestRMS(class RDKit::ROMol {lvalue} [,int=1 [,class boost::python::api::object=None [,int=1000000 [,bool=True [,class boost::python::api::object=[]]]]]])
    """
@typing.overload
def GetAllConformerBestRMS(mol: Mol, params: BestAlignmentParams) -> tuple:
    """
        Returns the symmetric distance matrix between the conformers of a molecule.
               getBestRMS() is used to calculate the inter-conformer distances
        
               ARGUMENTS
                - mol:       the molecule to be considered
                - numThreads:  (optional) number of threads to use
                - map:         (optional) a list of lists of (probeAtomId,refAtomId)
                               tuples with the atom-atom mappings of the two
                               molecules. If not provided, these will be generated
                               using a substructure search.
                - maxMatches:  (optional) if map isn't specified, this will be
                               the max number of matches found in a SubstructMatch()
                - symmetrizeConjugatedTerminalGroups:  (optional) if set, conjugated
                               terminal functional groups (like nitro or carboxylate)
                               will be considered symmetrically
                - weights:     (optional) weights for mapping
               
              RETURNS
              A tuple with the best RMSDS. The ordering is [(1,0),(2,0),(2,1),(3,0),... etc]
          
    
        C++ signature :
            class boost::python::tuple GetAllConformerBestRMS(class RDKit::ROMol {lvalue},struct RDKit::MolAlign::pyBestAlignmentParams)
    """
@typing.overload
def GetBestAlignmentTransform(prbMol: Mol, refMol: Mol, prbCid: int = -1, refCid: int = -1, map: typing.Any = [], maxMatches: int = 1000000, symmetrizeConjugatedTerminalGroups: bool = True, weights: typing.Any = [], reflect: bool = False, maxIters: int = 50, numThreads: int = 1) -> typing.Any:
    """
        Compute the optimal RMS, transformation and atom map for aligning
              two molecules, taking symmetry into account. Molecule coordinates
              are left unaltered.
            
              This function will attempt to align all permutations of matching atom
              orders in both molecules, for some molecules it will lead to 'combinatorial
              explosion' especially if hydrogens are present.
              Use 'GetAlignmentTransform' to align molecules without changing the atom order.
            
             ARGUMENTS
              - prbMol      molecule that is to be aligned
              - refMol      molecule used as the reference for the alignment
              - prbCid      ID of the conformation in the probe to be used 
                            for the alignment (defaults to first conformation)
              - refCid      ID of the conformation in the ref molecule to which 
                            the alignment is computed (defaults to first conformation)
              - map:        (optional) a list of lists of (probeAtomId, refAtomId)
                            tuples with the atom-atom mappings of the two
                            molecules. If not provided, these will be generated
                            using a substructure search.
              - maxMatches  (optional) if atomMap is empty, this will be the max number of
                            matches found in a SubstructMatch().
              - symmetrizeConjugatedTerminalGroups (optional) if set, conjugated
                            terminal functional groups (like nitro or carboxylate)
                            will be considered symmetrically.
              - weights     Optionally specify weights for each of the atom pairs
              - reflect     if true reflect the conformation of the probe molecule
              - maxIters    maximum number of iterations used in minimizing the RMSD
              - numThreads  (optional) number of threads to use
               
              RETURNS
              a tuple of (RMSD value, best transform matrix, best atom map)
            
        
    
        C++ signature :
            struct _object * __ptr64 GetBestAlignmentTransform(class RDKit::ROMol,class RDKit::ROMol [,int=-1 [,int=-1 [,class boost::python::api::object=[] [,int=1000000 [,bool=True [,class boost::python::api::object=[] [,bool=False [,unsigned int=50 [,int=1]]]]]]]]])
    """
@typing.overload
def GetBestAlignmentTransform(prbMol: Mol, refMol: Mol, params: BestAlignmentParams, prbCid: int = -1, refCid: int = -1, reflect: bool = False, maxIters: int = 50) -> typing.Any:
    """
        Compute the optimal RMS, transformation and atom map for aligning
              two molecules, taking symmetry into account. Molecule coordinates
              are left unaltered.
            
              This function will attempt to align all permutations of matching atom
              orders in both molecules, for some molecules it will lead to 'combinatorial
              explosion' especially if hydrogens are present.
              Use 'GetAlignmentTransform' to align molecules without changing the atom order.
            
             ARGUMENTS
              - prbMol      molecule that is to be aligned
              - refMol      molecule used as the reference for the alignment
              - prbCid      ID of the conformation in the probe to be used 
                            for the alignment (defaults to first conformation)
              - refCid      ID of the conformation in the ref molecule to which 
                            the alignment is computed (defaults to first conformation)
              - map:        (optional) a list of lists of (probeAtomId, refAtomId)
                            tuples with the atom-atom mappings of the two
                            molecules. If not provided, these will be generated
                            using a substructure search.
              - maxMatches  (optional) if atomMap is empty, this will be the max number of
                            matches found in a SubstructMatch().
              - symmetrizeConjugatedTerminalGroups (optional) if set, conjugated
                            terminal functional groups (like nitro or carboxylate)
                            will be considered symmetrically.
              - weights     Optionally specify weights for each of the atom pairs
              - reflect     if true reflect the conformation of the probe molecule
              - maxIters    maximum number of iterations used in minimizing the RMSD
              - numThreads  (optional) number of threads to use
               
              RETURNS
              a tuple of (RMSD value, best transform matrix, best atom map)
            
        
    
        C++ signature :
            struct _object * __ptr64 GetBestAlignmentTransform(class RDKit::ROMol,class RDKit::ROMol,struct RDKit::MolAlign::pyBestAlignmentParams [,int=-1 [,int=-1 [,bool=False [,unsigned int=50]]]])
    """
@typing.overload
def GetBestRMS(prbMol: Mol, refMol: Mol, prbId: int = -1, refId: int = -1, map: typing.Any = None, maxMatches: int = 1000000, symmetrizeConjugatedTerminalGroups: bool = True, weights: typing.Any = [], numThreads: int = 1) -> float:
    """
        Returns the optimal RMS for aligning two molecules, taking
               symmetry into account. As a side-effect, the probe molecule is
               left in the aligned state.
              
               Note:
               This function will attempt to align all permutations of matching atom
               orders in both molecules, for some molecules it will lead to
               'combinatorial explosion' especially if hydrogens are present.
               Use 'rdkit.Chem.AllChem.AlignMol' to align molecules without changing
               the atom order.
              
               ARGUMENTS
                - prbMol:      the molecule to be aligned to the reference
                - refMol:      the reference molecule
                - prbId:       (optional) probe conformation to use
                - refId:       (optional) reference conformation to use
                - map:         (optional) a list of lists of (probeAtomId,refAtomId)
                               tuples with the atom-atom mappings of the two
                               molecules. If not provided, these will be generated
                               using a substructure search.
                - maxMatches:  (optional) if map isn't specified, this will be
                               the max number of matches found in a SubstructMatch()
                - symmetrizeConjugatedTerminalGroups:  (optional) if set, conjugated
                               terminal functional groups (like nitro or carboxylate)
                               will be considered symmetrically
                - weights:     (optional) weights for mapping
                - numThreads:  (optional) number of threads to use
               
              RETURNS
              The best RMSD found
            
        
    
        C++ signature :
            double GetBestRMS(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,int=-1 [,int=-1 [,class boost::python::api::object=None [,int=1000000 [,bool=True [,class boost::python::api::object=[] [,int=1]]]]]]])
    """
@typing.overload
def GetBestRMS(prbMol: Mol, refMol: Mol, params: BestAlignmentParams, prbId: int = -1, refId: int = -1) -> float:
    """
        Returns the optimal RMS for aligning two molecules, taking
               symmetry into account. As a side-effect, the probe molecule is
               left in the aligned state.
              
               Note:
               This function will attempt to align all permutations of matching atom
               orders in both molecules, for some molecules it will lead to
               'combinatorial explosion' especially if hydrogens are present.
               Use 'rdkit.Chem.AllChem.AlignMol' to align molecules without changing
               the atom order.
              
               ARGUMENTS
                - prbMol:      the molecule to be aligned to the reference
                - refMol:      the reference molecule
                - prbId:       (optional) probe conformation to use
                - refId:       (optional) reference conformation to use
                - map:         (optional) a list of lists of (probeAtomId,refAtomId)
                               tuples with the atom-atom mappings of the two
                               molecules. If not provided, these will be generated
                               using a substructure search.
                - maxMatches:  (optional) if map isn't specified, this will be
                               the max number of matches found in a SubstructMatch()
                - symmetrizeConjugatedTerminalGroups:  (optional) if set, conjugated
                               terminal functional groups (like nitro or carboxylate)
                               will be considered symmetrically
                - weights:     (optional) weights for mapping
                - numThreads:  (optional) number of threads to use
               
              RETURNS
              The best RMSD found
            
        
    
        C++ signature :
            double GetBestRMS(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue},struct RDKit::MolAlign::pyBestAlignmentParams [,int=-1 [,int=-1]])
    """
def GetCrippenO3A(prbMol: Mol, refMol: Mol, prbCrippenContribs: list = [], refCrippenContribs: list = [], prbCid: int = -1, refCid: int = -1, reflect: bool = False, maxIters: int = 50, options: int = 0, constraintMap: list = [], constraintWeights: list = []) -> O3A:
    """
        Get an O3A object with atomMap and weights vectors to overlay
              the probe molecule onto the reference molecule based on
              Crippen logP atom contributions
             
             ARGUMENTS
              - prbMol                   molecule that is to be aligned
              - refMol                   molecule used as the reference for the alignment
              - prbCrippenContribs       Crippen atom contributions for the probe molecule
                                         as a list of (logp, mr) tuples, as returned
                                         by _CalcCrippenContribs()
              - refCrippenContribs       Crippen atom contributions for the reference molecule
                                         as a list of (logp, mr) tuples, as returned
                                         by _CalcCrippenContribs()
              - prbCid                   ID of the conformation in the probe to be used 
                                         for the alignment (defaults to first conformation)
              - refCid                   ID of the conformation in the ref molecule to which 
                                         the alignment is computed (defaults to first conformation)
              - reflect                  if true reflect the conformation of the probe molecule
                                         (defaults to false)
              - maxIters                 maximum number of iterations used in minimizing the RMSD
                                         (defaults to 50)
              - options                  least 2 significant bits encode accuracy
                                         (0: maximum, 3: minimum; defaults to 0)
                                         bit 3 triggers local optimization of the alignment
                                         (no computation of the cost matrix; defaults: off)
              - constraintMap            a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                                         which shall be used for the alignment (defaults to [])
              - constraintWeights        optionally specify weights for each of the constraints
                                         (weights default to 100.0)
               
              RETURNS
              The O3A object
            
        
    
        C++ signature :
            class RDKit::MolAlign::PyO3A * __ptr64 GetCrippenO3A(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,class boost::python::list=[] [,class boost::python::list=[] [,int=-1 [,int=-1 [,bool=False [,unsigned int=50 [,unsigned int=0 [,class boost::python::list=[] [,class boost::python::list=[]]]]]]]]]])
    """
def GetCrippenO3AForProbeConfs(prbMol: Mol, refMol: Mol, numThreads: int = 1, prbCrippenContribs: list = [], refCrippenContribs: list = [], refCid: int = -1, reflect: bool = False, maxIters: int = 50, options: int = 0, constraintMap: list = [], constraintWeights: list = []) -> tuple:
    """
        Get a vector of O3A objects for the overlay of all 
              the probe molecule's conformations onto the reference molecule based on
              MMFF atom types and charges
             
             ARGUMENTS
              - prbMol                   molecule that is to be aligned
              - refMol                   molecule used as the reference for the alignment
              - numThreads :             the number of threads to use, only has an effect if
                                         the RDKit was built with thread support (defaults to 1)
              - prbCrippenContribs       Crippen atom contributions for the probe molecule
                                         as a list of (logp, mr) tuples, as returned
                                         by _CalcCrippenContribs()
              - refCrippenContribs       Crippen atom contributions for the reference molecule
                                         as a list of (logp, mr) tuples, as returned
                                         by _CalcCrippenContribs()
              - refCid                   ID of the conformation in the ref molecule to which 
                                         the alignment is computed (defaults to first conformation)
              - reflect                  if true reflect the conformation of the probe molecule
                                         (defaults to false)
              - maxIters                 maximum number of iterations used in minimizing the RMSD
                                         (defaults to 50)
              - options                  least 2 significant bits encode accuracy
                                         (0: maximum, 3: minimum; defaults to 0)
                                         bit 3 triggers local optimization of the alignment
                                         (no computation of the cost matrix; defaults: off)
              - constraintMap            a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                                         which shall be used for the alignment (defaults to [])
              - constraintWeights        optionally specify weights for each of the constraints
                                         (weights default to 100.0)
               
              RETURNS
              A vector of O3A objects
            
        
    
        C++ signature :
            class boost::python::tuple GetCrippenO3AForProbeConfs(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,int=1 [,class boost::python::list=[] [,class boost::python::list=[] [,int=-1 [,bool=False [,unsigned int=50 [,unsigned int=0 [,class boost::python::list=[] [,class boost::python::list=[]]]]]]]]]])
    """
def GetO3A(prbMol: Mol, refMol: Mol, prbPyMMFFMolProperties: typing.Any = None, refPyMMFFMolProperties: typing.Any = None, prbCid: int = -1, refCid: int = -1, reflect: bool = False, maxIters: int = 50, options: int = 0, constraintMap: list = [], constraintWeights: list = []) -> O3A:
    """
        Get an O3A object with atomMap and weights vectors to overlay
              the probe molecule onto the reference molecule based on
              MMFF atom types and charges
             
             ARGUMENTS
              - prbMol                   molecule that is to be aligned
              - refMol                   molecule used as the reference for the alignment
              - prbPyMMFFMolProperties   PyMMFFMolProperties object for the probe molecule as returned
                                         by SetupMMFFForceField()
              - refPyMMFFMolProperties   PyMMFFMolProperties object for the reference molecule as returned
                                         by SetupMMFFForceField()
              - prbCid                   ID of the conformation in the probe to be used 
                                         for the alignment (defaults to first conformation)
              - refCid                   ID of the conformation in the ref molecule to which 
                                         the alignment is computed (defaults to first conformation)
              - reflect                  if true reflect the conformation of the probe molecule
                                         (defaults to false)
              - maxIters                 maximum number of iterations used in minimizing the RMSD
                                         (defaults to 50)
              - options                  least 2 significant bits encode accuracy
                                         (0: maximum, 3: minimum; defaults to 0)
                                         bit 3 triggers local optimization of the alignment
                                         (no computation of the cost matrix; defaults: off)
              - constraintMap            a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                                         which shall be used for the alignment (defaults to [])
              - constraintWeights        optionally specify weights for each of the constraints
                                         (weights default to 100.0)
               
              RETURNS
              The O3A object
            
        
    
        C++ signature :
            class RDKit::MolAlign::PyO3A * __ptr64 GetO3A(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,class boost::python::api::object=None [,class boost::python::api::object=None [,int=-1 [,int=-1 [,bool=False [,unsigned int=50 [,unsigned int=0 [,class boost::python::list=[] [,class boost::python::list=[]]]]]]]]]])
    """
def GetO3AForProbeConfs(prbMol: Mol, refMol: Mol, numThreads: int = 1, prbPyMMFFMolProperties: typing.Any = None, refPyMMFFMolProperties: typing.Any = None, refCid: int = -1, reflect: bool = False, maxIters: int = 50, options: int = 0, constraintMap: list = [], constraintWeights: list = []) -> tuple:
    """
        Get a vector of O3A objects for the overlay of all 
              the probe molecule's conformations onto the reference molecule based on
              MMFF atom types and charges
             
             ARGUMENTS
              - prbMol                   molecule that is to be aligned
              - refMol                   molecule used as the reference for the alignment
              - numThreads :             the number of threads to use, only has an effect if
                                         the RDKit was built with thread support (defaults to 1)
                                         If set to zero, the max supported by the system will be used.
              - prbPyMMFFMolProperties   PyMMFFMolProperties object for the probe molecule as returned
                                         by SetupMMFFForceField()
              - refPyMMFFMolProperties   PyMMFFMolProperties object for the reference molecule as returned
                                         by SetupMMFFForceField()
              - refCid                   ID of the conformation in the ref molecule to which 
                                         the alignment is computed (defaults to first conformation)
              - reflect                  if true reflect the conformation of the probe molecule
                                         (defaults to false)
              - maxIters                 maximum number of iterations used in minimizing the RMSD
                                         (defaults to 50)
              - options                  least 2 significant bits encode accuracy
                                         (0: maximum, 3: minimum; defaults to 0)
                                         bit 3 triggers local optimization of the alignment
                                         (no computation of the cost matrix; defaults: off)
              - constraintMap            a vector of pairs of atom IDs (probe AtomId, ref AtomId)
                                         which shall be used for the alignment (defaults to [])
              - constraintWeights        optionally specify weights for each of the constraints
                                         (weights default to 100.0)
               
              RETURNS
              A vector of O3A objects
            
        
    
        C++ signature :
            class boost::python::tuple GetO3AForProbeConfs(class RDKit::ROMol {lvalue},class RDKit::ROMol {lvalue} [,int=1 [,class boost::python::api::object=None [,class boost::python::api::object=None [,int=-1 [,bool=False [,unsigned int=50 [,unsigned int=0 [,class boost::python::list=[] [,class boost::python::list=[]]]]]]]]]])
    """
def RandomTransform(mol: Mol, cid: int = -1, seed: int = -1) -> None:
    """
        Perform a random transformation on a molecule
             
             ARGUMENTS
              - mol    molecule that is to be transformed
              - cid    ID of the conformation in the mol to be transformed
                       (defaults to first conformation)
              - seed   seed used to initialize the random generator
                       (defaults to -1, that is no seeding)
               
            
        
    
        C++ signature :
            void RandomTransform(class RDKit::ROMol {lvalue} [,int=-1 [,int=-1]])
    """

from __future__ import annotations
import math as math
import numpy as numpy
from rdkit import Chem
from rdkit.Chem import ChemicalFeatures
from rdkit.Chem import ChemicalForceFields
from rdkit.Chem.Pharm3D import ExcludedVolume
from rdkit.Chem import rdDistGeom as MolDG
from rdkit import DistanceGeometry as DG
from rdkit.ML.Data import Stats
import rdkit.RDLogger
from rdkit import RDLogger as logging
import sys as sys
import time as time
__all__: list[str] = ['AddExcludedVolumes', 'Check2DBounds', 'Chem', 'ChemicalFeatures', 'ChemicalForceFields', 'CoarseScreenPharmacophore', 'CombiEnum', 'ComputeChiralVolume', 'ConstrainedEnum', 'DG', 'DownsampleBoundsMatrix', 'EmbedMol', 'EmbedOne', 'EmbedPharmacophore', 'ExcludedVolume', 'GetAllPharmacophoreMatches', 'GetAtomHeavyNeighbors', 'MatchFeatsToMol', 'MatchPharmacophore', 'MatchPharmacophoreToMol', 'MolDG', 'OptimizeMol', 'ReplaceGroup', 'Stats', 'UpdatePharmacophoreBounds', 'defaultFeatLength', 'isNaN', 'logger', 'logging', 'math', 'numpy', 'sys', 'time']
def AddExcludedVolumes(bm, excludedVolumes, smoothIt = True):
    """
     Adds a set of excluded volumes to the bounds matrix
      and returns the new matrix
    
      excludedVolumes is a list of ExcludedVolume objects
    
    
       >>> boundsMat = numpy.array([[0.0, 2.0, 2.0],[1.0, 0.0, 2.0],[1.0, 1.0, 0.0]])
       >>> ev1 = ExcludedVolume.ExcludedVolume(([(0, ), 0.5, 1.0], ), exclusionDist=1.5)
       >>> bm = AddExcludedVolumes(boundsMat, (ev1, ))
    
       the results matrix is one bigger:
    
       >>> bm.shape == (4, 4)
       True
    
       and the original bounds mat is not altered:
    
       >>> boundsMat.shape == (3, 3)
       True
    
       >>> print(', '.join([f'{x:.3f}' for x in bm[-1]]))
       0.500, 1.500, 1.500, 0.000
       >>> print(', '.join([f'{x:.3f}' for x in bm[:,-1]]))
       1.000, 3.000, 3.000, 0.000
    
      
    """
def Check2DBounds(atomMatch, mol, pcophore):
    """
     checks to see if a particular mapping of features onto
      a molecule satisfies a pharmacophore's 2D restrictions
    
        >>> from rdkit import Geometry
        >>> from rdkit.Chem.Pharm3D import Pharmacophore
        >>> activeFeats = [
        ...  ChemicalFeatures.FreeChemicalFeature('Acceptor', Geometry.Point3D(0.0, 0.0, 0.0)),
        ...  ChemicalFeatures.FreeChemicalFeature('Donor', Geometry.Point3D(0.0, 0.0, 0.0))]
        >>> pcophore= Pharmacophore.Pharmacophore(activeFeats)
        >>> pcophore.setUpperBound2D(0, 1, 3)
        >>> m = Chem.MolFromSmiles('FCC(N)CN')
        >>> Check2DBounds(((0, ), (3, )), m, pcophore)
        True
        >>> Check2DBounds(((0, ), (5, )), m, pcophore)
        False
    
      
    """
def CoarseScreenPharmacophore(atomMatch, bounds, pcophore, verbose = False):
    """
    
      >>> from rdkit import Geometry
      >>> from rdkit.Chem.Pharm3D import Pharmacophore
      >>> feats = [
      ...   ChemicalFeatures.FreeChemicalFeature('HBondAcceptor', 'HAcceptor1',
      ...                                        Geometry.Point3D(0.0, 0.0, 0.0)),
      ...   ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
      ...                                        Geometry.Point3D(2.65, 0.0, 0.0)),
      ...   ChemicalFeatures.FreeChemicalFeature('Aromatic', 'Aromatic1',
      ...                                        Geometry.Point3D(5.12, 0.908, 0.0)),
      ...   ]
      >>> pcophore = Pharmacophore.Pharmacophore(feats)
      >>> pcophore.setLowerBound(0, 1, 1.1)
      >>> pcophore.setUpperBound(0, 1, 1.9)
      >>> pcophore.setLowerBound(0, 2, 2.1)
      >>> pcophore.setUpperBound(0, 2, 2.9)
      >>> pcophore.setLowerBound(1, 2, 2.1)
      >>> pcophore.setUpperBound(1, 2, 3.9)
    
      >>> bounds = numpy.array([[0, 2, 3],[1, 0, 4],[2, 3, 0]], dtype=numpy.float64)
      >>> CoarseScreenPharmacophore(((0, ),(1, )),bounds, pcophore)
      True
    
      >>> CoarseScreenPharmacophore(((0, ),(2, )),bounds, pcophore)
      False
    
      >>> CoarseScreenPharmacophore(((1, ),(2, )),bounds, pcophore)
      False
    
      >>> CoarseScreenPharmacophore(((0, ),(1, ),(2, )),bounds, pcophore)
      True
    
      >>> CoarseScreenPharmacophore(((1, ),(0, ),(2, )),bounds, pcophore)
      False
    
      >>> CoarseScreenPharmacophore(((2, ),(1, ),(0, )),bounds, pcophore)
      False
    
      # we ignore the point locations here and just use their definitions:
    
      >>> feats = [
      ...   ChemicalFeatures.FreeChemicalFeature('HBondAcceptor', 'HAcceptor1',
      ...                                        Geometry.Point3D(0.0, 0.0, 0.0)),
      ...   ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
      ...                                        Geometry.Point3D(2.65, 0.0, 0.0)),
      ...   ChemicalFeatures.FreeChemicalFeature('Aromatic', 'Aromatic1',
      ...                                        Geometry.Point3D(5.12, 0.908, 0.0)),
      ...   ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
      ...                                        Geometry.Point3D(2.65, 0.0, 0.0)),
      ...                ]
      >>> pcophore=Pharmacophore.Pharmacophore(feats)
      >>> pcophore.setLowerBound(0,1, 2.1)
      >>> pcophore.setUpperBound(0,1, 2.9)
      >>> pcophore.setLowerBound(0,2, 2.1)
      >>> pcophore.setUpperBound(0,2, 2.9)
      >>> pcophore.setLowerBound(0,3, 2.1)
      >>> pcophore.setUpperBound(0,3, 2.9)
      >>> pcophore.setLowerBound(1,2, 1.1)
      >>> pcophore.setUpperBound(1,2, 1.9)
      >>> pcophore.setLowerBound(1,3, 1.1)
      >>> pcophore.setUpperBound(1,3, 1.9)
      >>> pcophore.setLowerBound(2,3, 1.1)
      >>> pcophore.setUpperBound(2,3, 1.9)
      >>> bounds = numpy.array([[0, 3, 3, 3],
      ...                       [2, 0, 2, 2],
      ...                       [2, 1, 0, 2],
      ...                       [2, 1, 1, 0]],
      ...                      dtype=numpy.float64)
    
      >>> CoarseScreenPharmacophore(((0, ), (1, ), (2, ), (3, )), bounds, pcophore)
      True
    
      >>> CoarseScreenPharmacophore(((0, ), (1, ), (3, ), (2, )), bounds, pcophore)
      True
    
      >>> CoarseScreenPharmacophore(((1, ), (0, ), (3, ), (2, )), bounds, pcophore)
      False
    
      
    """
def CombiEnum(sequence):
    """
     This generator takes a sequence of sequences as an argument and
      provides all combinations of the elements of the subsequences:
    
      >>> gen = CombiEnum(((1, 2), (10, 20)))
      >>> next(gen)
      [1, 10]
      >>> next(gen)
      [1, 20]
    
      >>> [x for x in CombiEnum(((1, 2), (10,20)))]
      [[1, 10], [1, 20], [2, 10], [2, 20]]
    
      >>> [x for x in CombiEnum(((1, 2),(10, 20), (100, 200)))]
      [[1, 10, 100], [1, 10, 200], [1, 20, 100], [1, 20, 200], [2, 10, 100],
       [2, 10, 200], [2, 20, 100], [2, 20, 200]]
    
      
    """
def ComputeChiralVolume(mol, centerIdx, confId = -1):
    """
     Computes the chiral volume of an atom
    
      We're using the chiral volume formula from Figure 7 of
      Blaney and Dixon, Rev. Comp. Chem. V, 299-335 (1994)
    
        >>> import os.path
        >>> from rdkit import RDConfig
        >>> dataDir = os.path.join(RDConfig.RDCodeDir,'Chem/Pharm3D/test_data')
    
        This function only makes sense if we're using legacy stereo perception
        >>> origVal = Chem.GetUseLegacyStereoPerception()
        >>> Chem.SetUseLegacyStereoPerception(True)
    
        R configuration atoms give negative volumes:
    
        >>> mol = Chem.MolFromMolFile(os.path.join(dataDir, 'mol-r.mol'))
        >>> Chem.AssignStereochemistry(mol)
        >>> mol.GetAtomWithIdx(1).GetProp('_CIPCode')
        'R'
        >>> ComputeChiralVolume(mol, 1) < 0
        True
    
        S configuration atoms give positive volumes:
    
        >>> mol = Chem.MolFromMolFile(os.path.join(dataDir, 'mol-s.mol'))
        >>> Chem.AssignStereochemistry(mol)
        >>> mol.GetAtomWithIdx(1).GetProp('_CIPCode')
        'S'
        >>> ComputeChiralVolume(mol, 1) > 0
        True
    
        Non-chiral (or non-specified) atoms give zero volume:
    
        >>> ComputeChiralVolume(mol, 0) == 0.0
        True
    
        We also work on 3-coordinate atoms (with implicit Hs):
    
        >>> mol = Chem.MolFromMolFile(os.path.join(dataDir, 'mol-r-3.mol'))
        >>> Chem.AssignStereochemistry(mol)
        >>> mol.GetAtomWithIdx(1).GetProp('_CIPCode')
        'R'
        >>> ComputeChiralVolume(mol, 1) < 0
        True
    
        >>> mol = Chem.MolFromMolFile(os.path.join(dataDir, 'mol-s-3.mol'))
        >>> Chem.AssignStereochemistry(mol)
        >>> mol.GetAtomWithIdx(1).GetProp('_CIPCode')
        'S'
        >>> ComputeChiralVolume(mol, 1) > 0
        True
    
        >>> Chem.SetUseLegacyStereoPerception(origVal)
    
      
    """
def ConstrainedEnum(matches, mol, pcophore, bounds, use2DLimits = False, index = 0, soFar = list()):
    """
     Enumerates the list of atom mappings a molecule
      has to a particular pharmacophore.
      We do check distance bounds here.
    
    
      
    """
def DownsampleBoundsMatrix(bm, indices, maxThresh = 4.0):
    """
     Removes rows from a bounds matrix that are that are greater
      than a threshold value away from a set of other points
    
      Returns the modfied bounds matrix
    
      The goal of this function is to remove rows from the bounds matrix
      that correspond to atoms (atomic index) that are likely to be quite far from
      the pharmacophore we're interested in. Because the bounds smoothing
      we eventually have to do is N^3, this can be a big win
    
       >>> boundsMat = numpy.array([[0.0, 3.0, 4.0],[2.0, 0.0, 3.0],[2.0, 2.0, 0.0]])
       >>> bm = DownsampleBoundsMatrix(boundsMat,(0, ), 3.5)
       >>> bm.shape == (2, 2)
       True
    
       we don't touch the input matrix:
    
       >>> boundsMat.shape == (3, 3)
       True
    
       >>> print(', '.join([f'{x:.3f}' for x in bm[0]]))
       0.000, 3.000
       >>> print(', '.join([f'{x:.3f}' for x in bm[1]]))
       2.000, 0.000
    
       if the threshold is high enough, we don't do anything:
    
       >>> boundsMat = numpy.array([[0.0, 4.0, 3.0],[2.0, 0.0, 3.0],[2.0, 2.0, 0.0]])
       >>> bm = DownsampleBoundsMatrix(boundsMat, (0, ), 5.0)
       >>> bm.shape == (3, 3)
       True
    
       If there's a max value that's close enough to *any* of the indices
       we pass in, we'll keep it:
    
       >>> boundsMat = numpy.array([[0.0, 4.0, 3.0],[2.0, 0.0, 3.0],[2.0, 2.0, 0.0]])
       >>> bm = DownsampleBoundsMatrix(boundsMat, (0, 1), 3.5)
       >>> bm.shape == (3, 3)
       True
    
       However, the datatype should not be changed or uprank into np.float64 as default behaviour
       >>> boundsMat = numpy.array([[0.0, 4.0, 3.0],[2.0, 0.0, 3.0],[2.0, 2.0, 0.0]], dtype=numpy.float32)
       >>> bm = DownsampleBoundsMatrix(boundsMat,(0, 1), 3.5)
       >>> bm.dtype == numpy.float64
       False
       >>> bm.dtype == numpy.float32 or numpy.issubdtype(bm.dtype, numpy.float32)
       True
       >>> bm.dtype == boundsMat.dtype or numpy.issubdtype(bm.dtype, boundsMat.dtype)
       True
    
      
    """
def EmbedMol(mol, bm, atomMatch = None, weight = 2.0, randomSeed = -1, excludedVolumes = None):
    """
      Generates an embedding for a molecule based on a bounds matrix and adds
      a conformer (id 0) to the molecule
    
      if the optional argument atomMatch is provided, it will be used to provide
      supplemental weights for the embedding routine (used in the optimization
      phase to ensure that the resulting geometry really does satisfy the
      pharmacophore).
    
      if the excludedVolumes is provided, it should be a sequence of
      ExcludedVolume objects
    
      >>> m = Chem.MolFromSmiles('c1ccccc1C')
      >>> bounds = MolDG.GetMoleculeBoundsMatrix(m)
      >>> bounds.shape == (7, 7)
      True
      >>> m.GetNumConformers()
      0
      >>> EmbedMol(m,bounds,randomSeed=23)
      >>> m.GetNumConformers()
      1
    
    
      
    """
def EmbedOne(mol, name, match, pcophore, count = 1, silent = 0, **kwargs):
    """
     generates statistics for a molecule's embeddings
    
      Four energies are computed for each embedding:
          1) E1: the energy (with constraints) of the initial embedding
          2) E2: the energy (with constraints) of the optimized embedding
          3) E3: the energy (no constraints) the geometry for E2
          4) E4: the energy (no constraints) of the optimized free-molecule
             (starting from the E3 geometry)
    
      Returns a 9-tuple:
          1) the mean value of E1
          2) the sample standard deviation of E1
          3) the mean value of E2
          4) the sample standard deviation of E2
          5) the mean value of E3
          6) the sample standard deviation of E3
          7) the mean value of E4
          8) the sample standard deviation of E4
          9) The number of embeddings that failed
    
      
    """
def EmbedPharmacophore(mol, atomMatch, pcophore, randomSeed = -1, count = 10, smoothFirst = True, silent = False, bounds = None, excludedVolumes = None, targetNumber = -1, useDirs = False):
    """
     Generates one or more embeddings for a molecule that satisfy a pharmacophore
    
      atomMatch is a sequence of sequences containing atom indices
      for each of the pharmacophore's features.
    
        - count: is the maximum number of attempts to make a generating an embedding
        - smoothFirst: toggles triangle smoothing of the molecular bounds matix
        - bounds: if provided, should be the molecular bounds matrix. If this isn't
           provided, the matrix will be generated.
        - targetNumber: if this number is positive, it provides a maximum number
           of embeddings to generate (i.e. we'll have count attempts to generate
           targetNumber embeddings).
    
      returns: a 3 tuple:
        1) the molecular bounds matrix adjusted for the pharmacophore
        2) a list of embeddings (molecules with a single conformer)
        3) the number of failed attempts at embedding
    
        >>> from rdkit import Geometry
        >>> from rdkit.Chem.Pharm3D import Pharmacophore
        >>> m = Chem.MolFromSmiles('OCCN')
        >>> feats = [
        ...   ChemicalFeatures.FreeChemicalFeature('HBondAcceptor', 'HAcceptor1',
        ...                                        Geometry.Point3D(0.0, 0.0, 0.0)),
        ...   ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
        ...                                        Geometry.Point3D(2.65, 0.0, 0.0)),
        ...   ]
        >>> pcophore=Pharmacophore.Pharmacophore(feats)
        >>> pcophore.setLowerBound(0,1, 2.5)
        >>> pcophore.setUpperBound(0,1, 3.5)
        >>> atomMatch = ((0, ), (3, ))
    
        >>> bm,embeds,nFail = EmbedPharmacophore(m, atomMatch, pcophore, randomSeed=23, silent=1)
        >>> len(embeds)
        10
        >>> nFail
        0
    
        Set up a case that can't succeed:
    
        >>> pcophore = Pharmacophore.Pharmacophore(feats)
        >>> pcophore.setLowerBound(0,1, 2.0)
        >>> pcophore.setUpperBound(0,1, 2.1)
        >>> atomMatch = ((0, ), (3, ))
    
        >>> bm, embeds, nFail = EmbedPharmacophore(m, atomMatch, pcophore, randomSeed=23, silent=1)
        >>> len(embeds)
        0
        >>> nFail
        10
    
      
    """
def GetAllPharmacophoreMatches(matches, bounds, pcophore, useDownsampling = 0, progressCallback = None, use2DLimits = False, mol = None, verbose = False):
    ...
def GetAtomHeavyNeighbors(atom):
    """
     returns a list of the heavy-atom neighbors of the
      atom passed in:
    
      >>> m = Chem.MolFromSmiles('CCO')
      >>> l = GetAtomHeavyNeighbors(m.GetAtomWithIdx(0))
      >>> len(l)
      1
      >>> isinstance(l[0],Chem.Atom)
      True
      >>> l[0].GetIdx()
      1
    
      >>> l = GetAtomHeavyNeighbors(m.GetAtomWithIdx(1))
      >>> len(l)
      2
      >>> l[0].GetIdx()
      0
      >>> l[1].GetIdx()
      2
    
      
    """
def MatchFeatsToMol(mol, featFactory, features):
    """
     generates a list of all possible mappings of each feature to a molecule
    
      Returns a 2-tuple:
        1) a boolean indicating whether or not all features were found
        2) a list, numFeatures long, of sequences of features
    
    
        >>> import os.path
        >>> from rdkit import RDConfig, Geometry
        >>> fdefFile = os.path.join(RDConfig.RDCodeDir, 'Chem/Pharm3D/test_data/BaseFeatures.fdef')
        >>> featFactory = ChemicalFeatures.BuildFeatureFactory(fdefFile)
        >>> activeFeats = [
        ...  ChemicalFeatures.FreeChemicalFeature('Acceptor', Geometry.Point3D(0.0, 0.0, 0.0)),
        ...  ChemicalFeatures.FreeChemicalFeature('Donor', Geometry.Point3D(0.0, 0.0, 0.0))]
        >>> m = Chem.MolFromSmiles('FCCN')
        >>> match, mList = MatchFeatsToMol(m, featFactory, activeFeats)
        >>> match
        True
    
        Two feature types:
    
        >>> len(mList)
        2
    
        The first feature type, Acceptor, has two matches:
    
        >>> len(mList[0])
        2
        >>> mList[0][0].GetAtomIds()
        (0,)
        >>> mList[0][1].GetAtomIds()
        (3,)
    
        The first feature type, Donor, has a single match:
    
        >>> len(mList[1])
        1
        >>> mList[1][0].GetAtomIds()
        (3,)
    
      
    """
def MatchPharmacophore(matches, bounds, pcophore, useDownsampling = False, use2DLimits = False, mol = None, excludedVolumes = None, useDirs = False):
    """
    
    
      if use2DLimits is set, the molecule must also be provided and topological
      distances will also be used to filter out matches
    
      
    """
def MatchPharmacophoreToMol(mol, featFactory, pcophore):
    """
     generates a list of all possible mappings of a pharmacophore to a molecule
    
      Returns a 2-tuple:
        1) a boolean indicating whether or not all features were found
        2) a list, numFeatures long, of sequences of features
    
    
        >>> import os.path
        >>> from rdkit import Geometry, RDConfig
        >>> from rdkit.Chem.Pharm3D import Pharmacophore
        >>> fdefFile = os.path.join(RDConfig.RDCodeDir,'Chem/Pharm3D/test_data/BaseFeatures.fdef')
        >>> featFactory = ChemicalFeatures.BuildFeatureFactory(fdefFile)
        >>> activeFeats = [
        ...  ChemicalFeatures.FreeChemicalFeature('Acceptor', Geometry.Point3D(0.0, 0.0, 0.0)),
        ...  ChemicalFeatures.FreeChemicalFeature('Donor',Geometry.Point3D(0.0, 0.0, 0.0))]
        >>> pcophore= Pharmacophore.Pharmacophore(activeFeats)
        >>> m = Chem.MolFromSmiles('FCCN')
        >>> match, mList = MatchPharmacophoreToMol(m,featFactory,pcophore)
        >>> match
        True
    
        Two feature types:
    
        >>> len(mList)
        2
    
        The first feature type, Acceptor, has two matches:
    
        >>> len(mList[0])
        2
        >>> mList[0][0].GetAtomIds()
        (0,)
        >>> mList[0][1].GetAtomIds()
        (3,)
    
        The first feature type, Donor, has a single match:
    
        >>> len(mList[1])
        1
        >>> mList[1][0].GetAtomIds()
        (3,)
    
      
    """
def OptimizeMol(mol, bm, atomMatches = None, excludedVolumes = None, forceConstant = 1200.0, maxPasses = 5, verbose = False):
    """
      carries out a UFF optimization for a molecule optionally subject
      to the constraints in a bounds matrix
    
        - atomMatches, if provided, is a sequence of sequences
        - forceConstant is the force constant of the spring used to enforce
          the constraints
    
       returns a 2-tuple:
         1) the energy of the initial conformation
         2) the energy post-embedding
       NOTE that these energies include the energies of the constraints
    
        >>> from rdkit import Geometry
        >>> from rdkit.Chem.Pharm3D import Pharmacophore
        >>> m = Chem.MolFromSmiles('OCCN')
        >>> feats = [
        ...  ChemicalFeatures.FreeChemicalFeature('HBondAcceptor', 'HAcceptor1',
        ...                                       Geometry.Point3D(0.0, 0.0, 0.0)),
        ...  ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
        ...                                       Geometry.Point3D(2.65, 0.0, 0.0)),
        ...  ]
        >>> pcophore=Pharmacophore.Pharmacophore(feats)
        >>> pcophore.setLowerBound(0,1, 2.5)
        >>> pcophore.setUpperBound(0,1, 2.8)
        >>> atomMatch = ((0, ), (3, ))
        >>> bm, embeds, nFail = EmbedPharmacophore(m, atomMatch, pcophore, randomSeed=23, silent=1)
        >>> len(embeds)
        10
        >>> testM = embeds[0]
    
        Do the optimization:
    
        >>> e1, e2 = OptimizeMol(testM,bm,atomMatches=atomMatch)
    
        Optimizing should have lowered the energy:
    
        >>> e2 < e1
        True
    
        Check the constrained distance:
    
        >>> conf = testM.GetConformer(0)
        >>> p0 = conf.GetAtomPosition(0)
        >>> p3 = conf.GetAtomPosition(3)
        >>> d03 = p0.Distance(p3)
        >>> bool(d03 >= pcophore.getLowerBound(0,1) - 0.01)
        True
        >>> bool(d03 <= pcophore.getUpperBound(0,1) + 0.01)
        True
    
        If we optimize without the distance constraints (provided via the atomMatches
        argument) we're not guaranteed to get the same results, particularly in a case
        like the current one where the pharmacophore brings the atoms uncomfortably
        close together:
    
        >>> testM = embeds[1]
        >>> e1, e2 = OptimizeMol(testM,bm)
        >>> e2 < e1
        True
        >>> conf = testM.GetConformer(0)
        >>> p0 = conf.GetAtomPosition(0)
        >>> p3 = conf.GetAtomPosition(3)
        >>> d03 = p0.Distance(p3)
        >>> bool(d03 >= pcophore.getLowerBound(0, 1) - 0.01)
        True
        >>> bool(d03 <= pcophore.getUpperBound(0, 1) + 0.01)
        False
    
      
    """
def ReplaceGroup(match, bounds, slop = 0.01, useDirs = False, dirLength = 2.0):
    """
     Adds an entry at the end of the bounds matrix for a point at
       the center of a multi-point feature
    
       returns a 2-tuple:
         new bounds mat
         index of point added
    
       >>> boundsMat = numpy.array([[0.0, 2.0, 2.0],[1.0, 0.0, 2.0],[1.0, 1.0, 0.0]])
       >>> match = [0, 1, 2]
       >>> bm,idx = ReplaceGroup(match, boundsMat, slop=0.0)
    
       the index is at the end:
    
       >>> idx == 3
       True
    
       and the matrix is one bigger:
    
       >>> bm.shape == (4, 4)
       True
    
       but the original bounds mat is not altered:
    
       >>> boundsMat.shape == (3, 3)
       True
    
    
       We make the assumption that the points of the
       feature form a regular polygon, are listed in order
       (i.e. pt 0 is a neighbor to pt 1 and pt N-1)
       and that the replacement point goes at the center:
    
       >>> print(', '.join([f'{x:.3f}' for x in bm[-1]]))
       0.577, 0.577, 0.577, 0.000
       >>> print(', '.join([f'{x:.3f}' for x in bm[:,-1]]))
       1.155, 1.155, 1.155, 0.000
    
       The slop argument (default = 0.01) is fractional:
    
       >>> bm, idx = ReplaceGroup(match, boundsMat)
       >>> print(', '.join([f'{x:.3f}' for x in bm[-1]]))
       0.572, 0.572, 0.572, 0.000
       >>> print(', '.join([f'{x:.3f}' for x in bm[:,-1]]))
       1.166, 1.166, 1.166, 0.000
    
      
    """
def UpdatePharmacophoreBounds(bm, atomMatch, pcophore, useDirs = False, dirLength = 2.0, mol = None):
    """
     loops over a distance bounds matrix and replaces the elements
      that are altered by a pharmacophore
    
      **NOTE** this returns the resulting bounds matrix, but it may also
      alter the input matrix
    
      atomMatch is a sequence of sequences containing atom indices
      for each of the pharmacophore's features.
    
        >>> from rdkit import Geometry
        >>> from rdkit.Chem.Pharm3D import Pharmacophore
        >>> feats = [
        ...   ChemicalFeatures.FreeChemicalFeature('HBondAcceptor', 'HAcceptor1',
        ...                                        Geometry.Point3D(0.0, 0.0, 0.0)),
        ...   ChemicalFeatures.FreeChemicalFeature('HBondDonor', 'HDonor1',
        ...                                        Geometry.Point3D(2.65, 0.0, 0.0)),
        ...   ]
        >>> pcophore = Pharmacophore.Pharmacophore(feats)
        >>> pcophore.setLowerBound(0,1, 1.0)
        >>> pcophore.setUpperBound(0,1, 2.0)
    
        >>> boundsMat = numpy.array([[0.0, 3.0, 3.0],[2.0, 0.0, 3.0],[2.0, 2.0, 0.0]])
        >>> atomMatch = ((0, ), (1, ))
        >>> bm = UpdatePharmacophoreBounds(boundsMat, atomMatch, pcophore)
    
    
         In this case, there are no multi-atom features, so the result matrix
         is the same as the input:
    
         >>> bm is boundsMat
         True
    
         this means, of course, that the input boundsMat is altered:
    
         >>> print(', '.join([f'{x:.3f}' for x in boundsMat[0]]))
         0.000, 2.000, 3.000
         >>> print(', '.join([f'{x:.3f}' for x in boundsMat[1]]))
         1.000, 0.000, 3.000
         >>> print(', '.join([f'{x:.3f}' for x in boundsMat[2]]))
         2.000, 2.000, 0.000
    
      
    """
def _checkMatch(match, mol, bounds, pcophore, use2DLimits):
    """
     **INTERNAL USE ONLY**
    
      checks whether a particular atom match can be satisfied by
      a molecule
    
      
    """
def _getFeatDict(mol, featFactory, features):
    """
     **INTERNAL USE ONLY**
    
        >>> import os.path
        >>> from rdkit import Geometry, RDConfig, Chem
        >>> fdefFile = os.path.join(RDConfig.RDCodeDir, 'Chem/Pharm3D/test_data/BaseFeatures.fdef')
        >>> featFactory = ChemicalFeatures.BuildFeatureFactory(fdefFile)
        >>> activeFeats = [
        ...  ChemicalFeatures.FreeChemicalFeature('Acceptor', Geometry.Point3D(0.0, 0.0, 0.0)),
        ...  ChemicalFeatures.FreeChemicalFeature('Donor', Geometry.Point3D(0.0, 0.0, 0.0))]
        >>> m = Chem.MolFromSmiles('FCCN')
        >>> d = _getFeatDict(m, featFactory, activeFeats)
        >>> sorted(list(d.keys()))
        ['Acceptor', 'Donor']
        >>> donors = d['Donor']
        >>> len(donors)
        1
        >>> donors[0].GetAtomIds()
        (3,)
        >>> acceptors = d['Acceptor']
        >>> len(acceptors)
        2
        >>> acceptors[0].GetAtomIds()
        (0,)
        >>> acceptors[1].GetAtomIds()
        (3,)
    
      
    """
def _runDoctests(verbose = None):
    ...
def isNaN(v):
    """
     provides an OS independent way of detecting NaNs
      This is intended to be used with values returned from the C++
      side of things.
    
      We can't actually test this from Python (which traps
      zero division errors), but it would work something like
      this if we could:
    
      >>> isNaN(0)
      False
    
      #>>> isNan(1/0)
      #True
    
      
    """
_times: dict = {}
defaultFeatLength: float = 2.0
logger: rdkit.RDLogger.logger  # value = <rdkit.RDLogger.logger object>

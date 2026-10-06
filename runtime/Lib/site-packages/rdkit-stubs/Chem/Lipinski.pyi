"""
 Calculation of Lipinski parameters for molecules

"""
from __future__ import annotations
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors
import rdkit.Chem.rdchem
__all__: list[str] = ['Chem', 'HAcceptorSmarts', 'HDonorSmarts', 'HeavyAtomCount', 'HeteroatomSmarts', 'NHOHSmarts', 'NOCountSmarts', 'RotatableBondSmarts', 'nm', 'rdMolDescriptors', 'txt']
def HeavyAtomCount(mol):
    """
     Number of heavy atoms a molecule.
    """
HAcceptorSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
HDonorSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
HeteroatomSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
NHOHSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
NOCountSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
RotatableBondSmarts: rdkit.Chem.rdchem.Mol  # value = <rdkit.Chem.rdchem.Mol object>
_bulkConvert: tuple = ('CalcFractionCSP3', 'CalcNumAromaticRings', 'CalcNumSaturatedRings', 'CalcNumAromaticHeterocycles', 'CalcNumAromaticCarbocycles', 'CalcNumSaturatedHeterocycles', 'CalcNumSaturatedCarbocycles', 'CalcNumAliphaticRings', 'CalcNumAliphaticHeterocycles', 'CalcNumAliphaticCarbocycles', 'CalcNumHeterocycles', 'CalcNumBridgeheadAtoms', 'CalcNumAmideBonds', 'CalcNumAtomStereoCenters', 'CalcNumHeterocycles', 'CalcNumUnspecifiedAtomStereoCenters', 'CalcNumSpiroAtoms', 'CalcPhi')
nm: str = 'Phi'
txt: str = 'CalcPhi'

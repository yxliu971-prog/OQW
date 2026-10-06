from __future__ import annotations
from rdkit.Chem import fmcs
from rdkit.Chem.fmcs.fmcs import Default
import warnings as warnings
__all__: list = ['FindMCS']
class MCSResult:
    def __init__(self, obj):
        ...
    def __nonzero__(self):
        ...
    def __repr__(self):
        ...
    def __str__(self):
        ...
def FindMCS(mols, minNumAtoms = 2, maximize = 'bonds', atomCompare = 'elements', bondCompare = 'bondtypes', matchValences = False, ringMatchesRingOnly = False, completeRingsOnly = False, timeout = None, threshold = None):
    """
    Find the maximum common substructure of a set of molecules
    
        ***************************************************
        NB: rdkit.Chem.MCS module is deprecated; please use
        rdkit.Chem.rdFMCS instead.
        ***************************************************
    
        In the simplest case, pass in a list of molecules and get back
        an MCSResult object which describes the MCS:
    
        >>> from rdkit import Chem
        >>> mols = [Chem.MolFromSmiles("C#CCP"), Chem.MolFromSmiles("C=CCO")]
        >>> from rdkit.Chem import MCS
        >>> MCS.FindMCS(mols)
        MCSResult(numAtoms=2, numBonds=1, smarts='[#6]-[#6]', completed=1)
    
        The SMARTS '[#6]-[#6]' matches the largest common substructure of
        the input structures. It has 2 atoms and 1 bond. If there is no
        MCS which is at least `minNumAtoms` in size then the result will set
        numAtoms and numBonds to -1 and set smarts to None.
    
        By default, two atoms match if they are the same element and two
        bonds match if they have the same bond type. Specify `atomCompare`
        and `bondCompare` to use different comparison functions, as in:
    
        >>> MCS.FindMCS(mols, atomCompare="any")
        MCSResult(numAtoms=3, numBonds=2, smarts='[*]-[*]-[*]', completed=1)
        >>> MCS.FindMCS(mols, bondCompare="any")
        MCSResult(numAtoms=3, numBonds=2, smarts='[#6]~[#6]~[#6]', completed=1)
    
        An atomCompare of "any" says that any atom matches any other atom,
        "elements" compares by element type, and "isotopes" matches based on
        the isotope label. Isotope labels can be used to implement user-defined
        atom types. A bondCompare of "any" says that any bond matches any
        other bond, and "bondtypes" says bonds are equivalent if and only if
        they have the same bond type.
    
        A substructure has both atoms and bonds. The default `maximize`
        setting of "atoms" finds a common substructure with the most number
        of atoms. Use maximize="bonds" to maximize the number of bonds.
        Maximizing the number of bonds tends to maximize the number of rings,
        although two small rings may have fewer bonds than one large ring.
    
        You might not want a 3-valent nitrogen to match one which is 5-valent.
        The default `matchValences` value of False ignores valence information.
        When True, the atomCompare setting is modified to also require that
        the two atoms have the same valency.
    
        >>> MCS.FindMCS(mols, matchValences=True)
        MCSResult(numAtoms=2, numBonds=1, smarts='[#6v4]-[#6v4]', completed=1)
    
        It can be strange to see a linear carbon chain match a carbon ring,
        which is what the `ringMatchesRingOnly` default of False does. If
        you set it to True then ring bonds will only match ring bonds.
    
        >>> mols = [Chem.MolFromSmiles("C1CCC1CCC"), Chem.MolFromSmiles("C1CCCCCC1")]
        >>> MCS.FindMCS(mols)
        MCSResult(numAtoms=7, numBonds=6, smarts='[#6]-[#6]-[#6]-[#6]-[#6]-[#6]-[#6]', completed=1)
        >>> MCS.FindMCS(mols, ringMatchesRingOnly=True)
        MCSResult(numAtoms=4, numBonds=3, smarts='[#6](-@[#6])-@[#6]-@[#6]', completed=1)
    
        You can further restrict things and require that partial rings
        (as in this case) are not allowed. That is, if an atom is part of
        the MCS and the atom is in a ring of the entire molecule then
        that atom is also in a ring of the MCS. Set `completeRingsOnly`
        to True to toggle this requirement and also sets ringMatchesRingOnly
        to True.
    
        >>> mols = [Chem.MolFromSmiles("CCC1CC2C1CN2"), Chem.MolFromSmiles("C1CC2C1CC2")]
        >>> MCS.FindMCS(mols)
        MCSResult(numAtoms=6, numBonds=6, smarts='[#6]-1-[#6]-[#6](-[#6])-[#6]-1-[#6]', completed=1)
        >>> MCS.FindMCS(mols, ringMatchesRingOnly=True)
        MCSResult(numAtoms=5, numBonds=5, smarts='[#6]-@1-@[#6]-@[#6](-@[#6])-@[#6]-@1', completed=1)
        >>> MCS.FindMCS(mols, completeRingsOnly=True)
        MCSResult(numAtoms=4, numBonds=4, smarts='[#6]-@1-@[#6]-@[#6]-@[#6]-@1', completed=1)
    
        The MCS algorithm will exhaustively search for a maximum common substructure.
        Typically this takes a fraction of a second, but for some comparisons this
        can take minutes or longer. Use the `timeout` parameter to stop the search
        after the given number of seconds (wall-clock seconds, not CPU seconds) and
        return the best match found in that time. If timeout is reached then the
        `completed` property of the MCSResult will be 0 instead of 1.
    
        >>> mols = [Chem.MolFromSmiles("Nc1ccccc1"*100), Chem.MolFromSmiles("Nc1ccccccccc1"*100)]
        >>> MCS.FindMCS(mols, timeout=0.1)
        MCSResult(..., completed=0)
    
        (The MCS after 50 seconds contained 511 atoms.)
        
    """
def _test():
    ...

"""
 Definitions for 2D Pharmacophores from:
  Gobbi and Poppinger, Biotech. Bioeng. _61_ 47-54 (1998)

"""
from __future__ import annotations
from rdkit.Chem import ChemicalFeatures
import rdkit.Chem.Pharm2D.SigFactory
from rdkit.Chem.Pharm2D.SigFactory import SigFactory
__all__: list[str] = ['ChemicalFeatures', 'SigFactory', 'defaultBins', 'factory', 'fdef']
def _init():
    ...
defaultBins: list = [(2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 100)]
factory: rdkit.Chem.Pharm2D.SigFactory.SigFactory  # value = <rdkit.Chem.Pharm2D.SigFactory.SigFactory object>
fdef: str = '\nDefineFeature Hydrophobic [$([C;H2,H1](!=*)[C;H2,H1][C;H2,H1][$([C;H1,H2,H3]);!$(C=*)]),$(C([C;H2,H3])([C;H2,H3])[C;H2,H3])]\n  Family LH\n  Weights 1.0\nEndFeature\nDefineFeature Donor [$([N;!H0;v3]),$([N;!H0;+1;v4]),$([O,S;H1;+0]),$([n;H1;+0])]\n  Family HD\n  Weights 1.0\nEndFeature\nDefineFeature Acceptor [$([O,S;H1;v2]-[!$(*=[O,N,P,S])]),$([O,S;H0;v2]),$([O,S;-]),$([N&v3;H1,H2]-[!$(*=[O,N,P,S])]),$([N;v3;H0]),$([n,o,s;+0]),F]\n  Family HA\n  Weights 1.0\nEndFeature\nDefineFeature AromaticAttachment [$([a;D3](@*)(@*)*)]\n  Family AR\n  Weights 1.0\nEndFeature\nDefineFeature AliphaticAttachment [$([A;D3](@*)(@*)*)]\n  Family RR\n  Weights 1.0\nEndFeature\nDefineFeature UnusualAtom [!#1;!#6;!#7;!#8;!#9;!#16;!#17;!#35;!#53]\n  Family X\n  Weights 1.0\nEndFeature\nDefineFeature BasicGroup [$([N;H2&+0][$([C,a]);!$([C,a](=O))]),$([N;H1&+0]([$([C,a]);!$([C,a](=O))])[$([C,a]);!$([C,a](=O))]),$([N;H0&+0]([C;!$(C(=O))])([C;!$(C(=O))])[C;!$(C(=O))]),$([N,n;X2;+0])]\n  Family BG\n  Weights 1.0\nEndFeature\nDefineFeature AcidicGroup [$([C,S](=[O,S,P])-[O;H1])]\n  Family AG\n  Weights 1.0\nEndFeature\n'

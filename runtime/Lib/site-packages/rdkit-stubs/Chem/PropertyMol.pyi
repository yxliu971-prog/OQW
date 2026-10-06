from __future__ import annotations
from rdkit import Chem
import rdkit.Chem.rdchem
import typing
__all__: list[str] = ['Chem', 'PropertyMol']
class PropertyMol(rdkit.Chem.rdchem.Mol):
    """
     allows rdkit molecules to be pickled with their properties saved.
    
         >>> import os
         >>> import pickle
         >>> from rdkit import RDConfig
         >>> m = Chem.MolFromMolFile(os.path.join(RDConfig.RDCodeDir, 'Chem', 'test_data/benzene.mol'))
         >>> m.GetProp('_Name')
         'benzene.mol'
    
         by default pickling removes properties:
    
         >>> m2 = pickle.loads(pickle.dumps(m))
         >>> m2.HasProp('_Name')
         0
    
         Property mols solve this:
    
         >>> pm = PropertyMol(m)
         >>> pm.GetProp('_Name')
         'benzene.mol'
         >>> pm.SetProp('MyProp','foo')
         >>> pm.HasProp('MyProp')
         1
    
         >>> pm2 = pickle.loads(pickle.dumps(pm))
         >>> Chem.MolToSmiles(pm2)
         'c1ccccc1'
         >>> pm2.GetProp('_Name')
         'benzene.mol'
         >>> pm2.HasProp('MyProp')
         1
         >>> pm2.GetProp('MyProp')
         'foo'
         >>> pm2.HasProp('MissingProp')
         0
    
         Property mols are a bit more permissive about the types
         of property values:
    
         >>> pm.SetProp('IntVal',1)
    
         That wouldn't work with a standard mol
    
         but the Property mols still convert all values to strings before storing:
    
         >>> pm.GetProp('IntVal')
         '1'
    
         This is a test for sf.net issue 2880943: make sure properties end up in SD files:
    
         >>> import tempfile, os
         >>> fn = tempfile.NamedTemporaryFile(suffix='.sdf', delete=False).name
         >>> w = Chem.SDWriter(fn)
         >>> w.write(pm)
         >>> w=None
         >>> with open(fn,'r') as inf:
         ...   txt = inf.read()
         >>> '<IntVal>' in txt
         True
         >>> try:
         ...   os.unlink(fn)
         ... except Exception:
         ...   pass
    
         The next level of that bug: does writing a *depickled* propertymol
         to an SD file include properties:
    
         >>> fn = tempfile.NamedTemporaryFile(suffix='.sdf', delete=False).name
         >>> w = Chem.SDWriter(fn)
         >>> pm = pickle.loads(pickle.dumps(pm))
         >>> w.write(pm)
         >>> w=None
         >>> with open(fn,'r') as inf:
         ...   txt = inf.read()
         >>> '<IntVal>' in txt
         True
         >>> try:
         ...   os.unlink(fn)
         ... except Exception:
         ...   pass
    
    
    
        
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    def SetProp(self, nm, val):
        ...
    def __getstate__(self):
        ...
    def __init__(self, mol):
        ...
    def __setstate__(self, stateD):
        ...
def _test():
    ...

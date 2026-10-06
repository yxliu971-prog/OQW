from __future__ import annotations
import rdkit.Chem
import typing
__all__: list[str] = ['Deprotect', 'DeprotectData', 'DeprotectDataVect', 'DeprotectInPlace', 'GetDeprotections']
class DeprotectData(Boost.Python.instance):
    """
    DeprotectData class, contains a single deprotection reaction and information
    
     deprotectdata.deprotection_class - functional group being protected
     deprotectdata.reaction_smarts - reaction smarts used for deprotection
     deprotectdata.abbreviation - common abbreviation for the protecting group
     deprotectdata.full_name - full name for the protecting group
    
    
    """
    __instance_size__: typing.ClassVar[int] = 200
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self, deprotection_class: str, reaction_smarts: str, abbreviation: str, full_name: str) -> None:
        """
            Construct a new DeprotectData instance.
              >>> reaction_class = "amine"
              >>> reaction_smarts = "[C;R0][C;R0]([C;R0])([O;R0][C;R0](=[O;R0])[NX3;H0,H1:1])C>>[N:1]"
              >>> abbreviation = "Boc"
              >>> full_name = "tert-butyloxycarbonyl"
              >>> data = DeprotectData(reaction_class, reaction_smarts, abbreviation, full_name)
              >>> assert data.isValid()
            
            
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def isValid(self) -> bool:
        """
            Returns True if the DeprotectData has a valid reaction
        
            C++ signature :
                bool isValid(struct RDKit::Deprotect::DeprotectData {lvalue})
        """
    @property
    def abbreviation(*args, **kwargs):
        ...
    @property
    def deprotection_class(*args, **kwargs):
        ...
    @property
    def example(*args, **kwargs):
        ...
    @property
    def full_name(*args, **kwargs):
        ...
    @property
    def reaction_smarts(*args, **kwargs):
        ...
class DeprotectDataVect(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __contains__(self, item: typing.Any) -> bool:
        """
            C++ signature :
                bool __contains__(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue},struct _object * __ptr64)
        """
    def __delitem__(self, item: typing.Any) -> None:
        """
            C++ signature :
                void __delitem__(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue},struct _object * __ptr64)
        """
    def __getitem__(self, item: typing.Any) -> typing.Any:
        """
            C++ signature :
                class boost::python::api::object __getitem__(struct boost::python::back_reference<class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > & __ptr64>,struct _object * __ptr64)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    def __iter__(self) -> typing.Any:
        """
            C++ signature :
                struct boost::python::objects::iterator_range<struct boost::python::return_internal_reference<1,struct boost::python::default_call_policies>,class std::_Vector_iterator<class std::_Vector_val<struct std::_Simple_types<struct RDKit::Deprotect::DeprotectData> > > > __iter__(struct boost::python::back_reference<class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > & __ptr64>)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned __int64 __len__(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue})
        """
    def __setitem__(self, item: typing.Any, value: typing.Any) -> None:
        """
            C++ signature :
                void __setitem__(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue},struct _object * __ptr64,struct _object * __ptr64)
        """
    def append(self, item: typing.Any) -> None:
        """
            C++ signature :
                void append(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue},class boost::python::api::object)
        """
    def extend(self, other: typing.Any) -> None:
        """
            C++ signature :
                void extend(class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > {lvalue},class boost::python::api::object)
        """
def Deprotect(mol: Mol, deprotections: typing.Any = None) -> rdkit.Chem.Mol:
    """
        Return the deprotected version of the molecule.
    
        C++ signature :
            class boost::shared_ptr<class RDKit::ROMol> Deprotect(class RDKit::ROMol [,class boost::python::api::object=None])
    """
def DeprotectInPlace(mol: Mol, deprotections: typing.Any = None) -> bool:
    """
        Deprotects the molecule in place.
    
        C++ signature :
            bool DeprotectInPlace(class RDKit::ROMol {lvalue} [,class boost::python::api::object=None])
    """
def GetDeprotections() -> DeprotectDataVect:
    """
        Return the default list of deprotections
    
        C++ signature :
            class std::vector<struct RDKit::Deprotect::DeprotectData,class std::allocator<struct RDKit::Deprotect::DeprotectData> > GetDeprotections()
    """

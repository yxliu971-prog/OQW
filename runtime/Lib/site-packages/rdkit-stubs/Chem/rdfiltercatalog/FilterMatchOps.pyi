from __future__ import annotations
import rdkit.Chem.rdfiltercatalog
import typing
__all__: list[str] = ['And', 'Not', 'Or']
class And(rdkit.Chem.rdfiltercatalog.FilterMatcherBase):
    __instance_size__: typing.ClassVar[int] = 112
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self, arg1: FilterMatcherBase, arg2: FilterMatcherBase) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class RDKit::FilterMatcherBase {lvalue},class RDKit::FilterMatcherBase {lvalue})
        """
class Not(rdkit.Chem.rdfiltercatalog.FilterMatcherBase):
    __instance_size__: typing.ClassVar[int] = 96
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self, arg1: FilterMatcherBase) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class RDKit::FilterMatcherBase {lvalue})
        """
class Or(rdkit.Chem.rdfiltercatalog.FilterMatcherBase):
    __instance_size__: typing.ClassVar[int] = 112
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __init__(self, arg1: FilterMatcherBase, arg2: FilterMatcherBase) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class RDKit::FilterMatcherBase {lvalue},class RDKit::FilterMatcherBase {lvalue})
        """

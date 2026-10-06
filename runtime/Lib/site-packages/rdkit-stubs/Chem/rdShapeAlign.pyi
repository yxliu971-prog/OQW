from __future__ import annotations
import typing
__all__: list[str] = ['AlignMol', 'AlignShapes', 'FloatVector', 'PrepareConformer', 'ScoreMol', 'ScoreShape', 'ShapeInput', 'ShapeInputOptions', 'TransformConformer']
class FloatVector(Boost.Python.instance):
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __contains__(self, item: typing.Any) -> bool:
        """
            C++ signature :
                bool __contains__(class std::vector<float,class std::allocator<float> > {lvalue},struct _object * __ptr64)
        """
    def __delitem__(self, item: typing.Any) -> None:
        """
            C++ signature :
                void __delitem__(class std::vector<float,class std::allocator<float> > {lvalue},struct _object * __ptr64)
        """
    def __getitem__(self, item: typing.Any) -> typing.Any:
        """
            C++ signature :
                class boost::python::api::object __getitem__(struct boost::python::back_reference<class std::vector<float,class std::allocator<float> > & __ptr64>,struct _object * __ptr64)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
    def __iter__(self) -> typing.Any:
        """
            C++ signature :
                struct boost::python::objects::iterator_range<struct boost::python::return_value_policy<struct boost::python::return_by_value,struct boost::python::default_call_policies>,class std::_Vector_iterator<class std::_Vector_val<struct std::_Simple_types<float> > > > __iter__(struct boost::python::back_reference<class std::vector<float,class std::allocator<float> > & __ptr64>)
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned __int64 __len__(class std::vector<float,class std::allocator<float> > {lvalue})
        """
    def __setitem__(self, item: typing.Any, value: typing.Any) -> None:
        """
            C++ signature :
                void __setitem__(class std::vector<float,class std::allocator<float> > {lvalue},struct _object * __ptr64,struct _object * __ptr64)
        """
    def append(self, item: typing.Any) -> None:
        """
            C++ signature :
                void append(class std::vector<float,class std::allocator<float> > {lvalue},class boost::python::api::object)
        """
    def extend(self, other: typing.Any) -> None:
        """
            C++ signature :
                void extend(class std::vector<float,class std::allocator<float> > {lvalue},class boost::python::api::object)
        """
class ShapeInput(Boost.Python.instance):
    @staticmethod
    def __init__(*args, **kwargs):
        """
        Raises an exception
        This class cannot be instantiated from Python
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @property
    def alpha_vector(*args, **kwargs):
        ...
    @alpha_vector.setter
    def alpha_vector(*args, **kwargs):
        ...
    @property
    def atom_type_vector(*args, **kwargs):
        ...
    @atom_type_vector.setter
    def atom_type_vector(*args, **kwargs):
        ...
    @property
    def coord(*args, **kwargs):
        ...
    @coord.setter
    def coord(*args, **kwargs):
        ...
    @property
    def inertialRot(*args, **kwargs):
        """
        Rotation applied to put the shape into its principal axes frame of reference.
        """
    @property
    def shift(*args, **kwargs):
        """
        Translation of centre of shape coordinates to origin.
        """
    @shift.setter
    def shift(*args, **kwargs):
        ...
    @property
    def sof(*args, **kwargs):
        ...
    @sof.setter
    def sof(*args, **kwargs):
        ...
    @property
    def sov(*args, **kwargs):
        ...
    @sov.setter
    def sov(*args, **kwargs):
        ...
    @property
    def volumeAtomIndexVector(*args, **kwargs):
        ...
    @volumeAtomIndexVector.setter
    def volumeAtomIndexVector(*args, **kwargs):
        ...
class ShapeInputOptions(Boost.Python.instance):
    """
    Shape Input Options
    """
    __instance_size__: typing.ClassVar[int] = 144
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
    def atomRadii(*args, **kwargs):
        """
        Non-standard radii to use for the atoms specified by their indices in the molecule.  A list of tuples of [int, float].
        """
    @atomRadii.setter
    def atomRadii(*args, **kwargs):
        ...
    @property
    def atomSubset(*args, **kwargs):
        """
        If not empty, use just these atoms in the molecule to form the ShapeInput object.
        """
    @atomSubset.setter
    def atomSubset(*args, **kwargs):
        ...
    @property
    def customFeatures(*args, **kwargs):
        """
        Custom features for the shape.
        """
    @customFeatures.setter
    def customFeatures(*args, **kwargs):
        ...
    @property
    def dummyRadius(*args, **kwargs):
        """
        If using dummy atoms in the alignment, what radius to use for them.  Default=2.16 (the radius of Xe).
        """
    @dummyRadius.setter
    def dummyRadius(*args, **kwargs):
        ...
    @property
    def includeDummies(*args, **kwargs):
        """
        Whether to use dummy atoms in the alignment. Default=False.
        """
    @includeDummies.setter
    def includeDummies(*args, **kwargs):
        ...
    @property
    def normalize(*args, **kwargs):
        """
        Whether to normalise the shape by putting intoits inertial frame.  Default=True.
        """
    @normalize.setter
    def normalize(*args, **kwargs):
        ...
    @property
    def notColorAtoms(*args, **kwargs):
        """
        Any atoms mentioned here by index should not be used in a color feature.
        """
    @notColorAtoms.setter
    def notColorAtoms(*args, **kwargs):
        ...
    @property
    def useColors(*args, **kwargs):
        """
        Whether to use colors (pharmacophore features) in the score.  Default=True.
        """
    @useColors.setter
    def useColors(*args, **kwargs):
        ...
@typing.overload
def AlignMol(ref: Mol, probe: Mol, refConfId: int = -1, probeConfId: int = -1, useColors: bool = True, opt_param: float = 1.0, max_preiters: int = 10, max_postiters: int = 30) -> tuple:
    """
        Aligns a probe molecule to a reference molecule. The probe is modified.
        
        Parameters
        ----------
        ref : RDKit.ROMol
            Reference molecule
        probe : RDKit.ROMol
            Probe molecule
        refConfId : int, optional
            Reference conformer ID (default is -1)
        probeConfId : int, optional
            Probe conformer ID (default is -1)
        useColors : bool, optional
            Whether or not to use colors in the scoring (default is True)
        opt_param : float, optional
            Balance of shape and color for optimization.
            0 is only color, 0.5 is equal weight, and 1.0 is only shape.
            Default is 1.0.
        max_preiters : int, optional
            In the two phase optimization, the maximum iterations done on all poses.
        max_postiters : int, optional
            In the two phase optimization, the maximum iterations during the second phase on
            only the best poses from the first phase
        
        
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if opt_param is 1.0.
    
        C++ signature :
            class boost::python::tuple AlignMol(class RDKit::ROMol,class RDKit::ROMol {lvalue} [,int=-1 [,int=-1 [,bool=True [,double=1.0 [,unsigned int=10 [,unsigned int=30]]]]]])
    """
@typing.overload
def AlignMol(ref: Mol, probe: Mol, refShapeOpts: ShapeInputOptions, probeShapeOpts: ShapeInputOptions, refConfId: int = -1, probeConfId: int = -1, opt_param: float = 1.0, max_preiters: int = 10, max_postiters: int = 30) -> tuple:
    """
        Aligns a probe molecule to a reference molecule. The probe is modified.
        
        Parameters
        ----------
        ref : RDKit.ROMol
            Reference molecule
        probe : RDKit.ROMol
            Probe molecule
        refShapeOpts : ShapeInputOptions
            Options for constructing the shape for the reference molecule
        probeShapeOpts : ShapeInputOptions
            Options for constructing the shape for the probe molecule
        refConfId : int, optional
            Reference conformer ID (default is -1)
        probeConfId : int, optional
            Probe conformer ID (default is -1)
        opt_param : float, optional
            Balance of shape and color for optimization.
            0 is only color, 0.5 is equal weight, and 1.0 is only shape.
            Default is 1.0.
        max_preiters : int, optional
            In the two phase optimization, the maximum iterations done on all poses.
        max_postiters : int, optional
            In the two phase optimization, the maximum iterations during the second phase on
            only the best poses from the first phase
        
        
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if opt_param is 1.0.
    
        C++ signature :
            class boost::python::tuple AlignMol(class RDKit::ROMol,class RDKit::ROMol {lvalue},struct ShapeInputOptions,struct ShapeInputOptions [,int=-1 [,int=-1 [,double=1.0 [,unsigned int=10 [,unsigned int=30]]]]])
    """
@typing.overload
def AlignMol(refShape: ShapeInput, probe: Mol, probeConfId: int = -1, useColors: bool = True, opt_param: float = 1.0, max_preiters: int = 10, max_postiters: int = 30, applyRefShift: bool = False) -> tuple:
    """
        Aligns a probe molecule to a reference shape. The probe is modified.
        Assumes the shapes are both centred on the origin.
        
        Parameters
        ----------
        refShape : ShapeInput
            Reference shape
        probe : RDKit.ROMol
            Probe molecule
        probeConfId : int, optional
            Probe conformer ID (default is -1)
        useColors : bool, optional
            Whether or not to use colors in the scoring (default is True)
        opt_param : float, optional
            Balance of shape and color for optimization.
            0 is only color, 0.5 is equal weight, and 1.0 is only shape.
            Default is 1.0.
        max_preiters : int, optional
            In the two phase optimization, the maximum iterations done on all poses.
        max_postiters : int, optional
            In the two phase optimization, the maximum iterations during the second phase on
            only the best poses from the first phase
        applyRefShift : bool, optional
            If True, apply the reference shape's shift translation to the final
            coordinates.
        
        
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if opt_param is 1.0.
    
        C++ signature :
            class boost::python::tuple AlignMol(struct ShapeInput,class RDKit::ROMol {lvalue} [,int=-1 [,bool=True [,double=1.0 [,unsigned int=10 [,unsigned int=30 [,bool=False]]]]]])
    """
def AlignShapes(refShape: ShapeInput, probeShape: ShapeInput, opt_param: float = 1.0, max_preiters: int = 10, max_postiters: int = 30) -> tuple:
    """
        Aligns a probe shape to a reference shape. The probe is modified.
        
        Parameters
        ----------
        refShape : ShapeInput
            Reference shape
        probeShape : ShapeInput
            Probe shape
        opt_param : float, optional
            Balance of shape and color for optimization.
            0 is only color, 0.5 is equal weight, and 1.0 is only shape
        max_preiters : int, optional
            In the two phase optimization, the maximum iterations done on all poses.
        max_postiters : int, optional
            In the two phase optimization, the maximum iterations during the second phase on
            only the best poses from the first phase
        
        
        Returns
        -------
         3-tuple of double, double, list of doubles
            The results are (shape_score, color_score, matrix)
            The matrix is a 12-float list giving the transformation matrix that
            overlays the probe onto the reference.
    
        C++ signature :
            class boost::python::tuple AlignShapes(struct ShapeInput,struct ShapeInput {lvalue} [,double=1.0 [,unsigned int=10 [,unsigned int=30]]])
    """
def PrepareConformer(mol: Mol, confId: int = -1, opts: typing.Any = None) -> ShapeInput:
    """
        Generates a ShapeInput object for a molecule
        
        Parameters
        ----------
        mol : RDKit.ROMol
            Reference molecule
        confId : int, optional
            Conformer ID to use (default is -1)
        opts : ShapeInputOptions, optional
            Options for Shapeinput
        
        Returns
        -------
         a ShapeInput for the molecule
    
        C++ signature :
            struct ShapeInput * __ptr64 PrepareConformer(class RDKit::ROMol [,int=-1 [,class boost::python::api::object=None]])
    """
@typing.overload
def ScoreMol(mol1: Mol, mol2: Mol, mol1ShapeOpts: ShapeInputOptions, mol2ShapeOpts: ShapeInputOptions, mol1ConfId: int = -1, mol2ConfId: int = -1) -> tuple:
    """
        Calculate the scores between a shape and a molecule without moving them.
        
        Parameters
        ----------
        mol1 : RDKit.ROMol
            First molecule
        mol2 : RDKit.ROMol
            Second molecule
        mol1ShapeOptions:
            Options for constructing the shape for molecule 1
        mol2ShapeOptions:
            Options for constructing the shape for molecule 2
        mol1ConfId : int, optional
            First molecule conformer ID (default is -1)
        mol2ConfId : int, optional
            Second conformer ID (default is -1)
        
        
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if useColors is False for either of the
        shape options
    
        C++ signature :
            class boost::python::tuple ScoreMol(class RDKit::ROMol,class RDKit::ROMol {lvalue},struct ShapeInputOptions,struct ShapeInputOptions [,int=-1 [,int=-1]])
    """
@typing.overload
def ScoreMol(shape: ShapeInput, mol: Mol, molShapeOpts: ShapeInputOptions, molConfId: int = -1) -> tuple:
    """
        Calculate the scores between 2 molecules without moving them.
        
        Parameters
        ----------
        shape : ShapeInput
            Shape
        mol : RDKit.ROMol
            Molecule
        molShapeOptions:
            Options for constructing the shape for molecule
        molConfId : int, optional
            Molecule conformer ID (default is -1)
        
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if shape.useColors is False
    
        C++ signature :
            class boost::python::tuple ScoreMol(struct ShapeInput,class RDKit::ROMol {lvalue},struct ShapeInputOptions [,int=-1])
    """
def ScoreShape(shape1: ShapeInput, shape2: ShapeInput, useColors: bool = False) -> tuple:
    """
        Calculate the scores between 2 shapes without moving them.
        
        Parameters
        ----------
        shape1 : ShapeInput
            Shape
        shape2 : ShapeInput
            Shape
        useColors : bool
            Whether to use colors for the score or not.
        Returns
        -------
         2-tuple of doubles
            The results are (shape_score, color_score)
            The color_score is zero if useColors is False
    
        C++ signature :
            class boost::python::tuple ScoreShape(struct ShapeInput,struct ShapeInput {lvalue} [,bool=False])
    """
def TransformConformer(arg1: list, finalTrans: list, matrix: list, probeShape: ShapeInput, probeConformer: Conformer) -> None:
    """
        Assuming that probeShape has been overlaid onto refShape to give
        the supplied transformation matrix, applies that transformation to the
         given conformer.
        
        Parameters
        ----------
        finalTrans : list[float * 3]
            The final translation to apply to conformer.
        matrix: list[float * 12]
            The transformation matrix
        probeShape : ShapeInput
            Probe shape
        probeConformer : Conformer
            Probe conformer
        
    
        C++ signature :
            void TransformConformer(class boost::python::list,class boost::python::list,class boost::python::list,struct ShapeInput,class RDKit::Conformer {lvalue})
    """

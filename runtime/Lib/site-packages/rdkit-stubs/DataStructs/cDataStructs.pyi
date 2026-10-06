"""
Module containing an assortment of functionality for basic data structures.

At the moment the data structures defined are:
  Bit Vector classes (for storing signatures, fingerprints and the like:
    - ExplicitBitVect: class for relatively small (10s of thousands of bits) or
                       dense bit vectors.
    - SparseBitVect:   class for large, sparse bit vectors
  DiscreteValueVect:   class for storing vectors of integers
  SparseIntVect:       class for storing sparse vectors of integers
"""
from __future__ import annotations
import typing
__all__: list[str] = ['AllBitSimilarity', 'AllProbeBitsMatch', 'AsymmetricSimilarity', 'AsymmetricSimilarityNeighbors', 'AsymmetricSimilarityNeighbors_sparse', 'BitVectToBinaryText', 'BitVectToFPSText', 'BitVectToText', 'BraunBlanquetSimilarity', 'BraunBlanquetSimilarityNeighbors', 'BraunBlanquetSimilarityNeighbors_sparse', 'BulkAllBitSimilarity', 'BulkAsymmetricSimilarity', 'BulkBraunBlanquetSimilarity', 'BulkCosineSimilarity', 'BulkDiceSimilarity', 'BulkKulczynskiSimilarity', 'BulkMcConnaugheySimilarity', 'BulkOnBitSimilarity', 'BulkRogotGoldbergSimilarity', 'BulkRusselSimilarity', 'BulkSokalSimilarity', 'BulkTanimotoSimilarity', 'BulkTverskySimilarity', 'ComputeL1Norm', 'ConvertToExplicit', 'ConvertToNumpyArray', 'CosineSimilarity', 'CosineSimilarityNeighbors', 'CosineSimilarityNeighbors_sparse', 'CreateFromBinaryText', 'CreateFromBitString', 'CreateFromFPSText', 'DiceSimilarity', 'DiceSimilarityNeighbors', 'DiceSimilarityNeighbors_sparse', 'DiscreteValueType', 'DiscreteValueVect', 'EIGHTBITVALUE', 'ExplicitBitVect', 'FOURBITVALUE', 'FPBReader', 'FoldFingerprint', 'InitFromDaylightString', 'IntSparseIntVect', 'KulczynskiSimilarity', 'KulczynskiSimilarityNeighbors', 'KulczynskiSimilarityNeighbors_sparse', 'LongSparseIntVect', 'McConnaugheySimilarity', 'McConnaugheySimilarityNeighbors', 'McConnaugheySimilarityNeighbors_sparse', 'MultiFPBReader', 'NumBitsInCommon', 'ONEBITVALUE', 'OffBitProjSimilarity', 'OffBitsInCommon', 'OnBitProjSimilarity', 'OnBitSimilarity', 'OnBitsInCommon', 'RealValueVect', 'RogotGoldbergSimilarity', 'RogotGoldbergSimilarityNeighbors', 'RogotGoldbergSimilarityNeighbors_sparse', 'RusselSimilarity', 'RusselSimilarityNeighbors', 'RusselSimilarityNeighbors_sparse', 'SIXTEENBITVALUE', 'SokalSimilarity', 'SokalSimilarityNeighbors', 'SokalSimilarityNeighbors_sparse', 'SparseBitVect', 'TWOBITVALUE', 'TanimotoSimilarity', 'TanimotoSimilarityNeighbors', 'TanimotoSimilarityNeighbors_sparse', 'TverskySimilarity', 'UIntSparseIntVect', 'ULongSparseIntVect']
class DiscreteValueType(Boost.Python.enum):
    EIGHTBITVALUE: typing.ClassVar[DiscreteValueType]  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.EIGHTBITVALUE
    FOURBITVALUE: typing.ClassVar[DiscreteValueType]  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.FOURBITVALUE
    ONEBITVALUE: typing.ClassVar[DiscreteValueType]  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.ONEBITVALUE
    SIXTEENBITVALUE: typing.ClassVar[DiscreteValueType]  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.SIXTEENBITVALUE
    TWOBITVALUE: typing.ClassVar[DiscreteValueType]  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'ONEBITVALUE': rdkit.DataStructs.cDataStructs.DiscreteValueType.ONEBITVALUE, 'TWOBITVALUE': rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE, 'FOURBITVALUE': rdkit.DataStructs.cDataStructs.DiscreteValueType.FOURBITVALUE, 'EIGHTBITVALUE': rdkit.DataStructs.cDataStructs.DiscreteValueType.EIGHTBITVALUE, 'SIXTEENBITVALUE': rdkit.DataStructs.cDataStructs.DiscreteValueType.SIXTEENBITVALUE}
    values: typing.ClassVar[dict]  # value = {0: rdkit.DataStructs.cDataStructs.DiscreteValueType.ONEBITVALUE, 1: rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE, 2: rdkit.DataStructs.cDataStructs.DiscreteValueType.FOURBITVALUE, 3: rdkit.DataStructs.cDataStructs.DiscreteValueType.EIGHTBITVALUE, 4: rdkit.DataStructs.cDataStructs.DiscreteValueType.SIXTEENBITVALUE}
class DiscreteValueVect(Boost.Python.instance):
    """
    A container class for storing unsigned integer
    values within a particular range.
    
    The length of the vector and type of its elements (determines the maximum value
    that can be stored) are both set at construction time.
    
    As you would expect, _DiscreteValueVects_ support a set of binary operations
    so you can do things like:
      dvv3 = dvv1 & dvv2  the result contains the smallest value in each entry
      dvv3 = dvv1 | dvv2  the result contains the largest value in each entry
      dvv1 += dvv2     values are truncated when necessary
      dvv3 = dvv1 + dvv2    values are truncated when necessary
      dvv1 -= dvv3    would-be negative values are set to zero
      dvv3 = dvv1 - dvv2    would-be negative values are set to zero
    
    Elements can be set and read using indexing (i.e. bv[i] = 4 or val=bv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 64
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetTotalVal(self) -> int:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                unsigned int GetTotalVal(class RDKit::DiscreteValueVect {lvalue})
        """
    def GetValueType(self) -> DiscreteValueType:
        """
            Get the type of value stored in the vector
        
            C++ signature :
                enum RDKit::DiscreteValueVect::DiscreteValueType GetValueType(class RDKit::DiscreteValueVect {lvalue})
        """
    def __add__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::DiscreteValueVect {lvalue},class RDKit::DiscreteValueVect)
        """
    def __and__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::DiscreteValueVect {lvalue},class RDKit::DiscreteValueVect)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::DiscreteValueVect)
        """
    def __getitem__(self, i: int) -> int:
        """
            Get the value at a specified location
        
            C++ signature :
                unsigned int __getitem__(class RDKit::DiscreteValueVect {lvalue},unsigned int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::DiscreteValueVect & __ptr64>,class RDKit::DiscreteValueVect)
        """
    @typing.overload
    def __init__(self, valType: DiscreteValueType, length: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,enum RDKit::DiscreteValueVect::DiscreteValueType,unsigned int)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def __isub__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::DiscreteValueVect & __ptr64>,class RDKit::DiscreteValueVect)
        """
    def __len__(self) -> int:
        """
            Get the number of entries in the vector
        
            C++ signature :
                unsigned int __len__(class RDKit::DiscreteValueVect {lvalue})
        """
    def __or__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::DiscreteValueVect {lvalue},class RDKit::DiscreteValueVect)
        """
    def __setitem__(self, i: int, val: int) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::DiscreteValueVect {lvalue},unsigned int,unsigned int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: DiscreteValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::DiscreteValueVect {lvalue},class RDKit::DiscreteValueVect)
        """
class ExplicitBitVect(Boost.Python.instance):
    """
    A class to store explicit bit vectors.
    
    This class is most useful for situations where the size of the vector
    is relatively small (tens of thousands or smaller).
    
    For larger vectors, use the _SparseBitVect_ class instead.
    
    As you would expect, _ExplicitBitVects_ support a set of binary operations
    so you can do things like:
      bv3 = bv1 & bv2  (bitwise and)
      bv3 = bv1 | bv2  (bitwise or)
      bv3 = bv1 ^ bv2  (bitwise xor)
      bv3 = ~bv1       (bitwise negation)
    
    Bits can be set and read using either the Set/UnsetBit() and GetBit() methods
    or by indexing (i.e. bv[i] = 1 or if bv[i]).
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def ToBitString(*args, **kwargs):
        """
        
        BitVectToText( (SparseBitVect)bv1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class SparseBitVect)
        
        BitVectToText( (ExplicitBitVect)bv1) -> str :
            Returns a string of zeros and ones representing the bit vector.
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class ExplicitBitVect)
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def FromBase64(self, inD: str) -> None:
        """
            Initializes the vector from a base64 encoded binary string.
            
        
            C++ signature :
                void FromBase64(class ExplicitBitVect {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def GetBit(self, which: int) -> bool:
        """
            Returns the value of a bit.
            
        
            C++ signature :
                bool GetBit(class ExplicitBitVect {lvalue},unsigned int)
        """
    def GetNumBits(self) -> int:
        """
            Returns the number of bits in the vector (the vector's size).
            
        
            C++ signature :
                unsigned int GetNumBits(class ExplicitBitVect {lvalue})
        """
    def GetNumOffBits(self) -> int:
        """
            Returns the number of off bits.
            
        
            C++ signature :
                unsigned int GetNumOffBits(class ExplicitBitVect {lvalue})
        """
    def GetNumOnBits(self) -> int:
        """
            Returns the number of on bits.
            
        
            C++ signature :
                unsigned int GetNumOnBits(class ExplicitBitVect {lvalue})
        """
    def GetOnBits(self) -> _vectint:
        """
            Returns a tuple containing IDs of the on bits.
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetOnBits(class ExplicitBitVect)
        """
    def SetBit(self, which: int) -> bool:
        """
            Turns on a particular bit.  Returns the original state of the bit.
            
        
            C++ signature :
                bool SetBit(class ExplicitBitVect {lvalue},unsigned int)
        """
    def SetBitsFromList(self, onBitList: typing.Any) -> None:
        """
            Turns on a set of bits.  The argument should be a tuple or list of bit ids.
            
        
            C++ signature :
                void SetBitsFromList(class ExplicitBitVect * __ptr64,class boost::python::api::object)
        """
    def ToBase64(self) -> str:
        """
            Converts the vector to a base64 string (the base64 encoded version of the results of ToString()).
            
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > ToBase64(class ExplicitBitVect {lvalue})
        """
    def ToBinary(self) -> typing.Any:
        """
            Returns an internal binary representation of the vector.
            
        
            C++ signature :
                class boost::python::api::object ToBinary(class ExplicitBitVect)
        """
    def ToList(self) -> list:
        """
            Return the Bitvector as a python list (faster than list(vect))
        
            C++ signature :
                class boost::python::list ToList(class ExplicitBitVect)
        """
    def UnSetBit(self, which: int) -> bool:
        """
            Turns off a particular bit.  Returns the original state of the bit.
            
        
            C++ signature :
                bool UnSetBit(class ExplicitBitVect {lvalue},unsigned int)
        """
    def UnSetBitsFromList(self, offBitList: typing.Any) -> None:
        """
            Turns off a set of bits.  The argument should be a tuple or list of bit ids.
            
        
            C++ signature :
                void UnSetBitsFromList(class ExplicitBitVect * __ptr64,class boost::python::api::object)
        """
    def __add__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
    def __and__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
    def __eq__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class ExplicitBitVect)
        """
    def __getitem__(self, which: int) -> int:
        """
            C++ signature :
                int __getitem__(class ExplicitBitVect,int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class ExplicitBitVect & __ptr64>,class ExplicitBitVect)
        """
    @typing.overload
    def __init__(self, size: int) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __init__(self, size: int, bitsSet: bool) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int,bool)
        """
    def __invert__(self) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __invert__(class ExplicitBitVect {lvalue})
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class ExplicitBitVect {lvalue})
        """
    def __ne__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
    def __or__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
    def __setitem__(self, which: int, val: int) -> int:
        """
            C++ signature :
                int __setitem__(class ExplicitBitVect {lvalue},int,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __xor__(self, other: ExplicitBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __xor__(class ExplicitBitVect {lvalue},class ExplicitBitVect)
        """
class FPBReader(Boost.Python.instance):
    """
    A class for reading and searching FPB files from Andrew Dalke's chemfp.
        Note that this functionality is still experimental and the API may
        change in future releases.
    """
    __instance_size__: typing.ClassVar[int] = 48
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetBytes(self, which: int) -> typing.Any:
        """
            returns a particular fingerprint as bytes
        
            C++ signature :
                class boost::python::api::object GetBytes(class RDKit::FPBReader const * __ptr64,unsigned int)
        """
    def GetContainingNeighbors(self, bv: str) -> tuple:
        """
            returns indices of neighbors that contain this fingerprint (where all bits from this fingerprint are also set)
        
            C++ signature :
                class boost::python::tuple GetContainingNeighbors(class RDKit::FPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def GetFP(self, idx: int) -> ExplicitBitVect:
        """
            returns a particular fingerprint as an ExplicitBitVect
        
            C++ signature :
                class boost::shared_ptr<class ExplicitBitVect> GetFP(class RDKit::FPBReader {lvalue},unsigned int)
        """
    def GetId(self, idx: int) -> str:
        """
            returns the id of a particular fingerprint
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > GetId(class RDKit::FPBReader {lvalue},unsigned int)
        """
    def GetNumBits(self) -> int:
        """
            returns the number of bits in a fingerprint
        
            C++ signature :
                unsigned int GetNumBits(class RDKit::FPBReader {lvalue})
        """
    def GetTanimoto(self, which: int, bytes: str) -> float:
        """
            return the tanimoto similarity of a particular fingerprint to the bytes provided
        
            C++ signature :
                double GetTanimoto(class RDKit::FPBReader const * __ptr64,unsigned int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def GetTanimotoNeighbors(self, bv: str, threshold: float = 0.7) -> tuple:
        """
            returns tanimoto similarities to and indices of all neighbors above the specified threshold
        
            C++ signature :
                class boost::python::tuple GetTanimotoNeighbors(class RDKit::FPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,double=0.7])
        """
    def GetTversky(self, which: int, bytes: str, ca: float, cb: float) -> float:
        """
            return the Tverksy similarity of a particular fingerprint to the bytes provided
        
            C++ signature :
                double GetTversky(class RDKit::FPBReader const * __ptr64,unsigned int,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double)
        """
    def GetTverskyNeighbors(self, bv: str, ca: float, cb: float, threshold: float = 0.7) -> tuple:
        """
            returns Tversky similarities to and indices of all neighbors above the specified threshold
        
            C++ signature :
                class boost::python::tuple GetTverskyNeighbors(class RDKit::FPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double [,double=0.7])
        """
    def Init(self) -> None:
        """
            Read the fingerprints from the file. This can take a while.
            
        
            C++ signature :
                void Init(class RDKit::FPBReader {lvalue})
        """
    def __getitem__(self, which: int) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getitem__(class RDKit::FPBReader const * __ptr64,unsigned int)
        """
    def __init__(self, filename: str, lazy: bool = False) -> None:
        """
            docstring
        
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=False])
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class RDKit::FPBReader {lvalue})
        """
class IntSparseIntVect(Boost.Python.instance):
    """
    A container class for storing integer
    values within a particular range.
    
    The length of the vector is set at construction time.
    
    As you would expect, _SparseIntVects_ support a set of binary operations
    so you can do things like:
      Arithmetic:
      siv1 += siv2
      siv3 = siv1 + siv2
      siv1 -= siv3
      siv3 = siv1 - siv2
      "Fuzzy" binary operations:
      siv3 = siv1 & siv2  the result contains the smallest value in each entry
      siv3 = siv1 | siv2  the result contains the largest value in each entry
    
    Elements can be set and read using indexing (i.e. siv[i] = 4 or val=siv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetLength(self) -> int:
        """
            Returns the length of the vector
        
            C++ signature :
                int GetLength(class RDKit::SparseIntVect<int> {lvalue})
        """
    def GetNonzeroElements(self) -> dict:
        """
            returns a dictionary of the nonzero elements
        
            C++ signature :
                class boost::python::dict GetNonzeroElements(class RDKit::SparseIntVect<int> {lvalue})
        """
    def GetTotalVal(self, useAbs: bool = False) -> int:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                int GetTotalVal(class RDKit::SparseIntVect<int> {lvalue} [,bool=False])
        """
    def ToBinary(self) -> typing.Any:
        """
            returns a binary (pickle) representation of the vector
        
            C++ signature :
                class boost::python::api::object ToBinary(class RDKit::SparseIntVect<int>)
        """
    def ToList(self) -> list:
        """
            Return the SparseIntVect as a python list
        
            C++ signature :
                class boost::python::list ToList(class RDKit::SparseIntVect<int> {lvalue})
        """
    def UpdateFromSequence(self, seq: typing.Any) -> None:
        """
            update the vector based on the values in the list or tuple
        
            C++ signature :
                void UpdateFromSequence(class RDKit::SparseIntVect<int> {lvalue},class boost::python::api::object {lvalue})
        """
    def __add__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
    def __and__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
    def __eq__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::SparseIntVect<int>)
        """
    def __getitem__(self, item: int) -> int:
        """
            Get the value at a specified location
        
            C++ signature :
                int __getitem__(class RDKit::SparseIntVect<int> {lvalue},int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __iadd__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,class RDKit::SparseIntVect<int>)
        """
    @typing.overload
    def __iadd__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,int)
        """
    def __idiv__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __idiv__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,int)
        """
    def __imul__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __imul__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,int)
        """
    @typing.overload
    def __init__(self, arg1: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,int)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __isub__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,class RDKit::SparseIntVect<int>)
        """
    @typing.overload
    def __isub__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<int> & __ptr64>,int)
        """
    def __ne__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
    def __or__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
    def __setitem__(self, item: int, value: int) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::SparseIntVect<int> {lvalue},int,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: IntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::SparseIntVect<int> {lvalue},class RDKit::SparseIntVect<int>)
        """
class LongSparseIntVect(Boost.Python.instance):
    """
    A container class for storing integer
    values within a particular range.
    
    The length of the vector is set at construction time.
    
    As you would expect, _SparseIntVects_ support a set of binary operations
    so you can do things like:
      Arithmetic:
      siv1 += siv2
      siv3 = siv1 + siv2
      siv1 -= siv3
      siv3 = siv1 - siv2
      "Fuzzy" binary operations:
      siv3 = siv1 & siv2  the result contains the smallest value in each entry
      siv3 = siv1 | siv2  the result contains the largest value in each entry
    
    Elements can be set and read using indexing (i.e. siv[i] = 4 or val=siv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetLength(self) -> int:
        """
            Returns the length of the vector
        
            C++ signature :
                __int64 GetLength(class RDKit::SparseIntVect<__int64> {lvalue})
        """
    def GetNonzeroElements(self) -> dict:
        """
            returns a dictionary of the nonzero elements
        
            C++ signature :
                class boost::python::dict GetNonzeroElements(class RDKit::SparseIntVect<__int64> {lvalue})
        """
    def GetTotalVal(self, useAbs: bool = False) -> int:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                int GetTotalVal(class RDKit::SparseIntVect<__int64> {lvalue} [,bool=False])
        """
    def ToBinary(self) -> typing.Any:
        """
            returns a binary (pickle) representation of the vector
        
            C++ signature :
                class boost::python::api::object ToBinary(class RDKit::SparseIntVect<__int64>)
        """
    def ToList(self) -> list:
        """
            Return the SparseIntVect as a python list
        
            C++ signature :
                class boost::python::list ToList(class RDKit::SparseIntVect<__int64> {lvalue})
        """
    def UpdateFromSequence(self, seq: typing.Any) -> None:
        """
            update the vector based on the values in the list or tuple
        
            C++ signature :
                void UpdateFromSequence(class RDKit::SparseIntVect<__int64> {lvalue},class boost::python::api::object {lvalue})
        """
    def __add__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
    def __and__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
    def __eq__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::SparseIntVect<__int64>)
        """
    def __getitem__(self, item: int) -> int:
        """
            Get the value at a specified location
        
            C++ signature :
                int __getitem__(class RDKit::SparseIntVect<__int64> {lvalue},__int64)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __iadd__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,class RDKit::SparseIntVect<__int64>)
        """
    @typing.overload
    def __iadd__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,int)
        """
    def __idiv__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __idiv__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,int)
        """
    def __imul__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __imul__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,int)
        """
    @typing.overload
    def __init__(self, arg1: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,__int64)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __isub__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,class RDKit::SparseIntVect<__int64>)
        """
    @typing.overload
    def __isub__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<__int64> & __ptr64>,int)
        """
    def __ne__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
    def __or__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
    def __setitem__(self, item: int, value: int) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::SparseIntVect<__int64> {lvalue},__int64,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: LongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::SparseIntVect<__int64> {lvalue},class RDKit::SparseIntVect<__int64>)
        """
class MultiFPBReader(Boost.Python.instance):
    """
    A class for reading and searching multiple FPB files from Andrew Dalke's chemfp.
        Note that this functionality is still experimental and the API may
        change in future releases.
    """
    __instance_size__: typing.ClassVar[int] = 56
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AddReader(self, rdr: FPBReader) -> int:
        """
            adds an FPBReader to our set of readers
        
            C++ signature :
                unsigned int AddReader(class RDKit::MultiFPBReader {lvalue},class RDKit::FPBReader * __ptr64)
        """
    def GetContainingNeighbors(self, bv: str, numThreads: int = 1) -> tuple:
        """
            returns indices of neighbors that contain this fingerprint (where all bits from this fingerprint are also set)
        
            C++ signature :
                class boost::python::tuple GetContainingNeighbors(class RDKit::MultiFPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,unsigned int=1])
        """
    def GetNumBits(self) -> int:
        """
            returns the number of bits in a fingerprint
        
            C++ signature :
                unsigned int GetNumBits(class RDKit::MultiFPBReader {lvalue})
        """
    def GetReader(self, which: int) -> FPBReader:
        """
            returns one of our readers
        
            C++ signature :
                class RDKit::FPBReader * __ptr64 GetReader(class RDKit::MultiFPBReader {lvalue},unsigned int)
        """
    def GetTanimotoNeighbors(self, bv: str, threshold: float = 0.7, numThreads: int = 1) -> tuple:
        """
            returns tanimoto similarities to and indices of all neighbors above the specified threshold
        
            C++ signature :
                class boost::python::tuple GetTanimotoNeighbors(class RDKit::MultiFPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,double=0.7 [,unsigned int=1]])
        """
    def GetTverskyNeighbors(self, bv: str, ca: float, cb: float, threshold: float = 0.7, numThreads: int = 1) -> tuple:
        """
            returns Tversky similarities to and indices of all neighbors above the specified threshold
        
            C++ signature :
                class boost::python::tuple GetTverskyNeighbors(class RDKit::MultiFPBReader const * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double [,double=0.7 [,unsigned int=1]])
        """
    def Init(self) -> None:
        """
            Call Init() on each of our children. This can take a while.
            
        
            C++ signature :
                void Init(class RDKit::MultiFPBReader {lvalue})
        """
    def __init__(self, initOnSearch: bool = False) -> None:
        """
            docstring
        
            C++ signature :
                void __init__(struct _object * __ptr64 [,bool=False])
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class RDKit::MultiFPBReader {lvalue})
        """
class RealValueVect(Boost.Python.instance):
    """
    A container class for storing real
    values.
    
    The length of the vector is set at construction time.
    
    As you would expect, _RealValueVects_ support a set of binary operations
    so you can do things like:
      rvv3 = rvv1 & rvv2  the result contains the smallest value in each entry
      rvv3 = rvv1 | rvv2  the result contains the largest value in each entry
      rvv1 += rvv2     
      rvv3 = rvv1 + rvv2    
      rvv1 -= rvv3    
      rvv3 = rvv1 - rvv2    
    
    Elements can be set and read using indexing (i.e. bv[i] = 4 or val=bv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 56
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def GetTotalVal(arg1: RealValueVect) -> float:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                double GetTotalVal(class RDKit::RealValueVect {lvalue})
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def __add__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::RealValueVect {lvalue},class RDKit::RealValueVect)
        """
    def __and__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::RealValueVect {lvalue},class RDKit::RealValueVect)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::RealValueVect)
        """
    def __getitem__(self, item: int) -> float:
        """
            Get the value at a specified location
        
            C++ signature :
                double __getitem__(class RDKit::RealValueVect {lvalue},unsigned int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    def __iadd__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::RealValueVect & __ptr64>,class RDKit::RealValueVect)
        """
    @typing.overload
    def __init__(self, arg1: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int)
        """
    @typing.overload
    def __init__(self, arg1: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def __isub__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::RealValueVect & __ptr64>,class RDKit::RealValueVect)
        """
    def __len__(self) -> int:
        """
            Get the number of entries in the vector
        
            C++ signature :
                unsigned int __len__(class RDKit::RealValueVect {lvalue})
        """
    def __or__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::RealValueVect {lvalue},class RDKit::RealValueVect)
        """
    def __setitem__(self, item: int, value: float) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::RealValueVect {lvalue},unsigned int,double)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: RealValueVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::RealValueVect {lvalue},class RDKit::RealValueVect)
        """
class SparseBitVect(Boost.Python.instance):
    """
    A class to store sparse bit vectors.
    
    This class is most useful for situations where the size of the vector
    is large and relatively few bits are set
    
    For smaller or denser vectors, the _ExplicitBitVect_ class is much faster.
    
    As you would expect, _SparseBitVects_ support a set of binary operations
    so you can do things like:
      bv3 = bv1 & bv2  (bitwise and)
      bv3 = bv1 | bv2  (bitwise or)
      bv3 = bv1 ^ bv2  (bitwise xor)
      bv3 = ~bv1       (bitwise negation) NOTE: this operation is likely
                        to be VERY slow and inefficient.
    
    Bits can be set and read using either the Set/UnsetBit() and GetBit() methods
    or by indexing (i.e. bv[i] = 1 or if bv[i]).
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def ToBitString(*args, **kwargs):
        """
        
        BitVectToText( (SparseBitVect)bv1) -> str :
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class SparseBitVect)
        
        BitVectToText( (ExplicitBitVect)bv1) -> str :
            Returns a string of zeros and ones representing the bit vector.
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class ExplicitBitVect)
        """
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def FromBase64(self, inD: str) -> None:
        """
            Initializes the vector from a base64 encoded binary string.
            
        
            C++ signature :
                void FromBase64(class SparseBitVect {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def GetBit(self, which: int) -> bool:
        """
            Returns the value of a bit.
            
        
            C++ signature :
                bool GetBit(class SparseBitVect {lvalue},unsigned int)
        """
    def GetNumBits(self) -> int:
        """
            Returns the number of bits in the vector (the vector's size).
            
        
            C++ signature :
                unsigned int GetNumBits(class SparseBitVect {lvalue})
        """
    def GetNumOffBits(self) -> int:
        """
            Returns the number of off bits.
            
        
            C++ signature :
                unsigned int GetNumOffBits(class SparseBitVect {lvalue})
        """
    def GetNumOnBits(self) -> int:
        """
            Returns the number of on bits.
            
        
            C++ signature :
                unsigned int GetNumOnBits(class SparseBitVect {lvalue})
        """
    def GetOnBits(self) -> _vectint:
        """
            Returns a tuple containing IDs of the on bits.
            
        
            C++ signature :
                class std::vector<int,class std::allocator<int> > GetOnBits(class SparseBitVect)
        """
    def SetBit(self, which: int) -> bool:
        """
            Turns on a particular bit.  Returns the original state of the bit.
            
        
            C++ signature :
                bool SetBit(class SparseBitVect {lvalue},unsigned int)
        """
    def SetBitsFromList(self, onBitList: typing.Any) -> None:
        """
            Turns on a set of bits.  The argument should be a tuple or list of bit ids.
            
        
            C++ signature :
                void SetBitsFromList(class SparseBitVect * __ptr64,class boost::python::api::object)
        """
    def ToBase64(self) -> str:
        """
            Converts the vector to a base64 string (the base64 encoded version of the results of ToString()).
            
        
            C++ signature :
                class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > ToBase64(class SparseBitVect {lvalue})
        """
    def ToBinary(self) -> typing.Any:
        """
            Returns an internal binary representation of the vector.
            
        
            C++ signature :
                class boost::python::api::object ToBinary(class SparseBitVect)
        """
    def ToList(self) -> list:
        """
            Return the BitVector as a python list
        
            C++ signature :
                class boost::python::list ToList(class SparseBitVect)
        """
    def UnSetBit(self, which: int) -> bool:
        """
            Turns off a particular bit.  Returns the original state of the bit.
            
        
            C++ signature :
                bool UnSetBit(class SparseBitVect {lvalue},unsigned int)
        """
    def UnSetBitsFromList(self, offBitList: typing.Any) -> None:
        """
            Turns off a set of bits.  The argument should be a tuple or list of bit ids.
            
        
            C++ signature :
                void UnSetBitsFromList(class SparseBitVect * __ptr64,class boost::python::api::object)
        """
    def __and__(self, other: SparseBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class SparseBitVect {lvalue},class SparseBitVect)
        """
    def __eq__(self, other: SparseBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class SparseBitVect {lvalue},class SparseBitVect)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class SparseBitVect)
        """
    def __getitem__(self, which: int) -> int:
        """
            C++ signature :
                int __getitem__(class SparseBitVect,int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __init__(self, size: int) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    def __invert__(self) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __invert__(class SparseBitVect {lvalue})
        """
    def __len__(self) -> int:
        """
            C++ signature :
                unsigned int __len__(class SparseBitVect {lvalue})
        """
    def __ne__(self, other: SparseBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class SparseBitVect {lvalue},class SparseBitVect)
        """
    def __or__(self, other: SparseBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class SparseBitVect {lvalue},class SparseBitVect)
        """
    def __setitem__(self, which: int, val: int) -> int:
        """
            C++ signature :
                int __setitem__(class SparseBitVect {lvalue},int,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __xor__(self, other: SparseBitVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __xor__(class SparseBitVect {lvalue},class SparseBitVect)
        """
class UIntSparseIntVect(Boost.Python.instance):
    """
    A container class for storing integer
    values within a particular range.
    
    The length of the vector is set at construction time.
    
    As you would expect, _SparseIntVects_ support a set of binary operations
    so you can do things like:
      Arithmetic:
      siv1 += siv2
      siv3 = siv1 + siv2
      siv1 -= siv3
      siv3 = siv1 - siv2
      "Fuzzy" binary operations:
      siv3 = siv1 & siv2  the result contains the smallest value in each entry
      siv3 = siv1 | siv2  the result contains the largest value in each entry
    
    Elements can be set and read using indexing (i.e. siv[i] = 4 or val=siv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetLength(self) -> int:
        """
            Returns the length of the vector
        
            C++ signature :
                unsigned int GetLength(class RDKit::SparseIntVect<unsigned int> {lvalue})
        """
    def GetNonzeroElements(self) -> dict:
        """
            returns a dictionary of the nonzero elements
        
            C++ signature :
                class boost::python::dict GetNonzeroElements(class RDKit::SparseIntVect<unsigned int> {lvalue})
        """
    def GetTotalVal(self, useAbs: bool = False) -> int:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                int GetTotalVal(class RDKit::SparseIntVect<unsigned int> {lvalue} [,bool=False])
        """
    def ToBinary(self) -> typing.Any:
        """
            returns a binary (pickle) representation of the vector
        
            C++ signature :
                class boost::python::api::object ToBinary(class RDKit::SparseIntVect<unsigned int>)
        """
    def ToList(self) -> list:
        """
            Return the SparseIntVect as a python list
        
            C++ signature :
                class boost::python::list ToList(class RDKit::SparseIntVect<unsigned int> {lvalue})
        """
    def UpdateFromSequence(self, seq: typing.Any) -> None:
        """
            update the vector based on the values in the list or tuple
        
            C++ signature :
                void UpdateFromSequence(class RDKit::SparseIntVect<unsigned int> {lvalue},class boost::python::api::object {lvalue})
        """
    def __add__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
    def __and__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
    def __eq__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::SparseIntVect<unsigned int>)
        """
    def __getitem__(self, item: int) -> int:
        """
            Get the value at a specified location
        
            C++ signature :
                int __getitem__(class RDKit::SparseIntVect<unsigned int> {lvalue},unsigned int)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __iadd__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,class RDKit::SparseIntVect<unsigned int>)
        """
    @typing.overload
    def __iadd__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,int)
        """
    def __idiv__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __idiv__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,int)
        """
    def __imul__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __imul__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,int)
        """
    @typing.overload
    def __init__(self, arg1: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned int)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __isub__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,class RDKit::SparseIntVect<unsigned int>)
        """
    @typing.overload
    def __isub__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned int> & __ptr64>,int)
        """
    def __ne__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
    def __or__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
    def __setitem__(self, item: int, value: int) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::SparseIntVect<unsigned int> {lvalue},unsigned int,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: UIntSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::SparseIntVect<unsigned int> {lvalue},class RDKit::SparseIntVect<unsigned int>)
        """
class ULongSparseIntVect(Boost.Python.instance):
    """
    A container class for storing integer
    values within a particular range.
    
    The length of the vector is set at construction time.
    
    As you would expect, _SparseIntVects_ support a set of binary operations
    so you can do things like:
      Arithmetic:
      siv1 += siv2
      siv3 = siv1 + siv2
      siv1 -= siv3
      siv3 = siv1 - siv2
      "Fuzzy" binary operations:
      siv3 = siv1 & siv2  the result contains the smallest value in each entry
      siv3 = siv1 | siv2  the result contains the largest value in each entry
    
    Elements can be set and read using indexing (i.e. siv[i] = 4 or val=siv[i])
    
    """
    __getstate_manages_dict__: typing.ClassVar[bool] = True
    __instance_size__: typing.ClassVar[int] = 40
    __safe_for_unpickling__: typing.ClassVar[bool] = True
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def GetLength(self) -> int:
        """
            Returns the length of the vector
        
            C++ signature :
                unsigned __int64 GetLength(class RDKit::SparseIntVect<unsigned __int64> {lvalue})
        """
    def GetNonzeroElements(self) -> dict:
        """
            returns a dictionary of the nonzero elements
        
            C++ signature :
                class boost::python::dict GetNonzeroElements(class RDKit::SparseIntVect<unsigned __int64> {lvalue})
        """
    def GetTotalVal(self, useAbs: bool = False) -> int:
        """
            Get the sum of the values in the vector, basically L1 norm
        
            C++ signature :
                int GetTotalVal(class RDKit::SparseIntVect<unsigned __int64> {lvalue} [,bool=False])
        """
    def ToBinary(self) -> typing.Any:
        """
            returns a binary (pickle) representation of the vector
        
            C++ signature :
                class boost::python::api::object ToBinary(class RDKit::SparseIntVect<unsigned __int64>)
        """
    def ToList(self) -> list:
        """
            Return the SparseIntVect as a python list
        
            C++ signature :
                class boost::python::list ToList(class RDKit::SparseIntVect<unsigned __int64> {lvalue})
        """
    def UpdateFromSequence(self, seq: typing.Any) -> None:
        """
            update the vector based on the values in the list or tuple
        
            C++ signature :
                void UpdateFromSequence(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class boost::python::api::object {lvalue})
        """
    def __add__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __add__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __and__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __and__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __eq__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __eq__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __getinitargs__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getinitargs__(class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __getitem__(self, item: int) -> int:
        """
            Get the value at a specified location
        
            C++ signature :
                int __getitem__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},unsigned __int64)
        """
    def __getstate__(self) -> tuple:
        """
            C++ signature :
                class boost::python::tuple __getstate__(class boost::python::api::object)
        """
    @typing.overload
    def __iadd__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,class RDKit::SparseIntVect<unsigned __int64>)
        """
    @typing.overload
    def __iadd__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __iadd__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,int)
        """
    def __idiv__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __idiv__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,int)
        """
    def __imul__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __imul__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,int)
        """
    @typing.overload
    def __init__(self, arg1: int) -> None:
        """
            Constructor
        
            C++ signature :
                void __init__(struct _object * __ptr64,unsigned __int64)
        """
    @typing.overload
    def __init__(self, pkl: str) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __isub__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,class RDKit::SparseIntVect<unsigned __int64>)
        """
    @typing.overload
    def __isub__(self, other: int) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __isub__(struct boost::python::back_reference<class RDKit::SparseIntVect<unsigned __int64> & __ptr64>,int)
        """
    def __ne__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __ne__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __or__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __or__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
    def __setitem__(self, item: int, value: int) -> None:
        """
            Set the value at a specified location
        
            C++ signature :
                void __setitem__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},unsigned __int64,int)
        """
    def __setstate__(self, data: tuple) -> None:
        """
            C++ signature :
                void __setstate__(class boost::python::api::object,class boost::python::tuple)
        """
    def __sub__(self, other: ULongSparseIntVect) -> typing.Any:
        """
            C++ signature :
                struct _object * __ptr64 __sub__(class RDKit::SparseIntVect<unsigned __int64> {lvalue},class RDKit::SparseIntVect<unsigned __int64>)
        """
@typing.overload
def AllBitSimilarity(v1: SparseBitVect, v2: SparseBitVect) -> float:
    """
        C++ signature :
            double AllBitSimilarity(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def AllBitSimilarity(v1: ExplicitBitVect, v2: ExplicitBitVect) -> float:
    """
        (B(bv1) - B(bv1^bv2)) / B(bv1)
    
        C++ signature :
            double AllBitSimilarity(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def AllProbeBitsMatch(probe: SparseBitVect, ref: SparseBitVect) -> bool:
    """
        C++ signature :
            bool AllProbeBitsMatch(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def AllProbeBitsMatch(probe: ExplicitBitVect, ref: ExplicitBitVect) -> bool:
    """
        C++ signature :
            bool AllProbeBitsMatch(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def AllProbeBitsMatch(probe: SparseBitVect, ref: str) -> bool:
    """
        C++ signature :
            bool AllProbeBitsMatch(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
@typing.overload
def AllProbeBitsMatch(probe: ExplicitBitVect, ref: str) -> bool:
    """
        Returns True if all bits in the first argument match all bits in the 
          vector defined by the pickle in the second argument.
        
    
        C++ signature :
            bool AllProbeBitsMatch(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
@typing.overload
def AsymmetricSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double AsymmetricSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def AsymmetricSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / min(B(bv1),B(bv2))
    
        C++ signature :
            double AsymmetricSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def AsymmetricSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double AsymmetricSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def AsymmetricSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / min(B(bv1),B(bv2))
    
        C++ signature :
            double AsymmetricSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def AsymmetricSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / min(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list AsymmetricSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def AsymmetricSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / min(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list AsymmetricSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def BitVectToBinaryText(bv: SparseBitVect) -> typing.Any:
    """
        C++ signature :
            class boost::python::api::object BitVectToBinaryText(class SparseBitVect)
    """
@typing.overload
def BitVectToBinaryText(bv: ExplicitBitVect) -> typing.Any:
    """
        Returns a binary string (byte array) representing the bit vector.
    
        C++ signature :
            class boost::python::api::object BitVectToBinaryText(class ExplicitBitVect)
    """
@typing.overload
def BitVectToFPSText(bv1: SparseBitVect) -> str:
    """
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToFPSText(class SparseBitVect)
    """
@typing.overload
def BitVectToFPSText(bv1: ExplicitBitVect) -> str:
    """
        Returns an FPS string representing the bit vector.
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToFPSText(class ExplicitBitVect)
    """
@typing.overload
def BitVectToText(bv1: SparseBitVect) -> str:
    """
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class SparseBitVect)
    """
@typing.overload
def BitVectToText(bv1: ExplicitBitVect) -> str:
    """
        Returns a string of zeros and ones representing the bit vector.
    
        C++ signature :
            class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > BitVectToText(class ExplicitBitVect)
    """
@typing.overload
def BraunBlanquetSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double BraunBlanquetSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def BraunBlanquetSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / max(B(bv1),B(bv2))
    
        C++ signature :
            double BraunBlanquetSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def BraunBlanquetSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double BraunBlanquetSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def BraunBlanquetSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / max(B(bv1),B(bv2))
    
        C++ signature :
            double BraunBlanquetSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def BraunBlanquetSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / max(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list BraunBlanquetSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def BraunBlanquetSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / max(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list BraunBlanquetSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def BulkAllBitSimilarity(v1: ExplicitBitVect, v2: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkAllBitSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkAllBitSimilarity(v1: ExplicitBitVect, v2: typing.Any, returnDistance: bool = 0) -> list:
    """
        (B(bv1) - B(bv1^bv2)) / B(bv1)
    
        C++ signature :
            class boost::python::list BulkAllBitSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkAsymmetricSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkAsymmetricSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkAsymmetricSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / min(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list BulkAsymmetricSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkBraunBlanquetSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkBraunBlanquetSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkBraunBlanquetSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / max(B(bv1),B(bv2))
    
        C++ signature :
            class boost::python::list BulkBraunBlanquetSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkCosineSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkCosineSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkCosineSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / sqrt(B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list BulkCosineSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkDiceSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkDiceSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        2*B(bv1&bv2) / (B(bv1) + B(bv2))
    
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkDiceSimilarity(v1: IntSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Dice similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class RDKit::SparseIntVect<int>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkDiceSimilarity(v1: LongSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Dice similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class RDKit::SparseIntVect<__int64>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkDiceSimilarity(v1: UIntSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Dice similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class RDKit::SparseIntVect<unsigned int>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkDiceSimilarity(v1: ULongSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Dice similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkDiceSimilarity(class RDKit::SparseIntVect<unsigned __int64>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkKulczynskiSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkKulczynskiSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkKulczynskiSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2)*(B(bv1) + B(bv2)) / (2 * B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list BulkKulczynskiSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkMcConnaugheySimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkMcConnaugheySimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkMcConnaugheySimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        (B(bv1&bv2) * (B(bv1)+B(bv2)) - B(bv1)*B(bv2)) / (B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list BulkMcConnaugheySimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkOnBitSimilarity(v1: ExplicitBitVect, v2: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkOnBitSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkOnBitSimilarity(v1: ExplicitBitVect, v2: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / B(bv1|bv2)
    
        C++ signature :
            class boost::python::list BulkOnBitSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkRogotGoldbergSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkRogotGoldbergSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkRogotGoldbergSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list BulkRogotGoldbergSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkRusselSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkRusselSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkRusselSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list BulkRusselSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkSokalSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkSokalSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkSokalSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / (2*B(bv1) + 2*B(bv2) - 3*B(bv1&bv2))
    
        C++ signature :
            class boost::python::list BulkSokalSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkTanimotoSimilarity(bv1: SparseBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkTanimotoSimilarity(bv1: ExplicitBitVect, bvList: typing.Any, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / (B(bv1) + B(bv2) - B(bv1&bv2))
    
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object [,bool=0])
    """
@typing.overload
def BulkTanimotoSimilarity(v1: IntSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Tanimoto similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class RDKit::SparseIntVect<int>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkTanimotoSimilarity(v1: LongSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Tanimoto similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class RDKit::SparseIntVect<__int64>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkTanimotoSimilarity(v1: UIntSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Tanimoto similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class RDKit::SparseIntVect<unsigned int>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkTanimotoSimilarity(v1: ULongSparseIntVect, v2: list, returnDistance: bool = False) -> list:
    """
        return the Tanimoto similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTanimotoSimilarity(class RDKit::SparseIntVect<unsigned __int64>,class boost::python::list [,bool=False])
    """
@typing.overload
def BulkTverskySimilarity(bv1: SparseBitVect, bvList: typing.Any, a: float, b: float, returnDistance: bool = 0) -> list:
    """
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class SparseBitVect const * __ptr64,class boost::python::api::object,double,double [,bool=0])
    """
@typing.overload
def BulkTverskySimilarity(bv1: ExplicitBitVect, bvList: typing.Any, a: float, b: float, returnDistance: bool = 0) -> list:
    """
        B(bv1&bv2) / (a*B(bv1)+b*B(bv2)+(1-a-b)*B(bv1&bv2)
    
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class ExplicitBitVect const * __ptr64,class boost::python::api::object,double,double [,bool=0])
    """
@typing.overload
def BulkTverskySimilarity(v1: IntSparseIntVect, v2: list, a: float, b: float, returnDistance: bool = False) -> list:
    """
        return the Tversky similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class RDKit::SparseIntVect<int>,class boost::python::list,double,double [,bool=False])
    """
@typing.overload
def BulkTverskySimilarity(v1: LongSparseIntVect, v2: list, a: float, b: float, returnDistance: bool = False) -> list:
    """
        return the Tversky similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class RDKit::SparseIntVect<__int64>,class boost::python::list,double,double [,bool=False])
    """
@typing.overload
def BulkTverskySimilarity(v1: UIntSparseIntVect, v2: list, a: float, b: float, returnDistance: bool = False) -> list:
    """
        return the Tversky similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class RDKit::SparseIntVect<unsigned int>,class boost::python::list,double,double [,bool=False])
    """
@typing.overload
def BulkTverskySimilarity(v1: ULongSparseIntVect, v2: list, a: float, b: float, returnDistance: bool = False) -> list:
    """
        return the Tversky similarities between one vector and a sequence of others
    
        C++ signature :
            class boost::python::list BulkTverskySimilarity(class RDKit::SparseIntVect<unsigned __int64>,class boost::python::list,double,double [,bool=False])
    """
@typing.overload
def ComputeL1Norm(v1: DiscreteValueVect, v2: DiscreteValueVect) -> int:
    """
        Compute the distance between two discrete vector values
        
    
        C++ signature :
            unsigned int ComputeL1Norm(class RDKit::DiscreteValueVect,class RDKit::DiscreteValueVect)
    """
@typing.overload
def ComputeL1Norm(arg1: RealValueVect, arg2: RealValueVect) -> float:
    """
        Compute the distance between two real vector values
        
    
        C++ signature :
            double ComputeL1Norm(class RDKit::RealValueVect,class RDKit::RealValueVect)
    """
def ConvertToExplicit(sbv: SparseBitVect) -> ExplicitBitVect:
    """
        Converts a SparseBitVector to an ExplicitBitVector and returns the ExplicitBitVector
    
        C++ signature :
            class ExplicitBitVect * __ptr64 ConvertToExplicit(class SparseBitVect const * __ptr64)
    """
@typing.overload
def ConvertToNumpyArray(bv: ExplicitBitVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class ExplicitBitVect,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(bv: DiscreteValueVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::DiscreteValueVect,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(bv: IntSparseIntVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::SparseIntVect<int>,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(bv: LongSparseIntVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::SparseIntVect<__int64>,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(bv: UIntSparseIntVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::SparseIntVect<unsigned int>,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(bv: ULongSparseIntVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::SparseIntVect<unsigned __int64>,class boost::python::api::object)
    """
@typing.overload
def ConvertToNumpyArray(rvv: RealValueVect, destArray: typing.Any) -> None:
    """
        C++ signature :
            void ConvertToNumpyArray(class RDKit::RealValueVect,class boost::python::api::object)
    """
@typing.overload
def CosineSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double CosineSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def CosineSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / sqrt(B(bv1) * B(bv2))
    
        C++ signature :
            double CosineSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def CosineSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double CosineSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def CosineSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / sqrt(B(bv1) * B(bv2))
    
        C++ signature :
            double CosineSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def CosineSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / sqrt(B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list CosineSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def CosineSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / sqrt(B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list CosineSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
def CreateFromBinaryText(fps: str) -> ExplicitBitVect:
    """
        Creates an ExplicitBitVect from a binary string (byte array).
    
        C++ signature :
            class ExplicitBitVect * __ptr64 CreateFromBinaryText(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
def CreateFromBitString(bits: str) -> ExplicitBitVect:
    """
        Creates an ExplicitBitVect from a bit string (string of 0s and 1s).
    
        C++ signature :
            class ExplicitBitVect * __ptr64 CreateFromBitString(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
def CreateFromFPSText(fps: str) -> ExplicitBitVect:
    """
        Creates an ExplicitBitVect from an FPS string.
    
        C++ signature :
            class ExplicitBitVect * __ptr64 CreateFromFPSText(class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
@typing.overload
def DiceSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double DiceSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def DiceSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        2*B(bv1&bv2) / (B(bv1) + B(bv2))
    
        C++ signature :
            double DiceSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def DiceSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double DiceSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def DiceSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        2*B(bv1&bv2) / (B(bv1) + B(bv2))
    
        C++ signature :
            double DiceSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def DiceSimilarity(siv1: IntSparseIntVect, siv2: IntSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Dice similarity between two vectors
    
        C++ signature :
            double DiceSimilarity(class RDKit::SparseIntVect<int>,class RDKit::SparseIntVect<int> [,bool=False [,double=0.0]])
    """
@typing.overload
def DiceSimilarity(siv1: LongSparseIntVect, siv2: LongSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Dice similarity between two vectors
    
        C++ signature :
            double DiceSimilarity(class RDKit::SparseIntVect<__int64>,class RDKit::SparseIntVect<__int64> [,bool=False [,double=0.0]])
    """
@typing.overload
def DiceSimilarity(siv1: UIntSparseIntVect, siv2: UIntSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Dice similarity between two vectors
    
        C++ signature :
            double DiceSimilarity(class RDKit::SparseIntVect<unsigned int>,class RDKit::SparseIntVect<unsigned int> [,bool=False [,double=0.0]])
    """
@typing.overload
def DiceSimilarity(siv1: ULongSparseIntVect, siv2: ULongSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Dice similarity between two vectors
    
        C++ signature :
            double DiceSimilarity(class RDKit::SparseIntVect<unsigned __int64>,class RDKit::SparseIntVect<unsigned __int64> [,bool=False [,double=0.0]])
    """
def DiceSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        2*B(bv1&bv2) / (B(bv1) + B(bv2))
    
        C++ signature :
            class boost::python::list DiceSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def DiceSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        2*B(bv1&bv2) / (B(bv1) + B(bv2))
    
        C++ signature :
            class boost::python::list DiceSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def FoldFingerprint(bv: SparseBitVect, foldFactor: int = 2) -> SparseBitVect:
    """
        C++ signature :
            class SparseBitVect * __ptr64 FoldFingerprint(class SparseBitVect [,unsigned int=2])
    """
@typing.overload
def FoldFingerprint(bv: ExplicitBitVect, foldFactor: int = 2) -> ExplicitBitVect:
    """
        Folds the fingerprint by the provided amount. The default, foldFactor=2, returns a fingerprint that is half the size of the original.
    
        C++ signature :
            class ExplicitBitVect * __ptr64 FoldFingerprint(class ExplicitBitVect [,unsigned int=2])
    """
@typing.overload
def InitFromDaylightString(sbv: SparseBitVect, s: str) -> None:
    """
        C++ signature :
            void InitFromDaylightString(class SparseBitVect {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
@typing.overload
def InitFromDaylightString(sbv: ExplicitBitVect, s: str) -> None:
    """
        Fill a BitVect using an ASCII (Daylight) encoding of a fingerprint.
        
           **Arguments**
             - bv: either a _SparseBitVect_ or an _ExplicitBitVect_
             - txt: a string with the Daylight encoding (this is the text that
                    the Daylight tools put in the FP field of a TDT)
        
        
    
        C++ signature :
            void InitFromDaylightString(class ExplicitBitVect {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
    """
@typing.overload
def KulczynskiSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double KulczynskiSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def KulczynskiSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2)*(B(bv1) + B(bv2)) / (2 * B(bv1) * B(bv2))
    
        C++ signature :
            double KulczynskiSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def KulczynskiSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double KulczynskiSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def KulczynskiSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2)*(B(bv1) + B(bv2)) / (2 * B(bv1) * B(bv2))
    
        C++ signature :
            double KulczynskiSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def KulczynskiSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2)*(B(bv1) + B(bv2)) / (2 * B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list KulczynskiSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def KulczynskiSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2)*(B(bv1) + B(bv2)) / (2 * B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list KulczynskiSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def McConnaugheySimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double McConnaugheySimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def McConnaugheySimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        (B(bv1&bv2) * (B(bv1)+B(bv2)) - B(bv1)*B(bv2)) / (B(bv1) * B(bv2))
    
        C++ signature :
            double McConnaugheySimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def McConnaugheySimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double McConnaugheySimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def McConnaugheySimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        (B(bv1&bv2) * (B(bv1)+B(bv2)) - B(bv1)*B(bv2)) / (B(bv1) * B(bv2))
    
        C++ signature :
            double McConnaugheySimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def McConnaugheySimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        (B(bv1&bv2) * (B(bv1)+B(bv2)) - B(bv1)*B(bv2)) / (B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list McConnaugheySimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def McConnaugheySimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        (B(bv1&bv2) * (B(bv1)+B(bv2)) - B(bv1)*B(bv2)) / (B(bv1) * B(bv2))
    
        C++ signature :
            class boost::python::list McConnaugheySimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def NumBitsInCommon(bv1: SparseBitVect, bv2: SparseBitVect) -> int:
    """
        C++ signature :
            int NumBitsInCommon(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def NumBitsInCommon(bv1: ExplicitBitVect, bv2: ExplicitBitVect) -> int:
    """
        Returns the total number of bits in common between the two bit vectors
    
        C++ signature :
            int NumBitsInCommon(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def OffBitProjSimilarity(bv1: SparseBitVect, bv2: SparseBitVect) -> _vectdouble:
    """
        C++ signature :
            class std::vector<double,class std::allocator<double> > OffBitProjSimilarity(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def OffBitProjSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect) -> _vectdouble:
    """
        C++ signature :
            class std::vector<double,class std::allocator<double> > OffBitProjSimilarity(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def OffBitsInCommon(bv1: SparseBitVect, bv2: SparseBitVect) -> _vectint:
    """
        C++ signature :
            class std::vector<int,class std::allocator<int> > OffBitsInCommon(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def OffBitsInCommon(bv1: ExplicitBitVect, bv2: ExplicitBitVect) -> _vectint:
    """
        Returns the number of off bits in common between the two bit vectors
    
        C++ signature :
            class std::vector<int,class std::allocator<int> > OffBitsInCommon(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def OnBitProjSimilarity(bv1: SparseBitVect, bv2: SparseBitVect) -> _vectdouble:
    """
        C++ signature :
            class std::vector<double,class std::allocator<double> > OnBitProjSimilarity(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def OnBitProjSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect) -> _vectdouble:
    """
        Returns a 2-tuple: (B(bv1&bv2) / B(bv1), B(bv1&bv2) / B(bv2))
    
        C++ signature :
            class std::vector<double,class std::allocator<double> > OnBitProjSimilarity(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def OnBitSimilarity(v1: SparseBitVect, v2: SparseBitVect) -> float:
    """
        C++ signature :
            double OnBitSimilarity(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def OnBitSimilarity(v1: ExplicitBitVect, v2: ExplicitBitVect) -> float:
    """
        B(bv1&bv2) / B(bv1|bv2)
    
        C++ signature :
            double OnBitSimilarity(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def OnBitsInCommon(bv1: SparseBitVect, bv2: SparseBitVect) -> _vectint:
    """
        C++ signature :
            class std::vector<int,class std::allocator<int> > OnBitsInCommon(class SparseBitVect,class SparseBitVect)
    """
@typing.overload
def OnBitsInCommon(bv1: ExplicitBitVect, bv2: ExplicitBitVect) -> _vectint:
    """
        Returns the number of on bits in common between the two bit vectors
    
        C++ signature :
            class std::vector<int,class std::allocator<int> > OnBitsInCommon(class ExplicitBitVect,class ExplicitBitVect)
    """
@typing.overload
def RogotGoldbergSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double RogotGoldbergSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def RogotGoldbergSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            double RogotGoldbergSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def RogotGoldbergSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double RogotGoldbergSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def RogotGoldbergSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            double RogotGoldbergSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def RogotGoldbergSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list RogotGoldbergSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def RogotGoldbergSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list RogotGoldbergSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def RusselSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double RusselSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def RusselSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            double RusselSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def RusselSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double RusselSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def RusselSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            double RusselSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def RusselSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list RusselSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def RusselSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / B(bv1)
    
        C++ signature :
            class boost::python::list RusselSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def SokalSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double SokalSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def SokalSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (2*B(bv1) + 2*B(bv2) - 3*B(bv1&bv2))
    
        C++ signature :
            double SokalSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def SokalSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double SokalSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def SokalSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (2*B(bv1) + 2*B(bv2) - 3*B(bv1&bv2))
    
        C++ signature :
            double SokalSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
def SokalSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / (2*B(bv1) + 2*B(bv2) - 3*B(bv1&bv2))
    
        C++ signature :
            class boost::python::list SokalSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def SokalSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / (2*B(bv1) + 2*B(bv2) - 3*B(bv1&bv2))
    
        C++ signature :
            class boost::python::list SokalSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def TanimotoSimilarity(bv1: SparseBitVect, bv2: SparseBitVect, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double TanimotoSimilarity(class SparseBitVect,class SparseBitVect [,bool=0])
    """
@typing.overload
def TanimotoSimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (B(bv1) + B(bv2) - B(bv1&bv2))
    
        C++ signature :
            double TanimotoSimilarity(class ExplicitBitVect,class ExplicitBitVect [,bool=0])
    """
@typing.overload
def TanimotoSimilarity(bv1: SparseBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double TanimotoSimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def TanimotoSimilarity(bv1: ExplicitBitVect, pkl: str, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (B(bv1) + B(bv2) - B(bv1&bv2))
    
        C++ signature :
            double TanimotoSimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> > [,bool=0])
    """
@typing.overload
def TanimotoSimilarity(siv1: IntSparseIntVect, siv2: IntSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tanimoto similarity between two vectors
    
        C++ signature :
            double TanimotoSimilarity(class RDKit::SparseIntVect<int>,class RDKit::SparseIntVect<int> [,bool=False [,double=0.0]])
    """
@typing.overload
def TanimotoSimilarity(siv1: LongSparseIntVect, siv2: LongSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tanimoto similarity between two vectors
    
        C++ signature :
            double TanimotoSimilarity(class RDKit::SparseIntVect<__int64>,class RDKit::SparseIntVect<__int64> [,bool=False [,double=0.0]])
    """
@typing.overload
def TanimotoSimilarity(siv1: UIntSparseIntVect, siv2: UIntSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tanimoto similarity between two vectors
    
        C++ signature :
            double TanimotoSimilarity(class RDKit::SparseIntVect<unsigned int>,class RDKit::SparseIntVect<unsigned int> [,bool=False [,double=0.0]])
    """
@typing.overload
def TanimotoSimilarity(siv1: ULongSparseIntVect, siv2: ULongSparseIntVect, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tanimoto similarity between two vectors
    
        C++ signature :
            double TanimotoSimilarity(class RDKit::SparseIntVect<unsigned __int64>,class RDKit::SparseIntVect<unsigned __int64> [,bool=False [,double=0.0]])
    """
def TanimotoSimilarityNeighbors(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / (B(bv1) + B(bv2) - B(bv1&bv2))
    
        C++ signature :
            class boost::python::list TanimotoSimilarityNeighbors(class boost::python::api::object,class boost::python::api::object)
    """
def TanimotoSimilarityNeighbors_sparse(bvqueries: typing.Any, bvList: typing.Any) -> list:
    """
        B(bv1&bv2) / (B(bv1) + B(bv2) - B(bv1&bv2))
    
        C++ signature :
            class boost::python::list TanimotoSimilarityNeighbors_sparse(class boost::python::api::object,class boost::python::api::object)
    """
@typing.overload
def TverskySimilarity(bv1: SparseBitVect, bv2: SparseBitVect, a: float, b: float, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double TverskySimilarity(class SparseBitVect,class SparseBitVect,double,double [,bool=0])
    """
@typing.overload
def TverskySimilarity(bv1: ExplicitBitVect, bv2: ExplicitBitVect, a: float, b: float, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (a*B(bv1)+b*B(bv2)+(1-a-b)*B(bv1&bv2)
    
        C++ signature :
            double TverskySimilarity(class ExplicitBitVect,class ExplicitBitVect,double,double [,bool=0])
    """
@typing.overload
def TverskySimilarity(bv1: SparseBitVect, pkl: str, a: float, b: float, returnDistance: bool = 0) -> float:
    """
        C++ signature :
            double TverskySimilarity(class SparseBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double [,bool=0])
    """
@typing.overload
def TverskySimilarity(bv1: ExplicitBitVect, pkl: str, a: float, b: float, returnDistance: bool = 0) -> float:
    """
        B(bv1&bv2) / (a*B(bv1)+b*B(bv2)+(1-a-b)*B(bv1&bv2)
    
        C++ signature :
            double TverskySimilarity(class ExplicitBitVect,class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >,double,double [,bool=0])
    """
@typing.overload
def TverskySimilarity(siv1: IntSparseIntVect, siv2: IntSparseIntVect, a: float, b: float, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tversky similarity between two vectors
    
        C++ signature :
            double TverskySimilarity(class RDKit::SparseIntVect<int>,class RDKit::SparseIntVect<int>,double,double [,bool=False [,double=0.0]])
    """
@typing.overload
def TverskySimilarity(siv1: LongSparseIntVect, siv2: LongSparseIntVect, a: float, b: float, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tversky similarity between two vectors
    
        C++ signature :
            double TverskySimilarity(class RDKit::SparseIntVect<__int64>,class RDKit::SparseIntVect<__int64>,double,double [,bool=False [,double=0.0]])
    """
@typing.overload
def TverskySimilarity(siv1: UIntSparseIntVect, siv2: UIntSparseIntVect, a: float, b: float, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tversky similarity between two vectors
    
        C++ signature :
            double TverskySimilarity(class RDKit::SparseIntVect<unsigned int>,class RDKit::SparseIntVect<unsigned int>,double,double [,bool=False [,double=0.0]])
    """
@typing.overload
def TverskySimilarity(siv1: ULongSparseIntVect, siv2: ULongSparseIntVect, a: float, b: float, returnDistance: bool = False, bounds: float = 0.0) -> float:
    """
        return the Tversky similarity between two vectors
    
        C++ signature :
            double TverskySimilarity(class RDKit::SparseIntVect<unsigned __int64>,class RDKit::SparseIntVect<unsigned __int64>,double,double [,bool=False [,double=0.0]])
    """
EIGHTBITVALUE: DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.EIGHTBITVALUE
FOURBITVALUE: DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.FOURBITVALUE
ONEBITVALUE: DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.ONEBITVALUE
SIXTEENBITVALUE: DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.SIXTEENBITVALUE
TWOBITVALUE: DiscreteValueType  # value = rdkit.DataStructs.cDataStructs.DiscreteValueType.TWOBITVALUE

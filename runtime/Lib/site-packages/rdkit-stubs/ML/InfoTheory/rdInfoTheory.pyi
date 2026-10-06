"""
Module containing bunch of functions for information metrics and a ranker to rank bits
"""
from __future__ import annotations
import typing
__all__: list[str] = ['BIASCHISQUARE', 'BIASENTROPY', 'BitCorrMatGenerator', 'CHISQUARE', 'ChiSquare', 'ENTROPY', 'InfoBitRanker', 'InfoEntropy', 'InfoGain', 'InfoType']
class BitCorrMatGenerator(Boost.Python.instance):
    """
    A class to generate a pairwise correlation matrix between a list of bits
    The mode of operation for this class is something like this
    
       >>> cmg = BitCorrMatGenerator() 
       >>> cmg.SetBitList(blist) 
       >>> for fp in fpList:  
       >>>    cmg.CollectVotes(fp)  
       >>> corrMat = cmg.GetCorrMatrix() 
        
       The resulting correlation matrix is a one dimensional nummeric array containing the 
       lower triangle elements
    """
    __instance_size__: typing.ClassVar[int] = 64
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def CollectVotes(self, bitVect: typing.Any) -> None:
        """
            For each pair of on bits (bi, bj) in fp increase the correlation count for the pair by 1
            
            ARGUMENTS:
            
              - fp : a bit vector to collect the fingerprints from
            
        
            C++ signature :
                void CollectVotes(class RDInfoTheory::BitCorrMatGenerator * __ptr64,class boost::python::api::object)
        """
    def GetCorrMatrix(self) -> typing.Any:
        """
            Get the correlation matrix following the collection of votes from a bunch of fingerprints
            
        
            C++ signature :
                struct _object * __ptr64 GetCorrMatrix(class RDInfoTheory::BitCorrMatGenerator * __ptr64)
        """
    def SetBitList(self, bitList: typing.Any) -> None:
        """
            Set the list of bits that need to be correllated
            
             This may for example be their top ranking ensemble bits
            
            ARGUMENTS:
            
              - bitList : an integer list of bit IDs
            
        
            C++ signature :
                void SetBitList(class RDInfoTheory::BitCorrMatGenerator * __ptr64,class boost::python::api::object)
        """
    def __init__(self) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64)
        """
class InfoBitRanker(Boost.Python.instance):
    """
    A class to rank the bits from a series of labelled fingerprints
    A simple demonstration may help clarify what this class does. 
    Here's a small set of vectors:
    
    >>> for i,bv in enumerate(bvs): print(bv.ToBitString(),acts[i])
    ... 
    0001 0
    0101 0
    0010 1
    1110 1
    
    Default ranker, using infogain:
    
    >>> ranker = InfoBitRanker(4,2)  
    >>> for i,bv in enumerate(bvs): ranker.AccumulateVotes(bv,acts[i])
    ... 
    >>> for bit,gain,n0,n1 in ranker.GetTopN(3): print(int(bit),'%.3f'%gain,int(n0),int(n1))
    ... 
    3 1.000 2 0
    2 1.000 0 2
    0 0.311 0 1
    
    Using the biased infogain:
    
    >>> ranker = InfoBitRanker(4,2,InfoTheory.InfoType.BIASENTROPY)
    >>> ranker.SetBiasList((1,))
    >>> for i,bv in enumerate(bvs): ranker.AccumulateVotes(bv,acts[i])
    ... 
    >>> for bit,gain,n0,n1 in ranker.GetTopN(3): print(int(bit),'%.3f'%gain,int(n0),int(n1))
    ... 
    2 1.000 0 2
    0 0.311 0 1
    1 0.000 1 1
    
    A chi squared ranker is also available:
    
    >>> ranker = InfoBitRanker(4,2,InfoTheory.InfoType.CHISQUARE)
    >>> for i,bv in enumerate(bvs): ranker.AccumulateVotes(bv,acts[i])
    ... 
    >>> for bit,gain,n0,n1 in ranker.GetTopN(3): print(int(bit),'%.3f'%gain,int(n0),int(n1))
    ... 
    3 4.000 2 0
    2 4.000 0 2
    0 1.333 0 1
    
    As is a biased chi squared:
    
    >>> ranker = InfoBitRanker(4,2,InfoTheory.InfoType.BIASCHISQUARE)
    >>> ranker.SetBiasList((1,))
    >>> for i,bv in enumerate(bvs): ranker.AccumulateVotes(bv,acts[i])
    ... 
    >>> for bit,gain,n0,n1 in ranker.GetTopN(3): print(int(bit),'%.3f'%gain,int(n0),int(n1))
    ... 
    2 4.000 0 2
    0 1.333 0 1
    1 0.000 1 1
    """
    __instance_size__: typing.ClassVar[int] = 136
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    def AccumulateVotes(self, bitVect: typing.Any, label: int) -> None:
        """
            Accumulate the votes for all the bits turned on in a bit vector
            
            ARGUMENTS:
            
              - bv : bit vector either ExplicitBitVect or SparseBitVect operator
              - label : the class label for the bit vector. It is assumed that 0 <= class < nClasses 
            
        
            C++ signature :
                void AccumulateVotes(class RDInfoTheory::InfoBitRanker * __ptr64,class boost::python::api::object,int)
        """
    def GetTopN(self, num: int) -> typing.Any:
        """
            Returns the top n bits ranked by the information metric
            This is actually the function where most of the work of ranking is happening
            
            ARGUMENTS:
            
              - num : the number of top ranked bits that are required
            
        
            C++ signature :
                struct _object * __ptr64 GetTopN(class RDInfoTheory::InfoBitRanker * __ptr64,int)
        """
    def SetBiasList(self, classList: typing.Any) -> None:
        """
            Set the classes to which the entropy calculation should be biased
            
            This list contains a set of class ids used when in the BIASENTROPY mode of ranking bits. 
            In this mode, a bit must be correlated higher with one of the biased classes than all the 
            other classes. For example, in a two class problem with actives and inactives, the fraction of 
            actives that hit the bit has to be greater than the fraction of inactives that hit the bit
            
            ARGUMENTS: 
            
              - classList : list of class ids that we want a bias towards
            
        
            C++ signature :
                void SetBiasList(class RDInfoTheory::InfoBitRanker * __ptr64,class boost::python::api::object)
        """
    def SetMaskBits(self, maskBits: typing.Any) -> None:
        """
            Set the mask bits for the calculation
            
            ARGUMENTS: 
            
              - maskBits : list of mask bits to use
            
        
            C++ signature :
                void SetMaskBits(class RDInfoTheory::InfoBitRanker * __ptr64,class boost::python::api::object)
        """
    def Tester(self, bitVect: typing.Any) -> None:
        """
            C++ signature :
                void Tester(class RDInfoTheory::InfoBitRanker * __ptr64,class boost::python::api::object)
        """
    def WriteTopBitsToFile(self, fileName: str) -> None:
        """
            Write the bits that have been ranked to a file
        
            C++ signature :
                void WriteTopBitsToFile(class RDInfoTheory::InfoBitRanker {lvalue},class std::basic_string<char,struct std::char_traits<char>,class std::allocator<char> >)
        """
    @typing.overload
    def __init__(self, nBits: int, nClasses: int) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,int,int)
        """
    @typing.overload
    def __init__(self, nBits: int, nClasses: int, infoType: InfoType) -> None:
        """
            C++ signature :
                void __init__(struct _object * __ptr64,int,int,enum RDInfoTheory::InfoBitRanker::InfoType)
        """
class InfoType(Boost.Python.enum):
    BIASCHISQUARE: typing.ClassVar[InfoType]  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASCHISQUARE
    BIASENTROPY: typing.ClassVar[InfoType]  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASENTROPY
    CHISQUARE: typing.ClassVar[InfoType]  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.CHISQUARE
    ENTROPY: typing.ClassVar[InfoType]  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.ENTROPY
    __slots__: typing.ClassVar[tuple] = tuple()
    names: typing.ClassVar[dict]  # value = {'ENTROPY': rdkit.ML.InfoTheory.rdInfoTheory.InfoType.ENTROPY, 'BIASENTROPY': rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASENTROPY, 'CHISQUARE': rdkit.ML.InfoTheory.rdInfoTheory.InfoType.CHISQUARE, 'BIASCHISQUARE': rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASCHISQUARE}
    values: typing.ClassVar[dict]  # value = {1: rdkit.ML.InfoTheory.rdInfoTheory.InfoType.ENTROPY, 2: rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASENTROPY, 3: rdkit.ML.InfoTheory.rdInfoTheory.InfoType.CHISQUARE, 4: rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASCHISQUARE}
def ChiSquare(resArr: typing.Any) -> float:
    """
        Calculates the chi squared value for a variable
        
           ARGUMENTS:
        
             - varMat: a Numeric Array object
               varMat is a Numeric array with the number of possible occurrences
                 of each result for reach possible value of the given variable.
        
               So, for a variable which adopts 4 possible values and a result which
                 has 3 possible values, varMat would be 4x3
        
           RETURNS:
        
             - a Python float object
        
    
        C++ signature :
            double ChiSquare(class boost::python::api::object)
    """
def InfoEntropy(resArr: typing.Any) -> float:
    """
        calculates the informational entropy of the values in an array
        
          ARGUMENTS:
            
            - resMat: pointer to a long int array containing the data
            - dim: long int containing the length of the _tPtr_ array.
        
          RETURNS:
        
            a double
        
    
        C++ signature :
            double InfoEntropy(class boost::python::api::object)
    """
def InfoGain(resArr: typing.Any) -> float:
    """
        Calculates the information gain for a variable
        
           ARGUMENTS:
        
             - varMat: a Numeric Array object
               varMat is a Numeric array with the number of possible occurrences
                 of each result for reach possible value of the given variable.
        
               So, for a variable which adopts 4 possible values and a result which
                 has 3 possible values, varMat would be 4x3
        
           RETURNS:
        
             - a Python float object
        
           NOTES
        
             - this is a dropin replacement for _PyInfoGain()_ in entropy.py
        
    
        C++ signature :
            double InfoGain(class boost::python::api::object)
    """
BIASCHISQUARE: InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASCHISQUARE
BIASENTROPY: InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.BIASENTROPY
CHISQUARE: InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.CHISQUARE
ENTROPY: InfoType  # value = rdkit.ML.InfoTheory.rdInfoTheory.InfoType.ENTROPY

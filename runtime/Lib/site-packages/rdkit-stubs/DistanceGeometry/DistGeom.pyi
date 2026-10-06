"""
Module containing functions for basic distance geometry operations
"""
from __future__ import annotations
import typing
__all__: list[str] = ['DoTriangleSmoothing', 'EmbedBoundsMatrix']
def DoTriangleSmoothing(boundsMatrix: typing.Any, tol: float = 0.0) -> bool:
    """
        Do triangle smoothing on a bounds matrix
        
         
         ARGUMENTS:
        
            - mat: a square Numeric array of doubles containing the bounds matrix, this matrix
                   *is* modified by the smoothing
         
         RETURNS:
        
            a boolean indicating whether or not the smoothing worked.
        
        
    
        C++ signature :
            bool DoTriangleSmoothing(class boost::python::api::object [,double=0.0])
    """
def EmbedBoundsMatrix(boundsMatrix: typing.Any, maxIters: int = 10, randomizeOnFailure: bool = False, numZeroFail: int = 2, weights: list = [], randomSeed: int = -1) -> typing.Any:
    """
        Embed a bounds matrix and return the coordinates
        
         
         ARGUMENTS:
        
            - boundsMatrix: a square Numeric array of doubles containing the bounds matrix, this matrix
                   should already be smoothed
            - maxIters: (optional) the maximum number of random distance matrices to try
            - randomizeOnFailure: (optional) toggles using random coords if a matrix fails to embed
            - numZeroFail: (optional) sets the number of zero eigenvalues to be considered a failure
            - weights: (optional) a sequence of 3 sequences (i,j,weight) indicating elements of 
               the bounds matrix whose weights should be adjusted
            - randomSeed: (optional) sets the random number seed used for embedding
         
         RETURNS:
        
            a Numeric array of doubles with the coordinates
        
        
    
        C++ signature :
            struct _object * __ptr64 EmbedBoundsMatrix(class boost::python::api::object [,int=10 [,bool=False [,int=2 [,class boost::python::list=[] [,int=-1]]]]])
    """

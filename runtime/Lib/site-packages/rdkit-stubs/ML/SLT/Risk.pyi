"""
 code for calculating empirical risk

"""
from __future__ import annotations
import math as math
__all__: list[str] = ['BurgesRiskBound', 'CherkasskyRiskBound', 'CristianiRiskBound', 'log2', 'math']
def BurgesRiskBound(VCDim, nData, nWrong, conf):
    """
     Calculates Burges's formulation of the risk bound
    
        The formulation is from Eqn. 3 of Burges's review
        article "A Tutorial on Support Vector Machines for Pattern Recognition"
         In _Data Mining and Knowledge Discovery_ Kluwer Academic Publishers
         (1998) Vol. 2
    
        **Arguments**
    
          - VCDim: the VC dimension of the system
    
          - nData: the number of data points used
    
          - nWrong: the number of data points misclassified
    
          - conf: the confidence to be used for this risk bound
    
    
        **Returns**
    
          - a float
    
        **Notes**
    
         - This has been validated against the Burges paper
    
         - I believe that this is only technically valid for binary classification
    
      
    """
def CherkasskyRiskBound(VCDim, nData, nWrong, conf, a1 = 1.0, a2 = 2.0):
    """
    
    
        The formulation here is from Eqns 4.22 and 4.23 on pg 108 of
        Cherkassky and Mulier's book "Learning From Data" Wiley, 1998.
    
        **Arguments**
    
          - VCDim: the VC dimension of the system
    
          - nData: the number of data points used
    
          - nWrong: the number of data points misclassified
    
          - conf: the confidence to be used for this risk bound
    
          - a1, a2: constants in the risk equation. Restrictions on these values:
    
              - 0 <= a1 <= 4
    
              - 0 <= a2 <= 2
    
        **Returns**
    
          - a float
    
    
        **Notes**
    
         - This appears to behave reasonably
    
         - the equality a1=1.0 is by analogy to Burges's paper.
    
      
    """
def CristianiRiskBound(VCDim, nData, nWrong, conf):
    """
    
        the formulation here is from pg 58, Theorem 4.6 of the book
        "An Introduction to Support Vector Machines" by Cristiani and Shawe-Taylor
        Cambridge University Press, 2000
    
    
        **Arguments**
    
          - VCDim: the VC dimension of the system
    
          - nData: the number of data points used
    
          - nWrong: the number of data points misclassified
    
          - conf: the confidence to be used for this risk bound
    
    
        **Returns**
    
          - a float
    
        **Notes**
    
          - this generates odd (mismatching) values
    
      
    """
def log2(x):
    ...

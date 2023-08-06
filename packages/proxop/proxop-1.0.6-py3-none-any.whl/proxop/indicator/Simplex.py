"""
Version : 1.0 ( 06-8-2022).

Author  : Mbaye DIONGUE

DEPENDENCIES:
   -'Max.py' in the folder 'multi'

Copyright (C) 2019

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union, Optional
import numpy as np
from proxop.multi.Max import Max


class Simplex:
    """Compute the projection and the indicator of the simplex.

    Recall: every vector X belonging to the simplex verifies:

                    x >= 0 and  (1,..., 1).T * X = eta


     where (1, ..., 1) is a ND array with all components equal to one,
     and (1,..., 1).T its transpose

     INPUTS
    ========
     x    - ND array
     eta  - positive, scalar or ND array compatible with the blocks of 'x'
     axis - int or None, direction of block-wise processing [DEFAULT: axis=None]
            When the input 'x' is an array, the computation can vary as follows:
            - axis = None --> 'x' is processed as a single vector
            - axis >= 0 --> 'x' is processed block-wise along the specified axis
              (axis=0 -> rows, axis=1 -> columns etc.).
    """

    def __init__(
            self,
            eta: Union[float, np.ndarray],
            axis: Optional[int] = None
    ):
        if np.any(eta <= 0):
            raise Exception(
                "'eta' (or all of its components if it is an array) must be positive"
            )
        self.eta = eta
        self.axis = axis

    # proximal operator (i.e projection onto the simplex)
    def prox(self, x: np.ndarray) -> np.ndarray:
        if len(np.shape(x))==2 and self.axis==0:
            p, n = np.shape(x)
            u = np.sort(x, axis=0)[::-1, ...]
            pi = np.cumsum(u, axis=0) - self.eta
            ind = (np.arange(p) + 1).reshape(-1, 1)
            mask = (u - pi / ind) > 0
            rho = p - 1 - np.argmax(mask[::-1, ...], axis=0)
            theta = pi[tuple([rho, np.arange(n)])] / (rho + 1)
            w = np.maximum(x - theta, 0)
            return w
        elif len(np.shape(x))==2 and self.axis==1:
            x = np.transpose(x)
            p, n = np.shape(x)
            u = np.sort(x, axis=0)[::-1, ...]
            pi = np.cumsum(u, axis=0) - self.eta
            ind = (np.arange(p) + 1).reshape(-1, 1)
            mask = (u - pi / ind) > 0
            rho = p - 1 - np.argmax(mask[::-1, ...], axis=0)
            theta = pi[tuple([rho, np.arange(n)])] / (rho + 1)
            w = np.maximum(x - theta, 0)
            return w.T
        return x - Max(axis=self.axis).prox(x, gamma=self.eta)

    # indicator of the simplex
    def __call__(self, x: np.ndarray, tol: float=1e-10) -> float:
        """
        Indicate if the input 'x' is in the  simplex with a tolerance of 'tol'.
        Parameters
        ----------
        x : np.ndarray
        tol: float, error tolerated in comparisons of equality.
        Returns
        -------
        0      if the input 'x' is in the Simplex
        +inf   otherwise
        """
        scalar_prod = np.sum(x, axis=self.axis)
        if np.all(x >= 0) and np.all(np.abs(scalar_prod-self.eta)<=tol):
            return 0
        return np.inf

"""
Version : 1.0 ( 06-13-2022).

DEPENDENCIES:
     - 'fun_svd.py' located in the folder 'utils'
     - 'prox_svd.py' located in the folder 'utils'
     - 'AbsValue.py' located in the folder 'utils'

Author  : Mbaye Diongue

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union
import numpy as np
from proxop.scalar.AbsValue import AbsValue
from proxop.utils.prox_svd import prox_svd


class NuclearNorm:
    r"""Compute the proximity operator and the evaluation of gamma*f.

    Where f is the function defined as:


                        f(x) = ||X||_N = ||s||_1

            where X = U*diag(s)*V.T \in R^{M*N}

     INPUTS
    ========
     x         - (M,N) -array_like ( representing an M*N matrix )
     gamma     - positive, scalar or ND array compatible with the size of 'x'
    """

    def __init__(self):
        pass

    def prox(self, x: np.ndarray, gamma: Union[float, np.ndarray] = 1) -> np.ndarray:
        if np.any(gamma <= 0):
            raise Exception(
                "'gamma' (or all of its components if it is an array)" +
                " must be strictly positive"
            )
        return prox_svd(x, gamma, AbsValue().prox)

    def __call__(self, x: np.ndarray) -> float:
        return np.linalg.norm(x, ord='nuc')

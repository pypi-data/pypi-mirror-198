"""
Version : 1.0 (06-19-2022).

Author  : Mbaye DIONGUE

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union, Optional
import numpy as np


class TruncatedNorm:
    r"""Compute the proximity operator and the evaluation of the gamma*f.

    where the function f is defined as:

         f(x)= min{ ||x||_2^2, w}

     'gamma' is the gamma factor

     INPUTS
     ========
     x     - ND array
     gamma - positive, scalar [default: gamma=1]
     w     - positive, scalar or ND array compatible with the blocks of 'x'
     axis  - None or int, axis of block-wise processing [default: axis=None]
              axis = None --> 'x' is processed as a single vector [DEFAULT] In this
              case 'gamma' must be a scalar.
              axis >=0   --> 'x' is processed block-wise along the specified axis
              (0 -> rows, 1-> columns ect. In this case, 'gamma' must be singleton
              along 'axis'.
    """

    def __init__(
        self,
        w: Union[float, np.ndarray],
        axis: Optional[int] = None
    ):

        if np.any(w <= 0):
            raise ValueError("'w'  must be strictly positive")
        self.axis = axis
        self.w = w

    def prox(self, x: np.ndarray, gamma: Union[float, np.ndarray] = 1.0) -> np.ndarray:
        self._check(x, gamma)
        w = self.w
        sz0 = np.shape(x)
        if np.size(x) <= 1:
            x = np.reshape(x, (-1))
        sz = np.shape(x)
        axis = self.axis
        sz = np.array(sz, dtype=int)
        sz[axis] = 1

        if np.size(w) > 1:
            w = np.reshape(w, sz)
        if np.size(gamma) > 1:
            gamma = np.reshape(gamma, sz)
        mask = np.sum(x**2, axis=axis).reshape(sz) < w * (1 + 2 * gamma)
        prox_x = x / (1 + 2 * gamma * mask)
        prox_x = np.reshape(prox_x, sz0)
        return prox_x

    def __call__(self, x: np.ndarray) -> float:
        res = np.minimum(np.sum(x**2, axis=self.axis), self.w)
        return np.sum(res)

    def _check(self, x, gamma):
        sz = np.shape(x)
        if np.any(gamma <= 0):
            raise ValueError("'gamma'  must be strictly positive")
        if len(sz) <= 1:
            self.axis = None
        if len(sz) <= 1 and (np.size(gamma) > 1 or np.size(self.w) > 1):
            raise ValueError(
                "'gamma' and 'w' must be scalars when 'x' is one dimensional"
            )
        if len(sz) > 1 and self.axis is not None:
            sz = np.array(sz, dtype=int)
            sz[self.axis] = 1
            if 1 < np.size(gamma) != np.prod(sz):
                raise ValueError(
                    "The dimension of 'gamma' is not"
                    + " compatible with the blocks of 'x'"
                )
            if np.size(self.w) > 1 and (np.prod(sz) != np.size(self.w)):
                raise ValueError(
                    "The dimension of 'w' is not compatible with the blocks of 'x'"
                )

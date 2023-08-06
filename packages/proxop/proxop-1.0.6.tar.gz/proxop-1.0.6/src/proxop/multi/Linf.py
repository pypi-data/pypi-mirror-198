"""
Version : 1.0 ( 06-22-2022).

DEPENDENCIES:
    - 'Max.py' located in the folder 'multi'

Author  : Mbaye Diongue

Copyright (C) 2022

This file is part of the codes provided at http://proximity-operator.net

By downloading and/or using any of these files, you implicitly agree to
all the terms of the license CeCill-B (available online).
"""

from typing import Union, Optional
import numpy as np
from proxop.multi.Max import Max


class Linf(Max):
    r"""Compute the proximity operator and the evaluation of gamma*f.

    Where f is the infinitive norm:

                        f(x) = gamma *tau* max( |x1|, ..., |xn|)

    INPUTS
    ========
     x         - ND array
     gamma     - positive, scalar or ND array compatible with the blocks of 'x'
                 [default: gamma=1], 'gamma' is the scale factor
     axis    - None or int, axis of block-wise processing [default: axis=None]
                  axis = None --> 'x' is processed as a single vector [DEFAULT] In this
                  case 'gamma' must be a scalar.
                  axis >=0   --> 'x' is processed block-wise along the specified axis
                  (0 -> rows, 1-> columns ect. In this case, 'gamma' must be singleton
                  along 'axis'.
    """

    def __init__(
            self,
            axis: Optional[int] = None
    ):
        super().__init__(axis=axis)

    def prox(self, x: np.ndarray, gamma: Union[float, np.ndarray] = 1.0) -> np.ndarray:
        abs_x = np.abs(x)
        return np.sign(x) * Max(axis=self.axis).prox(abs_x, gamma)

    def __call__(self, x: np.ndarray) -> float:
        linf_x = np.max(np.abs(x), self.axis)
        return np.sum(linf_x)

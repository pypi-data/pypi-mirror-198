# -*- coding: utf-8 -*-

import numpy as np

def get_cosine(num_intervals: int = 10) -> np.ndarray:
    x = np.linspace(0, 2 * np.pi, num=num_intervals)
    y = np.cos(x)
    return y
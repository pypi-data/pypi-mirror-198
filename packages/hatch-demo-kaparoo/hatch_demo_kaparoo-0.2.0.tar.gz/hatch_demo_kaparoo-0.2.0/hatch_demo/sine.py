# -*- coding: utf-8 -*-

import numpy as np

def get_sine(num_intervals: int = 10) -> np.ndarray:
    x = np.linspace(0, 2 * np.pi, num=num_intervals)
    y = np.sin(x)
    return y
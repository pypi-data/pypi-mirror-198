# -*- coding: utf-8 -*-

import numpy as np

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("`matplotlib is not installed!`")


def plot_graph(g: np.ndarray):
    plt.plot(g)
    plt.show()
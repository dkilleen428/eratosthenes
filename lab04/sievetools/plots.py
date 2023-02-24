import sys
import math
import numpy as np
import matplotlib.pyplot as plt

def plt_prop(all_nmax, all_proportions, log_scale=False):
    if log_scale == True:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        plt.xscale("log")
        plt.yscale("log")
        return plt
    else:
        plt.plot(all_nmax, all_proportions)
        plt.xlabel("N")
        plt.ylabel("Proportion of primer numbers")
        return plt
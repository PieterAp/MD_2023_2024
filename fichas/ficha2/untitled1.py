#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:04:29 2024

@author: pieter
"""

import numpy as np
import matplotlib.pyplot as plt


x=np.array([1, 2.5, 5,10.3])


def f(X):
    return x**3+3*x+5

X = np.arange(-2,2-0.1)
plt.plot(X,f(X))
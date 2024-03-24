"""
Created on Fri Mar 22 15:18:50 2024

@author: pieter
TRABALHO
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

range(15,50)

U=set(range(15,1501,1))
U

U1={2**(k-10) for k in range(15,50) if 2**(k-10) < 1500}
U2=set(range(0,1501,4))
Uaux=set(range(0,1501,4))

U3=set(); n=1; u=1499
while u<1500:
    n=n+1
    
    if n<5:
        u=1500-n**5
    else:
        u=17*(n-4)**3
    U3.add(u)
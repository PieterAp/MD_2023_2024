"""
Created on Fri Mar  8 15:06:33 2024

@author: pieter
ficha 2
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt


#%% Ex1
#a
def f(x):
    return np.cos(x) + np.exp(x)

#b
f(0)
f(mt.pi)

#c
x=np.linspace(1, 2, 98)

#d
y=f(x)

#e
plt.plot(x,y,'r')
#%%


#%% Ex2
def f(x):
    return x**5-3*x**4-3*x**3+7*x**2+6*x

x=np.arange(-1.5,2.5+0.125,0.125)
y=f(x)

plt.plot(x,y,'r')
plt.title("Gráfico da função f")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["$f(x)=x^2-3x^4-3x^3+7x^2+6x$"], loc='lower center', fontsize='12')
plt.show()
#%%


#%% Ex3
def r(t):
    Co = 10 #quantidade inicial ---» gramas
    v = 140 #tempo de meia-vida ---» dias
    return Co * (0.5)**(t/v)

x=np.arange(0,(7*10)+7,7)
y=np.array([])
for n in range(0,(7*10)+7,7):
    y=np.append(y, r(n))
plt.plot(x,y,"r.")
y
#%%


#%% Ex4
def Z(n):
    sum=0
    k=1
    while k<=n:
        sum += (1/2)**k
        k+=1
    return sum
#a
x=np.arange(1,21)
y=np.array([])
for n in range(1,21,1):
    y=np.append(y, Z(n))
plt.plot(x,y,"r.")

#b
n=2
while (abs(Z(n) - Z(n-1)) >= 10**(-10)):
    if ((abs(Z(n) - Z(n-1)) >= 10**(-10))):
        n+=1
        
n
#%%


#%% Ex5
#a
def S(n):
    if (n%3==0):
        return 2**(-n/10)*(n/3)
    else:
        return 3**(-n/10)*n
        
x=np.arange(0,71)
y=np.array([])
for n in range(0,71,1):
    y=np.append(y, S(n))
plt.plot(x,y,"g*")

#b
def soma(n):
    sum=0
    k=1
    while k<=n:
        sum += S(k)
        k+=1
    return sum

n=0
while (soma(n) < 42):
    if (soma(n) < 42):
        n+=1    

n
#%%
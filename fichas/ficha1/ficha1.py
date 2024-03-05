"""
Created on Tue Mar  5 19:58:27 2024

@author: pieter
ficha 1
"""

import math as mt

#%% Ex1
#a
(35.6*64-7**3)/(45+5**2)

#b
5/7*4*6**2-((3**7)/(9**3-236))

#c
((3**2*mt.log10(76))/(7**3+54))+910**(1/3)

#d
(mt.cos(5*mt.pi/6))**2*mt.sin((7*mt.pi/8)**2)+((mt.tan(mt.pi/6*mt.log(8)))/(7**(1/2)))
#%%


#%% Ex2
x=13.5
#a
x**3-2*x+23.5*x**2

#b
((14*x**3)**(1/2)/(mt.e**(3*x)))

#c
mt.log10(abs(x**2-x**3))
#%%.


#%% Ex3
a=15.62; b=-7.08; c=62.5; d=0.5*(a*b-c)
#a
ex3a = a+(a*b)/c*((a+d)**2/(abs(a*b)**(1/2)))

#b
print("A solução da alínea 3 a) é", str(round(ex3a,5)))
#%%


#%% Ex4
p=True; q=False
a=p or q
#%%


#%% Ex5
p=True; q=False; w=True
#a
a=p and q

#b
b=(p or q) and (not q and w)
#%%

#%% Ex6
#a
ex6a = mt.log(16) > 0
print("O logaritmo neperiano de 16 é um valor positivo. => ", ex6a)

#b
ex6b = mt.tan(mt.radians(45)) > mt.sin(mt.radians(90)) 
print("A tangente de 45 graus é maior do que o seno de 90 graus. => ", ex6b)
#%%
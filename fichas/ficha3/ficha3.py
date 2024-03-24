"""
Created on Fri Mar 15 15:51:56 2024

@author: pieter
ficha 3
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt


#%% Ex1
A={1,2,3,4}
B={3,4,5,6,7}
C={1,5,9,10}

#a
U=A|B|C

#b
len(U)

#c
U-A

#d
A-B

#e
A^B #(A|B)-
#%%


#%% Ex2
A={0,1,2,4,8}
B={3,5}
C={4,6,8}

#a
len(A & C)

#b
A ^ (B | C)
#%%


#%% Ex3
def simdiff(A,B):
    return (A | B) - (A & B)
simdiff(A, B)
#%%


#%% Ex4
A={0,2,5,8,9}
B={2,3,5}
U={0,1,2,3,4,5,6,7,8,9}

#a
len(A)

#b
simdiff(A,B) & U
#%%


#%% Ex5
A=set(range(3,100,3))
B=set(range(70,140+7,7))
C=A ^ B

#a
B

#b
len((A | C) & B)
#%%


#%% Ex6
cards=set(range(1,411,1))

#a
numPares=set(range(2,411,2))
mults7=set(range(7,411,7))
len(numPares - mults7)

#b
Quad=set()
i=1
while (i<410):
    if (mt.sqrt(i)==int(mt.sqrt(i))):
        Quad.add(i)
    i+=1
Quad    

#teacher's solution (?????)
"""
Quad=set()
i=0
while i**2<410:
    Quad=Quad | {i**2}
    i=i+1
"""

#c
mults3=set(range(3,411,3))
mults3 - Quad
#%%


#%% Ex7
Lista_Atividades = ["Futebol", "Ioga", "Cinema", "Futebol", "Concertos", "Cinema", "Concertos"]
conjunto_atividades = set(Lista_Atividades)
#%%


#%% Ex8
B={1,2,3,4}
P=list([{1},{2},{3,4}])

#intersecção dá conjunto vazio?
(P[0]&P[1]) == set() & (P[0]&P[2]) == set() & (P[1]&P[2]) == set()

#união dá o conjunto B?
P[0]|P[1]|P[2]==B
#%%


#%% Ex9
def isPartition(conj, particao):
    AuxSet=set()
    
    for i in range(0,len(particao),1):
        if (particao[i] & AuxSet == set()):
            AuxSet = AuxSet | P[i] #add elements to auxiliar set
        else:
            print("Is not a partition")
            return False
        
    if (AuxSet == B):
        print("Is a partition")
        return True
    else:
        print("Is not a partition")
        return False

B={1,2,3,4}
P=list([{1},{2},{3,4}])
isPartition(B, P)

#teachers version(?????)
"""
for i:0; n-1, i++:
    for j:i+1, n, j++:
        if P[i] intercpt P[j] != set():
            return False
"""
#%%

"""
Created on Fri May  3 16:21:36 2024

@author: pieter
ficha 6
"""

import numpy as np
from numpy.linalg import matrix_power as mpower
import matplotlib.pyplot as plt
import math as mt
import pandas as pd

import networkx as nx
arestas=[('X', 'Y'), ('X', 'Z'), ('X', 'W'), ('Y', 'W'), ('Z', 'Y'), ('Z', 'W'), ('W', 'Z')]
G=nx.DiGraph(arestas)
nx.draw_networkx(G,node_color="pink", node_size=1000, font_color='black', arrowsize=25)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     

pos={'x': [0,1], 'Y':[1,1], 'Z':[0,0],'W':[1,0]}
arestas =[('X', 'Y'), ('X', 'Z'), ('X', 'W'),('Y', 'W'), ('Z', 'Y'), ('Z', 'W'), ('W', 'Z')]
G=nx.DiGraph(arestas)
nx.draw_networkx(G, pos, node_color='pink', node_size=1000, font_color='black', arrowsize=25)



FICHEIRO = pd.ExcelFile('MAdj_ex1.xlsx')
F1 = pd.read_excel(FICHEIRO, 'MAdj', header=None)
M=F1.to_numpy()



G = nx.DiGraph(M)
nx.draw_networkx(G)


####

#fortemente conexo
Soma=M.copy()

for i in range(2,7):
    Soma += mpower(M, i) # o 4 é um poço, e ja sabemos visualmente que nao e fortemente conexo

Soma[Soma!=0]=1
P=Soma.copy()


if (P==np.ones((6,6))).all():
    print("É fortemente conexo")
else:
    print("Não é fortemente conexo")
    
    
    
    
#unilateralmente conexo
Aux=(P+P.T+np.eye(6))
Aux[Aux!=0]=1

if (Aux==np.ones((6,6))).all():
    print("É unilateralmente conexo")
else:
    print("Não é unilateralmente conexo")

#caso nao nos lembremos disto, fazemos:
flag=True
for i in range(6):
    for j in range(6):
        if i!=j and P[i,j]==0 and P[j,i]==0:
            flag=False
            break
    if not flag:
        break
print(flag)









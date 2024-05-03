"""
Created on Fri Apr 12 16:32:00 2024

@author: pieter
ficha 5
"""

import numpy as np
from numpy.linalg import matrix_power as mpower
import matplotlib.pyplot as plt
import math as mt


ctrl+m
MR = np.array([np.array([[1, 0, 1, 0],
                         [1, 1, 1, 1]])
])

"""
A inversa da matriz é calculada com a transposta
"""

# a composição de funcoes, recebe uma matriz, dois ciclos for linha e colunas
# a composição de funcoes é multiplicar as matrizes, todos os valores !=0 ficam a 1

# reflexiva = matriz identidade a 1's
# simetrica = transposta

"""
Aula sexta 19 Apr
composicao de funcoes  -» multiplicação de matrizes

para a matriz da relação for reflexiva, a diagonal principal tem só 1's
    com o calc do traco da matriz
    ou vendo se tem 1's ou 0's na diagonal principal
    
para a matriz da relação for simẽtrica, temos que ver se é igual á transposta
    M=M^T 
    ou sem calculos manhosos, dois ciclos for, dentro ver se Mr[i,j] == Mr[j,i]
        apesar de funcionar estamos a duplicar a quantidade de checks
            podemos apenas percorrer o triangulo superior ou o inferior

para a matriz da relação for antissimétrica, mais facil ver se não for antisssi
    é antisimmtrica se Mr[i,j] != Mr[j,i] a não ser que sejam ambas 0
    dois ciclos de for, i e j, de percorrer apenas a triangular sup ou inf
        Mr[i,j]==1 and Mr[j,i]==1 ===» is not antissimetrica
        
para a matriz da relação for transitiva se R U R² = R
    tenho que aplicar o filtro UM
    
    
    
propriedades de fecho
filtroUm(Mr + Idm)

R U R⁻¹
filtroUm(Mr + Mr.T)

fecho transitivo = Mr + (Mr)² + (Mr)³ + ... + (Mr)^n



a matriz da menor relacao de equivalencia que contem R



»» classes de equivalencia

"""

# %% Ex1
#a
Mr=np.array([[1, 0, 1, 0],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1]])

#b
Mr.T

#c
#filtro um
def F_um(M):
    L,C = M.shape
    for i in range(L):
        for j in range(C):
            if M[i,j] > 1:
                M[i,j] = 1
    return M

MR2=F_um(Mr@Mr)

#OU
MR2 = Mr@Mr
MR2[MR!=0]

MR3=F_um(mpower(Mr, 3))

#d
"""
R não é reflexiva porque na diagonal principal da sua matriz temos zeros;
    ou porque, MR(2,2)=0
-------
R não é simétrica pois MR(1,2)=0 mas MR(2,1)=1
-------
R não é antissimétrica pois MR(1,3)= 1 e MR(3,1)=1 mas 3 é diferente de 1
-------
R não é transitiva pois MR(1,2)=0 e MR(2,1)=1,
    de outra forma, temos o par (1,3) e o par (3,2), mas não temos o (1,2)
"""

#e Determine a matriz:
##i fecho reflexivo
Mref = F_um(Mr + np.eye(4))

##ii fecho simetrico
Msim = F_um(Mr + Mr.T)

##iii fecho transitivo, temos que fazer 4 somas
Mtran = F_um(Mr + mpower(Mr,2) + mpower(Mr,3) + mpower(Mr,4))

#f
#para dar a menor relacao de equivalencia que contem R temos que fazer o 
#fecho simetrico, fecho reflexivo, eee
aux1 = Mr + np.eye(4)
aux2 = aux1 + aux1.T
Mequival = F_um(aux2 + mpower(aux2,2) + mpower(aux2,3) + mpower(aux2,4))


# %%


# %% Ex2
#b 
ver se na posicao 

# %%

# 4,5,6,7 --»» for homework

#8
#1 - nao
#2 - sim
#3 - 

#aula 8 (dia do teste de AM 1)


Mr=np.array([[1, 0, 1, 0],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1]])

#ver se é reflexiva, 
def is_reflexiva(M):
    L,C = np.shape(M)
    return (np.diag(M)==np.diag(np.eye(L))).all()

is_reflexiva(Mr)

def is_simetrica(M):
    return (M==M.T).all()
    
is_simetrica(Mr)

def is_transitiva(M):
    L,C = M.shape
    aux = (M+(M@M))
    aux[aux!=0]=1 #filtro(M+M^2)
    return (aux==M).all()
    
is_transitiva(Mr)

"""
is_antissimetrica
    if i!=j AND M(i,j)==1 AND M(j,i)==1
        FALSE
"""

#fecho reflexivo
def fecho_reflexivo(M):
    L,C = M.shape
    if is_reflexiva(M):
        return M
    else:
        aux = (M+np.eye(L))
        aux[aux!=0]=1
        return aux

fecho_reflexivo(Mr)

#fecho simétrico
def fecho_simetrico(M):
    L,C = M.shape
    if is_simetrica(M):
        return M
    else:
        aux = (M+M.T)
        aux[aux!=0]=1
        return aux
    
fecho_simetrico(Mr)

#fecho transitivo
def fecho_transitivo(M):
    L,C = M.shape
    if is_transitiva(M):
        return M
    else:
        S=np.copy(M)
        for i in range(2,L+1):        
            S+=mpower(M, i)
        
        S[S!=0]=1
        return S
    
fecho_transitivo(Mr)


#relacao de equivalencia

def equival(M):
    if (is_reflexiva(M) and is_simetrica(M) and is_transitiva(M)):
        print("é uma relação de equivalencia")
    else:
        print("Não é uma rel de equivalencia")
        print("A menor relação de equiv que contem a relação R é dada pela seguinte matriz:")
        return fecho_transitivo(fecho_simetrico(fecho_reflexivo(M)))

equival(Mr)

#ex9
#funcao 1 yusss
#funcao 2 nope, falta o filtro
#funcao 3 
"""
Created on Fri Mar 22 15:22:54 2024

@author: pieter
ficha 4
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt


# %% Ex1
# a
mt.ceil(100/8)

# b


def conversor(bits):
    return mt.ceil(bits/8)


conversor(100)  # should return 13
# %%


# %% Ex2
def inteiro(x):
    if x > 0:
        return mt.floor(x)
    return mt.ceil(x)


inteiro(1.3)  # should return 1
inteiro(2.8)  # should return 2
inteiro(-2.3)  # should return -2
inteiro(2)  # should return 2
inteiro(3.8)  # should return 3
inteiro(-4.1)  # should return -4
inteiro(2.4)  # should return 2
inteiro(-2.4)  # should return -2
# %%


# %% Ex3
def bissexto(x):  # x=ano
    if (x % 4 == 0):
        if (x % 100 == 0 and x % 400 != 0):
            return False
        else:
            return True
    else:
        return False


bissexto(1900)  # should return False
bissexto(2024)  # should return True
bissexto(2000)  # should return True
bissexto(2020)  # should return True
bissexto(2100)  # should return False
bissexto(2200)  # should return False
# %%


# %% Ex4
def F(x):
    if (x == 1 or x == 2):
        return 1

    return F(x-1) + F(x-2)

def invertedF(n):
    if n==1 or n==2:
        return 1
    else:
        F0=1
        F1=1

        for i in range(n-2):
            F2=F0+F1
            F0=F1
            F1=F2
    return F2

F(7)  # should return 13
F(15)  # should return 610

F(35)  # should return 9227465
F(40)  # should return 102334155
F(50)  # should return ... cpu too weak
invertedF(50)  # should return 12586269025
# %%


# %% Ex5
def soma_Fib(x):
    Fib_sum = 0
    for i in range(1, x+1):
        Fib_sum += F(i)
    return Fib_sum


soma_Fib(7)  # should return 33
soma_Fib(1)  # should return 1
# %%


# %% Ex6
def termos_Fib(s):
    Fib_list = list()  # use list because a set() wouldn't allow for repeated vaues
    i = 1
    while (soma_Fib(i) <= s):
        #print("Will be adding ",str(F(i))," to the list that contains", str(Fib_list))
        Fib_list.append(F(i))
        i += 1
    return Fib_list


termos_Fib(35)  # should return [1, 1, 2, 3, 5, 8, 13]
termos_Fib(12)  # should return [1, 1, 2, 3, 5]
termos_Fib(11)  # should return [1, 1, 2, 3]
# %%


# %% Ex7
#a
nOuro=(1+5**(1/2))/2
(1+5**(1/2))/2

abs(F(26)/F(26-1))
abs(F(20)/F(20-1))
10**(-10)

X = list()
Y = list()


n=2
while (abs(F(n)/F(n-1) - nOuro) > 10**(-10)):
    X.append(n-1)
    Y.append(F(n)/F(n-1))
    plt.plot(n-1,F(n)/F(n-1),"*")
    n=n+1
n

#b
plt.plot(X,Y,"*")
# %%


# %% Ex8
def Ackermann(x, y):
    if (x == 0):
        return y+1
    if (x > 0 and y == 0):
        return Ackermann(x-1, 1)
    elif (x > 0 and y > 0):
        return Ackermann(x-1, Ackermann(x, y-1))


Ackermann(0, 0)  # should return 1
Ackermann(2, 2)  # should return 7
Ackermann(3, 0)  # should return 5
Ackermann(3, 4)  # should return 125
# %%


# %% Ex9
def santaIsComingToTown(x):  # x=year in format YYYY
    diasDaSemana = ["domingo", "segunda", "terça",
                    "quarta", "quinta", "sexta", "sábado"]
    X = int(str(x)[0])
    Y = int(str(x)[1])
    Z = int(str(x)[2])
    W = int(str(x)[3])
    A = int(str(Z)+str(W))
    seculo = mt.ceil((x/100))

    dia = (50 + A + ((seculo-1)//4)+(A//4)-2*(seculo-1)) % 7
    return diasDaSemana[dia]


santaIsComingToTown(2017)  # should return "segunda"
santaIsComingToTown(2032)  # should return "sábado"
santaIsComingToTown(2050)  # should return "domingo"
santaIsComingToTown(2024)  # should return "quarta"
santaIsComingToTown(1997)  # should return "quinta"
santaIsComingToTown(1985)  # should return "quarta"
# a
santaIsComingToTown(2017)  # should return "segunda"
# b
santaIsComingToTown(2032)  # should return "sábado"
# c
santaIsComingToTown(2050)  # should return "domingo"
# %%


# %% Ex10
# o resto da divisão da expressão por 9 dá 0
# aka a expresão é multiplo de 9

def Nota_euro():
    S=input("Insira o código: ")
    letras=list("RSTUMN")
    
    beta=letras.index(S[0])+1
    
    soma=beta
    
    for i in range(1,12):
        soma+=int(S[i])
    
    if soma%9==0:
        return True
    else:
        return False

Nota_euro()


def Nota_euro(nota):
	letras=list("RSTUMN")
	print(str(letras.index(nota[0]) + 1))
	nota[0] = str(letras.index(nota[0]) + 1)

	soma=0

	for i in range(1,12):
		soma+=int(S[i])


	if soma%9==0:
		return True
	else:
		return False


#a

#b
Nota_euro("M50027558701")
#M50027558701

# %%

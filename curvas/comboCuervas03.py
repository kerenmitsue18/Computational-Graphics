#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Concatenación de curvas de bezier
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción:

Created on Tue Sep 27 12:22:21 2022
@author: computerappliedresearch
"""

import matplotlib.pyplot as plt
import numpy as np


def tercerOrden():
    M2 = np.array( [[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]])
    W2 = np.zeros((len(t),4), dtype=float)
    U = np.ones((len(t),1), dtype=float)
    W2[:,0] = t*t*t
    W2[:,1] = t*t
    W2[:,2] = t[:]
    W2[:,3] = U[:,0]
    return M2, W2
    
#Puntos para la curva
P = np.array([ [2,1],[4,7],[-3,5],[6,12]],dtype=float)
Q = np.array([[6,12],[8,-2],[7,2],[5,4]],dtype=float)
t = np.arange(0,1.01,0.01)


#Puntos de P
M1,W1 = tercerOrden()
B1 = M1@P
B = W1@B1

B2 = M1@Q
C = W1@B2
plt.figure()
plt.subplot(121)
plt.plot(B[:,0], B[:,1])
plt.plot(C[:,0], C[:,1])


#Concatenación de curvas
alpha = 0.8
PQ0 = (1-alpha)*P[1,0] + alpha*Q[1,0]
PQ1 = (1-alpha)*P[1,1] + alpha*Q[1,1]

#Actualizacion 
P[2,0] = PQ0
P[2,1] = PQ1
Q[0,0] = PQ0
Q[0,1] = PQ1


B1 = M1@P
B = W1@B1

B2 = M1@Q
C = W1@B2


plt.subplot(122)
plt.plot(B[:,0], B[:,1])
plt.plot(C[:,0], C[:,1])

plt.show()




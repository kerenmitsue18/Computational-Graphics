#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Transformación: escalado
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: 
    Aplicar una translación a un trángulo
Created on Fri Aug 12 12:44:09 2022

@author: KerenMitsue
"""

import numpy as np 
import matplotlib.pyplot as plt

P = np.array([ [2,3],[-4,7], [1,-5],[2,3] ], dtype=float)
sx = float(input("escriba el factor de escala sx:  "))
sy = float(input("escriba el factor de escla sy: "))
S = np.array([ [sx,0], [0,sy]])
T = P@S

#plt.axis([-10,10,-10,10])
plt.plot(P[:,0], P[:,1])

plt.plot(T[:,0], T[:,1])
plt.grid()
plt.show()

print(T)

A
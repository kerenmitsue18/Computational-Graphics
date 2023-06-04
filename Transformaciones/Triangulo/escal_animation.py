#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional 
Tema: Escalamiento
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: Animacion del escalamiento en una figura (triangulo)

Created on Tue Aug 23 03:40:28 2022

@author: KerenMitsue
"""

import numpy as np 
import matplotlib.pyplot as plt

P = np.array([ [2,3],[-4,7], [1,-5],[2,3] ], dtype=float)
sx = float(input("escriba el factor de escala sx:  "))
sy = float(input("escriba el factor de escla sy: "))
#plt.axis([-20,20,-20,20])
for i in range(1,20):
    S = np.array([ [sx*i,0], [0,sy*i]])
    T = P@S
    plt.plot(P[:,0], P[:,1])
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(0.5)
 
print(T)

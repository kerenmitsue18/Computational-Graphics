# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Transformadas homógeneas
Alumno: Keren Mitsue Ramírez Vergara
Descripción: Expandir y contraer una figura hasta colapsar
(Utilizando coordenadas homógeneas)

Created on Fri Aug 19 00:40:52 2022

@author: KerenMitsue
"""


from Homogeneas import Homogeneas 
import numpy as np
import matplotlib.pyplot as plt

homo = Homogeneas()
P = np.array([ [2,3,1], [3,5,1], [4,4,1],[6,5,1],[7,4,1],[4,2,1],[2,3,1], [2,7,1]])

for i in range(1,10):
    plt.clf()
    plt.axis([0,40,0,40])
    #plt.plot(P[0:-1,0], P[0:-1,1])
    M = homo.escalamiento(P, 0.5*i ,0.5*i)
    plt.plot(M[0:-1,0], M[0:-1,1])
    plt.axis("off")
    plt.pause(0.5)
print (M)

for j in range(10,-2, -1):
    plt.clf()
    plt.axis([0,40,0,40])
    #plt.plot(P[0:-1,0], P[0:-1,1])
    M = homo.escalamiento(P, 0.5*j ,0.5*j)
    plt.plot(M[0:-1,0], M[0:-1,1])
    plt.axis("off")
    plt.pause(0.5)

    
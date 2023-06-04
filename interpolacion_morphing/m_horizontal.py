#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Interpolación lineal
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Realizar una animación donde una figura en forma 
             de casa, se mueva horizontalmente
@author: KerenMitsue
"""
# Horizoontal

import numpy as np
import matplotlib.pyplot as plt

P = np.array([[0,0],[0,4],[1.5,5],[3,4],[3,0],[2,0],[2,1],[1,1],[1,0],[0,0]])

B = np.zeros((10,2))

h = 10
k = 0

B[:, 0] = P[:,  0] + h
B[:, 1] = P[:,  1] + k

T = np.zeros((10,2))

for i in range(50):
    plt.clf()
    plt.axis([0,20,0,20])
    
    t = float(i/50);
    
    T[:, 0] = (1-t) * P[:, 0] + t * B[:, 0]
    T[:, 1] = (1-t) * P[:, 1] + t * B[:, 1]
    
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(0.1)
    
    
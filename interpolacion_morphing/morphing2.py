# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Morphing
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Aplicar Morphing a una figura de más de 6 puntos

Created on Sat Aug 27 19:28:59 2022

@author: KerenMitsue
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([ [5,8],[7,10],[7,8],[9,8],[7,6],[9,4],[7,4],[7,2],[5,4],[3,2],
              [3,4],[1,4],[3,6],[1,8],[3,8],[3,10],[5,8]])
B = np.array([ [16,28],[18,26],[19,28],[20,26],[21,28],[22,26],[23,28],
              [24,26],[24,23],[22,22],[21,22],[21,16],[19,16],[19,22],
              [18,22],[16,23],[16,28]])

T = np.zeros((17,2))

for i in range(11):
    plt.clf()
    plt.axis([0,30,0,30])
    t = float(i/10);
    
    T[:, 0] = (1-t) * A[:, 0] + t * B[:, 0]
    T[:, 1] = (1-t) * A[:, 1] + t * B[:, 1]
    
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(1)
    
   
    

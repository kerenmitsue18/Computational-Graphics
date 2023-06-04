# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Morphing
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Aplicar Morphing a una figura de entre 40-60 puntos
             en 3D
Created on Sat Aug 27 19:28:59 2022
@author: KerenMitsue
"""
from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

B1 = np.array([  [-2.42,0,0],[0.32,-2.04,0],[3.11,-0.06,0],[2.09,3.2,0],
    [-1.33,3.24,0],[-2.42,0,0],[-4.13,-0.53,2.91],[-2.45,-2.91,4.7],
    [0.3,-3.84,2.91],[0.32,-2.04,0],[0.3,-3.84,2.91],[3.07,-2.97,4.7],
    [4.81,-0.64,2.91],[3.11,-0.06,0],[4.81,-0.64,2.91],[4.84,2.27,4.7],
    [3.16,4.69,2.91],[2.09,3.2,0],[3.16,4.69,2.91],[0.41,5.57,4.7],
    [-2.37,4.7,2.91],[-1.33,3.24,0],[-2.37,4.7,2.91],[-4.1,2.37,4.7],
    [-4.13,-0.53,2.91],[-2.42,0,0],[-4.13,-0.53,2.91],[-2.45,-2.91,4.7],
    [-1.38,-1.47,7.61],[-2.4,1.8,7.61],[-4.1,2.37,4.7],[-2.4,1.8,7.61],
    [0.39,3.77,7.61],[0.41,5.57,4.7],[0.39,3.77,7.61],[3.13,1.75,7.61],
    [4.84,2.27,4.7],[3.13,1.75,7.61],[2.03,-1.51,7.61],[3.07,-2.97,4.7],
    [2.03,-1.51,7.61],[-1.38,-1.47,7.61],[-1.38,-1.47,7.61],
    [-1.38,-1.47,7.61],[-1.38,-1.47,7.61],[-1.38,-1.47,7.61],
    [-1.38,-1.47,7.61],[-1.38,-1.47,7.61],[-1.38,-1.47,7.61],
    [-1.38,-1.47,7.61],[-1.38,-1.47,7.61],[-1.38,-1.47,7.61],
    [-1.38,-1.47,7.61],[-1.38,-1.47,7.61],[-1.38,-1.47,7.61],
    [-1.38,-1.47,7.61],[-1.38,-1.47,7.61]  ])


B2 = np.array([ [28.25,16.45,0], [20.8,12.33,0],[28.09,7.94,0],
   [28.25,16.45,0],[33.66,12.1,4.91],[29.82,19.05,7.95],[28.25,16.45,0],
   [21.87,19.2,4.91],[29.82,19.05,7.95],[28.25,16.45,0],[29.82,19.05,7.95],
   [23.34,16.54,12.86],[21.87,19.2,4.91],[29.82,19.05,7.95],
   [30.63,12.15,12.86],[23.34,16.54,12.86],[29.82,19.05,7.95],
   [30.63,12.15,12.86],[33.66,12.1,4.91],[29.82,19.05,7.95],[33.66,12.1,4.91],
   [28.25,16.45,0],[28.09,7.94,0],[33.66,12.1,4.91],[28.09,7.94,0],
   [29.56,5.29,7.95],[33.66,12.1,4.91],[29.56,5.29,7.95],[30.63,12.15,12.86],
   [33.66,12.1,4.91],[29.56,5.29,7.95],[30.63,12.15,12.86],[23.18,8.03,12.86],
   [29.56,5.29,7.95],[23.18,8.03,12.86],[21.61,5.43,4.91],[29.56,5.29,7.95],
   [21.61,5.43,4.91],[28.09,7.94,0],[29.56,5.29,7.95],[21.61,5.43,4.91],
   [23.18,8.03,12.86],[17.77,12.39,7.95],[21.61,5.43,4.91],[17.77,12.39,7.95],
   [20.8,12.33,0],[21.61,5.43,4.91],[17.77,12.39,7.95], [23.18,8.03,12.86],
   [23.34,16.54,12.86],[17.77,12.39,7.95],[23.34,16.54,12.86],
   [21.87,19.2,4.91],[17.77,12.39,7.95],[21.87,19.2,4.91],[20.8,12.33,0],
   [17.77,12.39,7.95]   ])

ax.plot(B1[:, 0], B1[:, 1], B1[:, 2])
ax.plot(B2[:, 0], B2[:, 1], B2[:, 2])

T = np.zeros((57,3))

for i in range(21):
    plt.clf()
    ax = fig.add_subplot(111, projection='3d')    
    t = float(i/20);
    
    T[:, 0] = (1-t) * B1[:, 0] + t * B2[:, 0]  
    T[:, 1] = (1-t) * B1[:, 1] + t * B2[:, 1]
    T[:, 2] = (1-t) * B1[:, 2] + t * B2[:, 2]
    
    ax.plot(T[:, 0], T[:, 1], T[:, 2])
    plt.axis('off')
    plt.pause(0.5)


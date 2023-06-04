#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción: superficie por desplazamiento (Swapping)

Created on Tue Oct  4 12:20:20 2022
@author: computerappliedresearch
"""

import matplotlib.pyplot as plt
import numpy as np 

print("======= Curvas de Bezier =======")
print("======== SWAPPING =============")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.axis([0,25,-10,35])
t = np.arange(0,1.01,0.01)
U = np.ones((len(t),1), dtype=float)
B = np.zeros((len(t),3), dtype=float)
B1 = np.zeros((4,3), dtype=float)
M = np.array([ [-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]   ])
P = np.array([[3,7,4],[5,-6,8],[12,5,4],[4,2,9]] )

W = np.zeros((len(t),4), dtype=float)
W[:,0] = t*t*t
W[:,1] = t*t
W[:,2] = t[:]
W[:,3]= U[:,0]

plt.axis([-3,20,0,20])
print(P)
B1 = M@P
B = W@B1

for i in range(50):
    ax.plot( B[:,0]+(i/2),  B[:,1]+(i/3), B[:,2]+(i/3)   )
    plt.axis('off')
    plt.pause(0.5)
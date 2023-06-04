# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: 
De tercer orden curva de bezier
Created on Fri Sep  9 18:27:38 2022

@author: KerenMitsue
"""


import matplotlib.pyplot as plt
import numpy as np 

t = np.arange(0,1.01,0.01)
t2= t*t
t3 = t*t*t
U = np.ones((len(t),1), dtype=float)
B = np.zeros((len(t),2), dtype=float)
B1 = np.zeros((4,2), dtype=float)
M = np.array( [[-1,3,-3,1],[3,-6,3,0],[-3,3,0,0],[1,0,0,0]])
P = np.zeros((4,2), dtype = float)
W = np.zeros((len(t),4), dtype=float)

W[:,0] = t3[:]
W[:,1] = t2[:]
W[:,2] = t[:]
W[:,3] = U[:,0]

plt.plot()
plt.grid(True)
plt.axis([0,15,0,20])
P = np.array(plt.ginput(4,mouse_stop=4))
print(P)
B1= M@P
B = W@B1
plt.plot(B[:,0], B[:,1])
plt.show()

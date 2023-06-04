"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Curvas de Bézier
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: SeRealizar una curva de béxier a partir de puntos ingreesados
            por el usuario 
             
Created on Fri Sep  9 17:46:38 2022

@author: KerenMitsue
"""

import matplotlib.pyplot as plt
import numpy as np 

P = np.array([[4,0], [-5,2],[-2,8] ])

t = np.arange(0,1.01,0.01)
t2= t*t
U = np.ones((len(t),1), dtype=float)
B = np.zeros((len(t),2), dtype=float)
B1 = np.zeros((3,2), dtype=float)
M = np.array( [[1,-2,1],[-2,2,0],[1,0,0]])
P = np.zeros((3,2), dtype = float)
W = np.zeros((len(t),3), dtype=float)

W[:,0] = t2[:]
W[:,1] = t[:]
W[:,2] = U[:,0]

plt.plot()
plt.grid(True)
plt.axis([0,15,0,20])
P = np.array(plt.ginput(3,mouse_stop=3))
print(P)
B1= M@P
B = W@B1
plt.plot(B[:,0], B[:,1])
plt.show()


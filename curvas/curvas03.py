"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Curvas de Bézier
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Seleccionar cuatro puntos en el pano 2D y calcular 4 puntos 
             de la curva de bézier correspondiente. 
             
Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""

import matplotlib.pyplot as plt
import numpy as np 


#P = np.array([[1,0], [4,2],[6,4] ])
P = np.array([[4,0], [-5,2],[-2,8],[4,9] ])
plt.plot(P[:,0], P[:,1])

t = np.linspace(0,1,50)
#t = np.array([ 0,0.25,0.5 ,0.75,1 ])
T = np.zeros((50,2))
for i in range(0,t.size):
    T[i,0] = ((1-t[i])**3) *(P[0,0]) + 3*(1-t[i])**2*(t[i])*P[1,0] + 3*(1-t[i])*((t[i])**2)*P[2,0] + ((t[i])**3)*P[3,0]
    T[i,1] = ((1-t[i])**3) *(P[0,1]) + 3*(1-t[i])**2*(t[i])*P[1,1] + 3*(1-t[i])*((t[i])**2)*P[2,1] + ((t[i])**3)*P[3,1]
plt.scatter(T[:,0], T[:,1])
plt.plot(T[:,0], T[:,1])
plt.show()



"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Granficacion computacional
Tema: Rotación
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: Aplicar la rotación a una figura
@author: KerenMitsue
"""

import numpy as np
from numpy import pi, cos, sin
import matplotlib.pyplot as plt


P = np.array([ [2,3],[-4,7], [1,-5],[2,3] ], dtype=float)
gr = float(input("Ingresa el angulo de rotación: "))
th = gr*(pi/180)
R = np.array([[cos(th), sin(th)], [-sin(th), cos(th)] ])


T = P@R
plt.plot(P[:,0], P[:,1])
plt.plot(T[:,0], T[:,1])
plt.grid()


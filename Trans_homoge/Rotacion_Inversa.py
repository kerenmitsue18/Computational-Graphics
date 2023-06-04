"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema:Tranformaciones inversas
Alumno: Keren Mitsue Ramírez Vergara

Descripción: APlicar una rotación inversa a una figura 
previamente rotada. 

Created on Fri Aug 19 13:15:45 2022
@author: KerenMitsue
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi

P = np.array([ [2,3,1], [3,5,1], [4,4,1],[6,5,1],[7,4,1],[4,2,1],[2,3,1], [2,7,1]])

plt.figure()
plt.subplot(131)
plt.plot(P[0:-1,0], P[0:-1,1])
plt.axis("off")
plt.title("Org")


gr = 45
th = gr*(pi/180)
R = np.array([[cos(th),sin(th), 1], [-sin(th), cos(th), 1], [0,0,1]])
M = P@R
plt.subplot(132)
plt.plot(M[0:-1,0], M[0:-1,1])
plt.axis("off")
plt.title("Rotacion")



gr = 45
th = gr*(pi/180)
Ri= np.array([[cos(-th),sin(-th), 1], [-sin(-th), cos(-th), 1], [0,0,1]])
M = M@Ri
plt.subplot(133)
plt.axis("off")
plt.plot(M[0:-1,0], M[0:-1,1])
plt.title("Inversa")








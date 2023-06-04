# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Descripción: escalar un tetraedro

Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import pi, sin, cos, exp, linspace

sx = float(input("Dev el factor de escala en el eje x:"))
sy = float(input("Dev el factor de escala en el eje y:"))
sz = float(input("Dev el factor de escala en el eje z:"))

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
P = np.array([[0,0,4], [0,4,0], [4,0,0], [0,0,4], [0,0,0], [4,0,0], [0,0,0], [0,4,0]])
Rx = np.array([[sx,0,0], [0,sy,0], [0,0,sz]])
T = P@Rx

ax.plot(P[:, 0], P[:, 1], P[:, 2])
ax.plot(T[:, 0], T[:, 1], T[:, 2])

plt.show()


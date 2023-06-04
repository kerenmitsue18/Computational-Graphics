#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción: Realizar un Helicoide 

Created on Tue Oct  4 13:16:23 2022
@author: computerappliedresearch
"""

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
v = arange(-pi/2, pi/2, 0.1)
u = arange(0,2*pi,0.1)
R = 3
b = 0.5
U,V = meshgrid(u,v)

ax.plot_surface(R * V* cos(U), R * V* sin(U), b * U, rstride=1,
                cstride=1, cmap=cm.PuRd)
ax.axis('off')
ax.set_title("Helicoide")
plt.show()




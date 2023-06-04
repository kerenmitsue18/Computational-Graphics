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
ax.axis([-10,10,-10,10])
for i in range(20):
    ax.plot_surface(R * V* cos(U), R * V* sin(U*i),
                    b * U*1, rstride=1, cstride=1, cmap=cm.cool)
    plt.axis('off')
    plt.pause(0.1)
    plt.show()

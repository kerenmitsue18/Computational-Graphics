#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción:

Created on Tue Oct 18 13:53:02 2022
@author: computerappliedresearch
"""

from numpy import *
import matplotlib.pyplot as mp
from matplotlib import cm 

v = linspace(-2,2,100)
u = linspace(-2,2,100)

U,V = meshgrid(u,v)

X = U - (U**3) /3 + (U*V**2)
Y = V - (V**3 /3) + (V*U**2)
Z = U**2 - V**2

fig = mp.figure()

ax = fig.add_subplot(111,projection="3d")
ax.set_title("Superficie de Enneper")
ax.plot_surface(X,Y,Z, cmap =cm.summer)
ax.axis('off')
mp.show()

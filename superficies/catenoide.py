#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: superficies paramétricas
Alumno: Kere
Profesor: 
Descripción:

Created on Tue Oct 18 13:47:22 2022
@author: computerappliedresearch
"""

import numpy 
from numpy import *
import matplotlib.pyplot as mp
from matplotlib import cm 

v = linspace(0,(2*pi)+0.1,100)
u = linspace(-2,2+0.1,100)
U,V = meshgrid(u,v)
X = U
Y = cosh(U) * cos(V)
Z = cosh(U) * sin(V)

fig = mp.figure()

ax = fig.add_subplot(111,projection="3d")
ax.axis('off')
ax.set_title("Catenoide")
ax.plot_surface(X,Y,Z, cmap =cm.BuPu)
mp.show()

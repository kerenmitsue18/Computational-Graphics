#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción

Created on Tue Oct 18 13:30:52 2022
@author: computerappliedresearch
"""

import numpy 
from numpy import *
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm 

u = linspace(0,(2*pi)+0.1,100)
v = linspace(-1,1,100)
R =18
U,V = meshgrid(u,v)
X = (R- V*sin(U/2)*sin(U))
Y = (R- V*sin(U/2)*cos(U))
Z = V* cos(U/2)
fig = mp.figure()

ax = fig.add_subplot(111,projection="3d")
ax.plot_surface(X,Y,Z, cmap =cm.copper)
ax.axis("off")
mp.show()


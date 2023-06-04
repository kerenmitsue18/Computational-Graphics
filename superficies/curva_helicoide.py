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

from numpy import sin, cos, linspace, pi, meshgrid
import matplotlib.pyplot as plt
from matplotlib import cm 

u = linspace(0,2*pi,20)
v = linspace(0,pi,20)
R = 3
b = 0.5
v0 = pi/2
u0 = pi

U,V = meshgrid(u,v)

X = R * V* cos(U)
Y =  R * V* sin(U)
Z =  b * U

x = R* u* cos(u0)
y =  R * v* sin(u0)
z =  b * u0

x1 = R* v0 * cos(u)
y1 =  R * v0 * sin(u)
z1 =  b * u

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('Curva sobre helicoide')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#ax.plot3D(x,y,z,linewidth=4, color='black')
ax.plot3D(x1,y1,z1,linewidth=4, color='red')
ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=cm.cool)
plt.show()


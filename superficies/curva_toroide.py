#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción:

Created on Tue Oct  4 13:41:58 2022
@author: computerappliedresearch
"""


from numpy import linspace, meshgrid,cos, sin, pi
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
v = linspace(0,(2*pi)+0.1,100)
u = linspace(0,(2*pi)+0.1,100)
R = 15
r = 4
U,V = meshgrid(u,v)
X = (R+r*cos(U))*cos(V)
Y = (R+r*cos(U))*sin(V)
Z = R*sin(U)

v0 = pi/2
u0 = pi

x = (R+r*cos(u0))*cos(v)
y = (R+r*cos(u0))*sin(v)
z = R*sin(u0)

x1 = (R+r*cos(u))*cos(v0)
y1 = (R+r*cos(u))*sin(v0)
z1 = R*sin(u)

#ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=cm.cool)
ax.plot3D(x,y,z,linewidth=4, color='black')
ax.plot_wireframe(X,Y,Z)
ax.plot3D(x1,y1,z1,linewidth=4, color='red')
plt.show()
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: 

Created on Fri Oct  7 17:11:45 2022

@author: KerenMitsue
"""
from numpy import cos, sin, linspace, pi, meshgrid
import matplotlib.pyplot as plt

u = linspace(0,2*pi,20)
v = linspace(0,pi,20)
a = 3

U,V = meshgrid(u,v)
X = a*cos(U)*sin(V)
Y = a*sin(U)*sin(V)
Z = a*cos(V)
v0 = pi/2
u0 = pi

x = a*cos(u0)*sin(v)
y = a*sin(u0)*sin(v)
z = a*cos(v)

x1 = a*cos(u)*sin(v0)
y1 = a*sin(u)*sin(v0)
z1 = a*cos(v0)

fig = plt.figure(figsize=[6,6])
ax = fig.add_subplot(projection='3d')
ax.set_title('Esfera')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot3D(x,y,z,linewidth=4, color='black')
ax.plot3D(x1,y1,z1,linewidth=4, color='red')
ax.plot_wireframe(X,Y,Z)
plt.show()



# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: 

Created on Tue Oct 25 19:44:43 2022

@author: KerenMitsue
"""


from numpy import * 
import matplotlib.pyplot as plt
from matplotlib import cm

u = linspace(0,(2*pi)+0.1, 100)
v = linspace(-pi/2, pi/2,100)

U,V = meshgrid(u,v);

R = 4
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.axis([-4,8,-4,8])
X = R* cos(U) * cos(V)
Y = R* sin(U) * cos(V)
Z = R* sin(V)
ax.plot_surface(X,Y,Z, cmap=cm.spring)
ax.axis('off')
plt.pause(0.1)
plt.show()
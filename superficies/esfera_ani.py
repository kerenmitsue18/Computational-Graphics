# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Superficies
Alumno: Keren Mitsue Ramírez Vergara
Profesor: *
Descripción: Realizar una superficie parámetrica  
Created on Fri Sep 30 13:17:55 2022

@author: KerenMitsue
"""

from numpy import * 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm

u = linspace(0,(2*pi)+0.1, 100)
v = linspace(-pi/2, pi/2,100)

U,V = meshgrid(u,v);

R = 3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.axis([-4,8,-4,8])

for i in range(1,10): 
    X = R* cos(U) * cos(V)*(i/10)
    Y = R* sin(U) * cos(V)*(1/10)
    Z = R* sin(V)
    ax.plot_surface(X,Y,Z, cmap=cm.cool)
    plt.pause(0.1)
    plt.show()
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción:

Created on Tue Oct  4 13:50:39 2022
@author: computerappliedresearch
"""
from numpy import *
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
v = linspace(0,(2*pi)+0.1,100)
u = linspace(0,(2*pi)+0.1,100)
R = 15
r = 4
U,V = meshgrid(u,v)
plt.axis('off')
ax.axis([-20,20,-10,20])
for i in range(20):
    X = (R+r*cos(U*i/2))*cos(V)
    Y = (R+r*cos(U*i/5))*sin(V*i)
    Z = R*sin(U)
    ax.plot_surface(X,Y,Z, rstride=1, cstride=1, cmap=cm.cool)
    plt.show()
    plt.pause(0.01)
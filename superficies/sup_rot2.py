#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción: Superficie de Rotación de curva de Bézier
             de  segundo orden 

Created on Tue Oct  4 12:44:02 2022
@author: computerappliedresearch
"""
import numpy as np 
import matplotlib.pyplot as plt

print("======= Curvas de Bezier =======")
print("======== POR DESPLAZAMIENTO =============")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.axis([0,25,-10,35])
t = np.arange(0,1.01,0.01)
U = np.ones((len(t),1), dtype=float)
B = np.zeros((len(t),3), dtype=float)
B1 = np.zeros((3,3), dtype=float)
M = np.array([ [1,-2,1],[-2,2,0],[1,0,0]   ])
P = np.array([[2,5,3],[10,4,8],[9,1,11] ])

W = np.zeros((len(t),3), dtype=float)
W[:,0] = t*t
W[:,1] = t[:]
W[:,2] = U[:,0]

plt.axis([-10,15,-10,15])
print(P)
B1 = M@P
B = W@B1

for i in range(360):
    th = float((np.pi/180)*i)
    T = np.array([ [np.sin(th),np.cos(th),0],
                  [-np.sin(th),np.cos(th),0],[1,0,0]])
    B2 = B@T
    ax.plot( B2[:,0],B2[:,1], B2[:,2] )
    plt.axis('off')
    plt.pause(0.5)
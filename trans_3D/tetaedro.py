# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Descripción: Trasladar un tetaedro y rotarlo 45°

Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vertices of a pyramid
v = np.array([[-3, 1, 0,1],[2,1, 0,1],[-0.5, 5.33, 0,1],[-0.5, 2.44, 4.08,1],[-3, 1, 0,1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generate list of sides' polygons of our pyramid
verts = [ [v[0,0:-1],v[1,0:-1],v[4,0:-1]], [v[0,0:-1],v[3,0:-1],v[4,0:-1]],[v[1,0:-1],
         v[2,0:-1],v[3,0:-1]],[v[2,0:-1],v[1,0:-1],v[4,0:-1]],[v[2,0:-1],
         v[3,0:-1],v[4,0:-1]], [v[0,0:-1],v[1,0:-1],v[2,0:-1],v[3,0:-1]],
         [v[0,0:-1],v[1,0:-1],v[3,0:-1]]  ]

# plot sides
ax.add_collection3d(Poly3DCollection(verts, linewidths=1, edgecolors='b', alpha=1))

#Translacion en xy y Rotacion en eje x
h = 3
k = 2
l = 8
T = np.array([ [1,0,0,0],[0,1,0,0],[0,0,1,0],[h,k,l,1]])

gr = 45
th = gr * (np.pi/180)
Rox = np.array([[1,0,0,0],[0,np.cos(th),np.sin(th),0],[0,-np.sin(th),np.cos(th),0],[0,0,0,1]])


T = T@Rox
M = v@T

ax.scatter3D(M[:, 0], M[:, 1], M[:, 2])
verts = [ [M[0,0:-1],M[1,0:-1],M[4,0:-1]], [M[0,0:-1],M[3,0:-1],M[4,0:-1]], [M[1,0:-1],
    M[2,0:-1],M[3,0:-1]],[M[2,0:-1],M[1,0:-1],M[4,0:-1]],[M[2,0:-1],M[3,0:-1],
    M[4,0:-1]], [M[0,0:-1],M[1,0:-1],M[2,0:-1],M[3,0:-1]],[M[0,0:-1],M[1,0:-1],M[3,0:-1]]]
ax.add_collection3d(Poly3DCollection(verts, linewidths=1, edgecolors="#FF8000", alpha=1))
plt.show()
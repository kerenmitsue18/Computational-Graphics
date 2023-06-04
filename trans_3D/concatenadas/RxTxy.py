# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación cpmputacional
Tema: Concatenación de transformaciones 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: 
    Aplicar la concatenación de Rotacion en x,  
    Translación en ejes xy.

Created on Thu Sep  1 22:03:15 2022

@author: KerenMitsue
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

P = np.array([[0, 0, 4,1], [0, 4, 0,1], [4, 0, 0,1], [0, 0, 4,1], [0, 0, 0,1], [4, 0, 0,1], [0, 0, 0,1], [0, 4, 0,1]])
# generate list of sides' polygons of our pyramid
verts = [ [P[0,0:-1],P[1,0:-1],P[4,0:-1]], 
          [P[0,0:-1],P[3,0:-1],P[4,0:-1]],
          [P[1,0:-1],P[2,0:-1],P[3,0:-1]],
          [P[2,0:-1],P[3,0:-1],P[4,0:-1]],
          [P[0,0:-1],P[1,0:-1],P[3,0:-1]]  ]

#Matriz de Rotacion en x (Rox)
gr = 80
th = gr * (np.pi/180)
Rox = np.array([ [1,0,0,0],[0,np.cos(th),np.sin(th),0],[0,-np.sin(th),np.cos(th),0],[0,0,0,1]])

#Matriz de translacion (Txy)
h = 5
k = 2
l = 0
T = np.array([ [1,0,0,0],[0,1,0,0],[0,0,1,0],[h,k,l,1]])

M = Rox@T
M = P@M

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-5,6)
ax.set_ylim(-5,6)
ax.set_zlim(-5,6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#ax.axis("off")


#Color sides of figure original
cmap = mpl.cm.get_cmap('viridis')
for i in range(len(verts)): 
    c = cmap(mpl.colors.Normalize(0, 100)(i*20)) 
    coll = Poly3DCollection(verts[i],edgecolors='w')
    coll.set_facecolor(c) 
    coll.set_clim(vmin=0, vmax=100)
    ax.add_collection(coll)
plt.show()

verts = [ [M[0,0:-1],M[1,0:-1],M[4,0:-1]], 
          [M[0,0:-1],M[3,0:-1],M[4,0:-1]],
          [M[1,0:-1],M[2,0:-1],M[3,0:-1]],
          [M[2,0:-1],M[3,0:-1],M[4,0:-1]],
          [M[0,0:-1],M[1,0:-1],M[3,0:-1]]  ]

#Color sides of figure modified
cmap = mpl.cm.get_cmap('plasma')
for i in range(len(verts)): 
    c = cmap(mpl.colors.Normalize(0, 100)(i*20)) 
    coll = Poly3DCollection(verts[i],edgecolors='w')
    coll.set_facecolor(c) 
    coll.set_clim(vmin=0, vmax=100)
    ax.add_collection(coll)
plt.show()

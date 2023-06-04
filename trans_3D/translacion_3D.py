"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Translacion de una figura en 3D (prisma pentagonal)
Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import matplotlib as mpl

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Puntos de la figura
v = np.array([[-1, 6.13, 4.9,1],[-4,2, 0,1],[2, 2, 0,1],[3.85, 7.71, 0,1], 
              [-1, 11.23, 0,1],[-5.85, 7.71,0,1],[-1, 6.13, 4.9,1]])

ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

#Matriz de transformacion
h = 0
k = 0
l = 12
T = np.array([ [1,0,0,0],[0,1,0,0],[0,0,1,0],[h,k,l,1]])

M = v@T
# lista de lados del poligono
verts = [[v[0,0:-1],v[4,0:-1],v[5,0:-1]], [v[4,0:-1],v[5,0:-1],v[6,0:-1]],
         [v[0,0:-1],v[1,0:-1],v[2,0:-1]], [v[0,0:-1],v[2,0:-1],v[3,0:-1]],
         [v[0,0:-1],v[3,0:-1],v[4,0:-1]], [v[0,0:-1],v[1,0:-1],v[5,0:-1]],
         [v[1,0:-1],v[2,0:-1],v[3,0:-1],v[4,0:-1],v[5,0:-1]]  ]

#Color sides of figure original
cmap = mpl.cm.get_cmap('viridis')
for i in range(len(verts)): 
    c = cmap(mpl.colors.Normalize(0, 100)(i*10)) 
    coll = Poly3DCollection(verts[i],edgecolors='w')
    coll.set_facecolor(c) 
    coll.set_clim(vmin=0, vmax=100)
    ax.add_collection(coll)
plt.show()

ax.scatter3D(M[:, 0], M[:, 1], M[:, 2])
verts = [[M[0,0:-1],M[4,0:-1],M[5,0:-1]],[M[4,0:-1],M[5,0:-1],M[6,0:-1]],
         [M[0,0:-1],M[1,0:-1],M[2,0:-1]],[M[0,0:-1],M[2,0:-1],M[3,0:-1]],
         [M[0,0:-1],M[3,0:-1],M[4,0:-1]],[M[0,0:-1],M[1,0:-1],M[5,0:-1]],
         [M[1,0:-1],M[2,0:-1],M[3,0:-1],M[4,0:-1],M[5,0:-1]]]


cmap = mpl.cm.get_cmap('plasma')
for i in range(len(verts)): 
    c = cmap(mpl.colors.Normalize(0, 100)(i*10)) 
    coll = Poly3DCollection(verts[i],edgecolors='w')
    coll.set_facecolor(c) 
    coll.set_clim(vmin=0, vmax=100)
    ax.axis("off")
    ax.add_collection(coll)
    
plt.show()


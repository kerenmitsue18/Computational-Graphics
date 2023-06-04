"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Rotación de una figura en 3D
Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# vPuntos de la figura
v = np.array([[-1,6.13,4.9,1],[-4,2,0,1],[2,2,0,1],[3.85,7.71,0,1], 
              [-1, 11.23, 0,1],[-5.85, 7.71,0,1],[-1, 6.13, 4.9,1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

#Matriz de transformacion
gr = 45
th = gr * (np.pi/180)
Rox = np.array([[1,0,0,0],[0,np.cos(th),np.sin(th),0],[0,-np.sin(th),
                 np.cos(th),0],[0,0,0,1]])

Roy = np.array([[np.cos(th),0,-np.sin(th),0],[0,1,0,0],
                [np.sin(th),0,np.cos(th),0],[0,0,0,1]])

Roz = np.array([[np.cos(th),np.sin(th),0,0],[-np.sin(th),0,np.cos(th),0],
                [0,0,1,0],[0,0,0,1]])

# lista de lados del poligono
verts = [[v[0,0:-1],v[4,0:-1],v[5,0:-1]],[v[4,0:-1],v[5,0:-1],v[6,0:-1]],
     [v[0,0:-1],v[1,0:-1],v[2,0:-1]], [v[0,0:-1],v[2,0:-1],v[3,0:-1]],
     [v[0,0:-1],v[3,0:-1],v[4,0:-1]],[v[0,0:-1],v[1,0:-1],v[5,0:-1]], 
     [v[1,0:-1],v[2,0:-1],v[3,0:-1], v[4,0:-1],v[5,0:-1]]  ]

# plot sides
ax.add_collection3d(Poly3DCollection(verts,linewidths=1,edgecolors='b',
    alpha=1))


M = v@Roz
ax.scatter3D(M[:, 0], M[:, 1], M[:, 2])
verts = [[M[0,0:-1],M[4,0:-1],M[5,0:-1]],[M[4,0:-1],M[5,0:-1],M[6,0:-1]],
         [M[0,0:-1],M[1,0:-1],M[2,0:-1]],[M[0,0:-1],M[2,0:-1],M[3,0:-1]],
         [M[0,0:-1],M[3,0:-1],M[4,0:-1]],[M[0,0:-1],M[1,0:-1],M[5,0:-1]], 
         [M[1,0:-1],M[2,0:-1],M[3,0:-1],M[4,0:-1],M[5,0:-1]]  ]

ax.add_collection3d(Poly3DCollection(verts,linewidths=1,edgecolors="#FF8000", 
    alpha=1))

plt.show()


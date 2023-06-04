# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción:Usar la librería path de matplotlib para dibujar figuras
Created on Tue Aug 30 01:17:21 2022

@author: KerenMitsue
"""



import matplotlib.patches as mpatches
import matplotlib.path as mpath 
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
Path = mpath.Path
path_data = [(Path.MOVETO,(1.0,4.5)),(Path.CURVE3,(6.4,4.5)), 
             (Path.LINETO,(6.4,1.0)),(Path.CLOSEPOLY,(1.0,4.5))]

codes , verts = zip(*path_data)
path = mpath.Path(verts,codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)
x, y = zip(*path.vertices)
line, = ax.plot(x,y,'go-')
ax.grid()
ax.axis('equal')
plt.show()


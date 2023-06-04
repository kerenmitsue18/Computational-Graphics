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
import numpy as np

P = np.array([[0,0], [0,2], [1,0], [1.5,3], [4,4], [3,6], [0,5], [6,7], [1,8]])

fig, ax = plt.subplots()
Path = mpath.Path
'''
path_data = [(Path.MOVETO,(0,0)),(Path.MOVETO,(0,2)),  
             (Path.MOVETO,(1,0)),(Path.CLOSEPOLY,(0,0)),
             (Path.MOVETO,(0,2)),(Path.MOVETO,(1,0)), 
             (Path.MOVETO,(1.5,3)),(Path.CLOSEPOLY,(0,2)),
             (Path.MOVETO,(1,0)),(Path.MOVETO,(1.5,3)), 
             (Path.MOVETO,(4,4)),(Path.CLOSEPOLY,(1,0)),
             (Path.MOVETO,(4,4)),(Path.MOVETO,(3,6)), 
             (Path.MOVETO,(0,5)),(Path.CLOSEPOLY,(4,4)),
             (Path.MOVETO,(3,6)),(Path.MOVETO,(0,5)), 
             (Path.MOVETO,(6,7)),(Path.CLOSEPOLY,(3,6)),
             (Path.MOVETO,(0,5)),(Path.MOVETO,(6,7)), 
             (Path.MOVETO,(1,8)),(Path.CLOSEPOLY,(0,5)),
             (Path.MOVETO,(1.5,3)),(Path.MOVETO,(0,5)), 
             (Path.MOVETO,(0,2)),(Path.CLOSEPOLY,(1.5,3)),
             (Path.MOVETO,(0,5)),(Path.MOVETO,(3,6)), 
             (Path.MOVETO,(1,8)),(Path.CLOSEPOLY,(0,5)),
             (Path.MOVETO,(4,4)),(Path.MOVETO,(6,7)), 
             (Path.MOVETO,(3,6)),(Path.CLOSEPOLY,(4,4))] '''
path_data = []
for i in range(len(P)-2):
        path_data.append((Path.MOVETO,(P[i,0], P[i,1])))
        path_data.append((Path.MOVETO,(P[i+1,0], P[i+1,1])))
        path_data.append((Path.MOVETO,(P[i+2,0], P[i+2,1])))
        path_data.append((Path.CLOSEPOLY,(P[i,0], P[i,1])))




codes , verts = zip(*path_data)
path = mpath.Path(verts,codes)
patch = mpatches.PathPatch(path, facecolor='r', alpha=0.5)
ax.add_patch(patch)
x, y = zip(*path.vertices)
line, = ax.plot(x,y,'go-')
ax.grid()
ax.axis('equal')
plt.show()


# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Asignar color a cada cara de un tetaedro

Created on Wed Aug 31 23:27:58 2022

@author: KerenMitsue
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def patch(ax, x, y, z, v, vmin=0, vmax=100, cmap_name='plasma'):
    cmap = mpl.cm.get_cmap(cmap_name)
    c = cmap(mpl.colors.Normalize(vmin, vmax)(v))   # Normalize value and get color
    pc = Poly3DCollection([list(zip(x,y,z))])       # Create PolyCollection from coords
    pc.set_facecolor(c)                             # Set facecolor to mapped value
    pc.set_edgecolor('k')                           # Set edgecolor to black
    ax.add_collection3d(pc)                         # Add PolyCollection to axes
    return pc


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-4,6)
ax.set_ylim(-4,6)
ax.set_zlim(-4,6)
ax.axis("off")


P = np.array([[0,0,4],[0,4,0],[4,0,0],[0,0,4],[0,0,0],[4,0,0],[0,0,0],[0,4,0]])

patch(ax, P[0], P[1],P[2], 50)
patch(ax, P[2], P[3],P[4], 20)
patch(ax, P[5], P[6],P[7], 70)
patch(ax, P[6], P[7],P[0], 100)

plt.show()


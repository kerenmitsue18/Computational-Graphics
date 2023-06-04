#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: 
Profesor: 
Descripción:

Created on Tue Aug 30 12:59:49 2022
@author: computerappliedresearch
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PolyCollection
from numpy import pi, sin, cos, exp, linspace
import matplotlib.patches as mpatches
import matplotlib.path as mpath 


Path = mpath.Path
path_data = [(Path.MOVETO,(0, 0, 4)),(Path.LINETO,(0, 4, 0)),
             (Path.LINETO,(4, 0, 0)),(Path.CLOSEPOLY,(0, 0, 4))]

#Rotacion en eje x con translacion en xy
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
P = np.array([[0, 0, 4,1], [0, 4, 0,1], [4, 0, 0,1], [0, 0, 4,1], [0, 0, 0,1],
              [4, 0, 0,1], [0, 0, 0,1], [0, 4, 0,1]])

for i in range(280):
    Rox = np.array([ [1,0,0,0],[0,np.cos(0.1*np.pi*i),np.sin(0.1*np.pi*i),0],
                    [0,-np.sin(0.1*np.pi*i),np.cos(0.1*np.pi*i),0],[0,0,0,1]])
    T = P@Rox
    ax.plot(T[:, 0], T[:, 1], T[:, 2])
    #ax.add_collection3d(PolyCollection(P),zs=T[:, 2])
    ax.axis("off")
    plt.pause(0.5)


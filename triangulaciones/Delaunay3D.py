#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:52:09 2022

@author: proyecto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.spatial import Delaunay

p = np.array([[0,0],[0,1],[1,0],[1,1],[2,7],[3,6],[0,5],[1,7],[6,9],[1,8]])
P = np.array([[0,0,0],[0,1,5],[1,0,4],[1,1,7],[2,7,5],[3,6,4],[0,5,5],[1,7,6],[6,9,3],[1,8,6]])

tri  = Delaunay(P)
tri2 = Delaunay(p)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(P[:,0],P[:,1],P[:,2], triangles=tri.simplices, cmap=cm.Spectral)
#ax.plot_wireframe(P[:,0],P[:,1],P[:,2], linewidth=0, antialiased=False)

plt.triplot(p[:,0],p[:,1], tri2.simplices)
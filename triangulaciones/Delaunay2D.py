#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:43:54 2022

@author: proyecto
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.spatial import Delaunay

points = np.array([[0,0], [0,2], [1,0], [1.5,3], [4,4], [3,6], [0,5], [6,7], [1,8]])

tri = Delaunay(points)

plt.triplot(points[:,0],points[:,1], tri.simplices)
plt.plot(points[:,0],points[:,1], 'o')
plt.grid()

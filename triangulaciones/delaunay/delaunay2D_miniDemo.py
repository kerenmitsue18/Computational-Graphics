#!/usr/bin/env python3
"""
Minimal delaunay2D test
See: http://github.com/jmespadero/pyDelaunay2D
"""
import numpy as np
from delaunay2D import Delaunay2D

# Create a random set of 2D points
seeds = np.array([[0,0],[0,2],[1,0],[1.5,3],[4,4],[3,6],[0,5],[6,7],[1,8]])

# Create Delaunay Triangulation and insert points one by one
dt = Delaunay2D()
for s in seeds:
    dt.addPoint(s)

# Dump points and triangles to console
print("Input points:\n", seeds)
print ("Delaunay triangles:\n", dt.exportTriangles())


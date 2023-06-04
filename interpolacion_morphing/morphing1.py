#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:37:52 2022

@author: proyecto
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[0,0],[0,4],[1.5,5],[3,4],[3,0],[2,0],[2,1],[1,1],[1,0],[0,0]])
B = np.array([[8,2],[8,4],[6,4],[6,5],[8.5,5],[11,5],[11,4],[9,4],[9,2],[8,2]])


T = np.zeros((10,2))

plt.axis([-1,20,-1,20])

for i in range(11):
    plt.axis([0,12,0,12])
    
    t = float(i/10);
    
    T[:, 0] = (1-t) * A[:, 0] + t * B[:, 0]
    T[:, 1] = (1-t) * A[:, 1] + t * B[:, 1]
    
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(1)
    
    plt.clf()

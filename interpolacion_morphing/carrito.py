# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Interpolación
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción: Realizar una animación donde un carrito se mueva simular
            a la función seno.

Created on Sat Aug 27 20:39:40 2022

@author: KerenMitsue
"""

import matplotlib.pyplot as plt
import numpy as np 

P = np.array([[-20.  ,  -0.9 ],[-20.  ,  -0.55],[ -6.  ,  -0.55],[ -6.  ,  -0.8 ],
       [ -3.  ,  -0.8 ],[ -3.  ,  -0.6 ],[  2.  ,  -0.6 ], [  4.  ,  -0.65],
       [  4.  ,  -0.9 ],[  1.  ,  -0.9 ],[  1.  ,  -0.95], [  0.  ,  -1.  ],
       [ -1.  ,  -1.  ],[ -2.  ,  -0.95],[ -2.  ,  -0.9 ], [ -3.  ,  -0.9 ],
       [ -3.  ,  -0.85],[ -6.  ,  -0.85],[ -6.  ,  -0.9 ],
       [ -8.  ,  -0.9 ],[ -8.  ,  -0.95],[ -9.  ,  -1.  ],[-10.  ,  -1.  ],
       [-11.  ,  -0.95],[-11.  ,  -0.9 ],[-15.  ,  -0.9 ],
       [-15.  ,  -0.95],[-16.  ,  -1.  ],[-17.  ,  -1.  ],
       [-18.  ,  -0.95],[-18.  ,  -0.9 ],[-20.  ,  -0.9 ]])

T = np.zeros((32,2))
x = np.arange(0.0,4*np.pi,0.01)

for i in range(500):
    plt.clf()
    
    plt.axis([-20,100,-2,1.5])
    
    t = (i*np.pi)/180
    
    T[:, 0] = t*8 + P[:, 0] 
    T[:, 1] = P[:, 1] + np.sin(t)
    
    plt.plot(T[:,0], T[:,1])
    plt.axis('off')
    plt.pause(0.01)
    


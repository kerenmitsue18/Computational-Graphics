#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Translacion
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: Generar una animación de la translación de una figura
    Considere mostrar cada una de las translaciones.
"""

import numpy as np
import matplotlib.pyplot as plt
import time as tm


P = np.array([ [2,3],[-4,7], [1,-5],[2,3] ], dtype=float)
h = 0.5
k= -3
plt.axis([-5,12,-6,10]) #mantener ejes fijos

for i in range(1,10):
    plt.plot(P[:,0] + i*h, P[:,1])
    plt.axis('off')
    plt.pause(0.9)
    
tm.sleep(2)


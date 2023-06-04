#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Granficacion computacional
Tema: Refleccion 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: Aplicar la reflección a una figura en el eje x
@author: computerappliedresearch
"""

import numpy as np 
import matplotlib.pyplot as plt

P = np.array([[2,3], [-5,4],[7,-3], [2,3]])
Rx = np.array( [[1,0], [0,-1]] )
T = P@Rx #Producto entre matrices


fig = plt.figure()
ax = fig.add_subplot(1,2,1)
ax.plot(P[:,0], P[:,1])
ax.grid()
ax.set_title('Figura orginal')
ax1 = fig.add_subplot(1,2,2)
ax1.plot(T[:,0], T[:,1])
ax1.grid()
ax1.set_title('Reflexion en el eje x')



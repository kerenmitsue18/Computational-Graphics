#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Translacion
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vázquez
Descripción: Mostrar diferentes tipos de translacion
             (en eje x, en eje y, en ambos)
Created on Tue Aug  9 12:45:07 2022

@author: computerappliedresearch
"""

import numpy as np 
import matplotlib.pyplot as plt


P = np.array([[2,3], [-5,4],[7,-3], [2,3]])
h = 5
k = -10

figure, ax = plt.subplots()
ax.plot(P[:,0], P[:,1])
ax.plot(P[:,0]+h, P[:,1]+k)
ax.grid()
ax.set_title('Translacion')
plt.show()


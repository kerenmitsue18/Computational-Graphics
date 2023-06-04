# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional 
Tema: Tranformaciones Homogéneas
Alumno: Keren Mitsue Ramírez Vergara
Descripción:Graficar una curva en 3D

Created on Fri Sep  2 18:23:47 2022

@author: KerenMitsue
"""

import matplotlib.pyplot as plt 
from numpy import * 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
t = linspace(0,8*pi,100)
x = 2*cos(t)
y = 2*sin(t)
z = 5*exp(cos(t))
plt.plot(x,y,z)
plt.grid()
#plt.axis("off")
plt.show()




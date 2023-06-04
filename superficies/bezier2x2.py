# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: Superficies de Bézier por producto cartesiano

Created on Fri Oct  7 18:28:28 2022

@author: KerenMitsue
"""

from numpy import *
import matplotlib.pyplot as plt
from matplotlib import cm 


P = array([ [0,0,0],[1,0,1],[0,0,2],
            [1,1,0],[4,1,1],[1,1,2],
            [0,2,0],[1,2,1],[0,2,2]  ], dtype=float)


U = linspace(0,1,50)
W = linspace(0,1,50)

B0 = zeros((50,50), dtype = float)
B1 = zeros((50,50), dtype = float)
B2 = zeros((50,50), dtype = float)

u,w = meshgrid(U,W)

B0 = ((1-u)**2*(1-w)**2*P[0,0]) +( 2*w*(1-u)**2*(1-w)*P[1,0] ) + ((1-u)**2*(w**2)*P[2,0])  + (2*(1-u)*u*((1-w)**2)*P[3,0]+ 4*w*(1-u)*u*(1-w)*P[4,0] )  + ( 2*(1-u)*u*(w**2)*P[5,0] ) +( (u**2)*((1-w)**2)*P[6,0]) +2*(u**2)*w*(1-w)*P[7,0]  + ( (u**2)*(w**2)*P[8,0])
B1= ((1-u)**2*(1-w)**2*P[0,1])  +( 2*w*(1-u)**2*(1-w)*P[1,1] ) + ((1-u)**2*(w**2)*P[2,1])  + (2*(1-u)*u*((1-w)**2)*P[3,1]+ 4*w*(1-u)*u*(1-w)*P[4,1] )  + ( 2*(1-u)*u*(w**2)*P[5,1] ) +( (u**2)*((1-w)**2)*P[6,1]) +2*(u**2)*w*(1-w)*P[7,1]  + ( (u**2)*(w**2)*P[8,1])
B2= ((1-u)**2*(1-w)**2*P[0,2])  +( 2*w*(1-u)**2*(1-w)*P[1,2] ) + ((1-u)**2*(w**2)*P[2,2])  + (2*(1-u)*u*((1-w)**2)*P[3,2]+ 4*w*(1-u)*u*(1-w)*P[4,2] )  + ( 2*(1-u)*u*(w**2)*P[5,2] ) +( (u**2)*((1-w)**2)*P[6,2]) +2*(u**2)*w*(1-w)*P[7,2]  + ( (u**2)*(w**2)*P[8,2])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_title('Curva Bezier')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_surface(B0,B1,B2, cmap = cm.cool)
#ax.plot3D(P[:,0],P[:,1],P[:,2])
plt.show()
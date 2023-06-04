# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformadas Homogeneas
Alumno: Keren Mitsue Ramírez Vergara
Descripción: 
    Animaciòn de figura que rota 360º
    
Created on Thu Aug 18 21:32:48 2022

@author: KerenMitsue
"""

from Homogeneas import Homogeneas
import matplotlib.pyplot as plt
import numpy as np

homo = Homogeneas()
plt.figure()

P = np.array([ [2,3,1], [3,5,1], [4,4,1],[6,5,1],[7,4,1],[4,2,1],[2,3,1], [2,7,1]])


#original
plt.subplot(221)
plt.plot(P[0:-1,0], P[0:-1,1])
plt.title('Imagen original')

#TSR0
plt.subplot(222)
T = homo.translacion(P,2,3)
S = homo.escalamiento(T,2,3)
Ro = homo.rotacion(S,45)
plt.plot(Ro[0:-1,0], Ro[0:-1,1])
plt.title('RSR0')

#STR0
plt.subplot(223)
S = homo.escalamiento(P,2,3)
T = homo.translacion(S,2,3)
Ro = homo.rotacion(T,45)
plt.plot(Ro[0:-1,0], Ro[0:-1,1])
plt.title('STR0')


#R0ST
plt.subplot(224)
Ro = homo.rotacion(P,45)
S = homo.escalamiento(Ro,2,3)
T = homo.translacion(S,2,3)
plt.plot(T[0:-1,0], T[0:-1,1])
plt.title('R0ST')

plt.pause(4)

plt.clf()
#Girar una figura 360
for i in range(1,360):    
    #plt.clf()
    plt.axis("off")
    Ro = homo.rotacion(P,i)
    plt.plot(Ro[0:-1,0], Ro[0:-1,1])
    plt.title('Gira una figura a 360')
    plt.pause(0.01)



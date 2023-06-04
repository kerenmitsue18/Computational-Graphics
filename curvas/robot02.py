"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficaci{on computacional
Tema: Tranformaciones homógeneas
Alumno: Keren Mitsue Ramírez Vergara
Descripción: 
            Animación de brazo manipulador
Created on Sat Sep 10 18:04:49 2022

@author: KerenMitsue
"""

from matplotlib import pyplot as plt
import numpy as np 
B1 = np.array( [[0,0,1],[0, 0.28,1],[7, 0.28,1], [7,0,1], [0,0,1]])
B2 = np.array( [[7, 0,1],[7, 0.28,1], [11, 0.28,1], [11,0,1],[7, 0,1] ])
M = np.array([[11,-0.25,1],[12,-0.25,1],[12,0,1],[11.5,0,1],[11.5,0.25,1],[12,0.25,1],
              [12,0.5,1],[11,0.5,1],[ 11,-0.25,1]])

#Figura de robot 
fig = plt.figure()
ax = fig.add_subplot()

#Primer brazo
for i in range(20):
    plt.cla()
    ax.axis([-0.5,15,-0.5,15])
    th = 0.01*np.pi*i
    R = np.array([[np.cos(th),np.sin(th),0], [-np.sin(th), np.cos(th),0], [0,0,1]])
    T1 = B1@R
    T2 = B2@R
    M2 = M@R
    ax.plot(T1[:,0],T1[:,1], T2[:,0],T2[:,1],M2[:,0],M2[:,1] )
    plt.pause(0.2)
    
T2 = np.array([[-6.04838710e-03, -2.39026396e-03,1],[-1.49697581e-01,  2.27379459e-01,1],
       [ 3.13155242e+00,  2.46380476e+00,1],[ 3.27520161e+00,  2.24935302e+00,1],
       [-6.04838710e-03, -2.39026396e-03,1]])

T = np.array([ [1,0,0], [0,1,0], [-5.78956402, -3.93458364, 1]])
W = M2@T

#Segundo brazo 
for i in range(20):
    plt.cla()
    ax.axis([-0.5,15,-0.5,15])
    th = 0.01*np.pi*i
    T = np.array([ [1,0,0], [0,1,0], [5.78956402, 3.93458364, 1]])
    R = np.array([[np.cos(th),np.sin(th),0], [-np.sin(th), np.cos(th),0], [0,0,1]])
    X2 = T2@R@T
    M  = W@R@T
    ax.plot(T1[:,0],T1[:,1],X2[:,0],X2[:,1],M[:,0],M[:,1]  )
    plt.pause(0.1)


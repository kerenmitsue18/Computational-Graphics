# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformadas Homogeneas
Alumno: Keren Mitsue Ramírez Vergara
Descripción: 
    Clase que contiene las matrices de las transformaciones homogéneas
    
Created on Thu Aug 18 21:32:48 2022

@author: KerenMitsue
"""

import numpy as np 
from numpy import sin, cos, pi

class Homogeneas:
    
    def translacion(self,P,h,k):
        #Matriz de translacion 
        T = np.array([ [1,0,0], [0,1,0], [h,k,1]])
        return P@T
        
    def reflexion(self,P,t='x'):
        if t=='x':
            R = np.array([ [1,0,0], [0,-1,0], [0,0,1]])
        else: 
            R = np.array([ [-1,0,0], [0,1,0], [0,0,1]])
        return P@R
    
    def escalamiento(self, P,sx,sy):
        S = np.array([ [sx,0,0], [0,sy,0], [0,0,1]])
        if sx<0 or sy<0:
            print("La figura ha colapsado")
        return P@S
            
    def rotacion(self,P,gr):
        th = gr*(pi/180)
        R = np.array([[cos(th),sin(th), 1], [-sin(th), cos(th), 1], [0,0,1]])
        return P@R






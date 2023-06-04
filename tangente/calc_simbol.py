# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: 

Created on Fri Nov 11 18:35:37 2022

@author: KerenMitsue
"""


import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x= symbols("x")
f = symbols("f")
#funcion 
#f = 2*x**2
f = parse_expr( input("Escriba la funcion f: "))

#derivada y substitucion 
der = diff(f).subs(x,3)
print(der)

#sustituir la funcion 
m = f.subs(x,3)
print(m)

#Evaluar la funcion 
print(f.evalf( subs={x:3}))


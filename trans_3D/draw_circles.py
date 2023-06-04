"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficacion computacional
Tema: Transformaciones en 3D
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Manuel Almeida Vazquez
Descripción:Uso de a librería turtle
Created on Sat Aug 27 19:30:42 2022

@author: KerenMitsue
"""

import turtle as t 

t.speed(0)
t.bgcolor("blue")
t.pencolor("yellow")

for x in range(100):
    t.circle(x*2)
    t.right(91)
t.setpos(60,75) #desplazamiento del pencolor a coordenada (60,75)

for x in range(100):
    t.circle(x)
    t.right(91)
    
t.setpos(-60,-75)
for x in range(100):
     t.circle(x)
     t.right(91)   


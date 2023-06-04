# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: 

Created on Fri Nov 11 19:22:13 2022

@author: KerenMitsue
"""

import numpy as np
from sympy import symbols,diff
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x= symbols("x")
f = symbols("f")
f = parse_expr( input("Escriba la funcion f: "))
der = diff(f)
w = np.arange(0,2.01,0.1)

fig,ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

#Configuracion de slider
axslider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(axslider, 'Punto X1', 0, 2, valinit=0, 
                valstep=0.1,color='green')

#calcular la evaluacion en los puntos
yeval = []
for i in w:
    yeval.append(f.subs(x,i))

#configuracion de plot
ax.plot(w,yeval)
ax.axis([0,2.3,0,4])
ax.set_title("Recta tangente de la curva")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid()
l, = ax.plot(w,yeval)


def update(val):
    
    xp = slider.val
    tang =  der.subs(x,xp)  #pendiente
    yp = f.subs(x,xp) #Y coordenada
    tangente = tang*(w-xp) + yp
    l.set_ydata(tangente)
    fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()



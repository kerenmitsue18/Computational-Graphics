# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Graficación computacional
Tema: Recta tangente de una curva
Alumno: Keren Mitsue Ramírez Vergara
Profesor: 
Descripción: Graficar una recta tangente 

Created on Tue Nov  8 12:36:19 2022

@author: KerenMitsue
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig,ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

#Configuracion de slider
axslider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(axslider, 'Punto X1', 0, 2,valinit=0,
                valstep=0.1,color='green')
x = np.linspace(0,2,100)
y = x**2

#configuracion de plot
ax.plot(x,y)
ax.axis([0,2.3,0,4])
ax.set_title("Recta tangente de la curva y = x^2")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid()
l, = ax.plot(x,y)

def update(val):
    
    xp = slider.val
    m = 2*xp #pendiente
    yp = xp**2 #Y coordenada
    tangente = m*(x-xp) + yp #tangente
    l.set_ydata(tangente)
    fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()
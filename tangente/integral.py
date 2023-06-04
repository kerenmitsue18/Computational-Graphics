
import numpy as np
from sympy import symbols
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from matplotlib.widgets import Slider

def evalf(f,i):    
     return f.subs(x,i)

def coorY(f,i):
    #puntos correspondientes a funcion 
    yeval = []
    for i in w:
        yeval.append(f.subs(x,i))
    
    return np.array(yeval)  

def Riemann(f,w):
  A = 0                                 
  f1 = []
  f2 = []
  xbar = []
  ybar = []
  a = []

  for i in range (1, len(w)):
    #Suma de Riemman
    f1.append(evalf(f,w[i-1]))               
    f2.append(evalf(f,w[i]))                 
    fx = np.amin([evalf(f,w[i-1]), evalf(f,w[i])])
    deltax = w[i] - w[i-1]              
    a.append(fx*deltax)                 
    A += fx*deltax

    #Datos Grafico de Barras:
    xbar.append(w[i-1]) #Inferior izquierda
    ybar.append(0)
    xbar.append(w[i-1]) #Esquina superior izquierda
    ybar.append(fx)
    xbar.append(w[i]) #Esquina superior derecha
    ybar.append(fx)
    xbar.append(w[i]) #Esquina inferior derecha    
    ybar.append(0)

  return(A, xbar, ybar)

x= symbols("x")
f = symbols("f")

#Inputs del usuario
f = parse_expr( input("Funcion: "))
xi = int(input("Inicial: "))
xf = int(input("Final: "))

w = np.linspace(xi,xf,100)
#Configuracion de slider
fig,ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
axslider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(axslider, 'barras', 0, 100, valinit=0, valstep=1,color='green')

#Configuracion del plot
ax.plot(w, coorY(f,w), 'k', label=("f(x)"))
ax.axis([xi,xf,0,4])
ax.set_title("Sumas de Riemann ")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid()

l, = ax.plot(w,coorY(f,w))

def update(val):
    
    n = slider.val
    w = np.linspace(xi,xf,n)
    A, xbar, ybar = Riemann(f,w)
    l.set_xdata(xbar)
    l.set_ydata(ybar)
    print("Area ", A)
    fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()                      

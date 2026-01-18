from matplotlib.pyplot import *
import numpy as np 
from numba import njit
from PIL import Image
import os
from datetime import datetime
import matplotlib.image as mpimg
from matplotlib.colors import LinearSegmentedColormap
import random as rnd

x=np.linspace(-2,2,3000)
y=np.linspace(-2,2,3000)


#Definimos una función para interar
#f(z)=z**2+c
b=rnd.random()
c=rnd.random()
#Ahora definimos una función que realiza el proceso iterativo y cuenta cuantos pasos tarda la funcion en un punto en diverger (bueno, que sea mayor en modulo a 4 pero eso es practicamente infinito)
@njit
def julia(c):
    count = 0
    z=c
    for a in range(1000):
        p=(-1)**a
        if p==-1:    
            z = (z**2+c+b*1j)
        if p ==1:
            z=  z**2+b+c*1j
        count += 1
        if (abs(z) > 2):
            break
    return count

@njit(parallel=True)
def mandelbrot_set(x,y):
    m = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])  #Inicia en (0,0)
            count = julia(c)
            m[i,j]= count
    return m

#m se va a encargar de contar precisamente las interacciones de cada punto, que luego expresaremos mediante un mapa de calor

figure(figsize=(10,10), dpi=300)
m = mandelbrot_set(x,y)
title("Iteración compleja aleatoria: a= %.1f, b=%.1f"%(b,c))

# Color


colors = [
    (0.0, '#0a2f45'),
    (0.3, '#4d8aa8'),
    (0.6, "#a2d3ea"),
    (1.0, "#D4D2D2")
]
bluewhite = LinearSegmentedColormap.from_list("bluewhite", colors)


print("Coloreando...")
normed = np.log(m + 1) / np.max(np.log(m + 1))
colored = bluewhite(normed)


carpeta = r"G:\Mi unidad\Personal\imagenes"
# Guardar
if not os.path.exists(carpeta):
    os.makedirs(carpeta)

# ========== GENERAR NOMBRE ÚNICO ==========

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_name = f"julia_{timestamp}"
filename = os.path.join(carpeta, base_name + ".png")

# ========== GUARDAR IMAGEN ==========

print(f"Guardando en: {filename}")
mpimg.imsave(filename, colored)
print("✅ Imagen guardada con éxito.")
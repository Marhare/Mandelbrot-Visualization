from matplotlib.pyplot import *
import numpy as np 
from numba import njit
import matplotlib.image as mpimg
import os
from datetime import datetime

x = np.linspace(-2, 0.8, 100)
y = np.linspace(-1.5, 1.5, 100)

@njit
def mandelbrot(c):
    count = 0
    z = c
    for a in range(1000):
        z = z**2 + c
        count += 1
        if abs(z) > 3:
            break
    return count

@njit
def mandelbrot_set(x, y):
    m = np.zeros((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            c = complex(x[i], y[j])
            count = mandelbrot(c)
            m[i, j] = count
    return m

# Calcula el conjunto
m = mandelbrot_set(x, y)

# Normaliza y colorea (log para detalles)
from matplotlib.cm import get_cmap
normed = np.log(m.T + 1) / np.log(np.max(m)+1)
colored = get_cmap("turbo")(normed)[:, :, :3]  # RGB

# Guardado directo sin reescalado ni dpi
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"mandelbrot_{timestamp}.png"
mpimg.imsave(filename, colored)

print(f"✅ Imagen guardada: {filename}")

figure()
plot(x,y)
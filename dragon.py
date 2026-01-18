import numpy as np
import matplotlib.pyplot as plt
import random as rnd

z0=0+0j

x=[]
y=[]
a=rnd.randint(0,7)/10
b=rnd.randint(0,7)/10
c=a+b*1j
print(c)
z=z0
for i in range(100000):
    u=rnd.randint(0,1)
    if u == 1:
        z = 1+c*z
    if u == 0:
        z = 1-c*z
    x.append(np.real(z))
    y.append(np.imag(z))

plt.figure(figsize=(6,6))
plt.scatter(x, y, s=0.5, color="red")  # s = tamaño de punto
plt.axis('equal')
plt.axis('off')
plt.title("Iteración compleja aleatoria: a= %.1f, b=%.1f"%(a,b))
plt.show()
    
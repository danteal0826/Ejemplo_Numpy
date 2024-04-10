import numpy as np #importa la biblioteca numpy asigandole un alias llamado np
import matplotlib.pyplot as plt #importa la biblioteca matplotlib y el módulo pyplot con el alias plt
def mandelbrot(h, w, maxit=20, r=2):  #define una función con el nombre mandelbrot, la cual contiene 4 parametros. Dos parametors contienen un valor inicial (maxit=20, r=2) y los otros dos inician con cero por defecto.
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5, 1.5, 4*h+1) #Se coloca una varibale denotada con la letra 'x' a la cual se le asigna una funcion de numpy (linspace), la cual genera un arreglo desde un intervalo dado (-2.5, 1.5) y espaciado de forma equidistante
    y = np.linspace(-1.5, 1.5, 3*w+1) #Se coloca una varibale denotada con la letra 'y' a la cual se le asigna una funcion de numpy (linspace), la cual genera un arreglo desde un intervalo dado (-1.5, 1.5) y espaciado de forma equidistante
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime
plt.clf()
plt.imshow(mandelbrot(400, 400))
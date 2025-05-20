import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def grafico(func_str, x_min=8, x_max=14, step=0.0001):
    """
    Grafica cualquier función matemática recibida como cadena.

    Parámetros:
    - func_str: función como cadena, por ejemplo " -x**2 + 10*log(x**3) + 1"
    - x_min: límite inferior del eje x
    - x_max: límite superior del eje x
    - step: paso para el rango x
    """
    x = sp.symbols('x')
    f_sym = sp.sympify(func_str)
    
    x_vals = np.arange(x_min, x_max, step)
    f_lambd = sp.lambdify(x, f_sym, modules=["numpy"])
    y_vals = f_lambd(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, 'b*', linewidth=0.1)
    plt.title('Gráfico de la función')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

# Ejemplo de uso:
#grafico("-x**2 + 10*np.log(x**3) + 1", 8, 14, 0.0001)

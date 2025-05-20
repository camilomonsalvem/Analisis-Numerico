import numpy as np

fx = lambda x: x**3 + 4*x**2 - 10
a = 1
b = 4
tolera = 0.001
iteramax = 20

xi_1 = (a + b) / 2
xi = b
itera = 0
tramo = abs(xi - xi_1)

print('i |      x[i-1]     xi          x[i+1]       f[i-1]      fi        tramo')
while not (tramo < tolera or itera > iteramax):
    fi_1 = fx(xi_1)
    fi = fx(xi)
    
    denominador = fi_1 - fi
    if abs(denominador) < 1e-15:
        print("Denominador muy pequeño, posible división por cero. Deteniendo el método.")
        break
    
    xi1 = xi - fi * (xi_1 - xi) / denominador
    tramo = abs(xi1 - xi)
    
    print(f"{itera:2d} | {xi_1:12.6f} {xi:12.6f} {xi1:12.6f} {fi_1:12.6f} {fi:12.6f} {tramo:.6e}")
    
    xi_1 = xi
    xi = xi1
    itera += 1

print('Raíz aproximada:', xi)

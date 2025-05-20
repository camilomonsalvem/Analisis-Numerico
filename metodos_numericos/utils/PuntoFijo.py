import sympy as sp

def punto_fijo(x0, tol, niter, A, f_str=None, g_str=None):
    """
    Punto fijo para resolver f(x)=0 usando g(x).
    
    Parámetros:
    - x0: valor inicial
    - tol: tolerancia de error
    - niter: máximo número de iteraciones
    - A: parámetro numérico para la función
    - f_str: cadena con la función f(x), si None se usa la función default
    - g_str: cadena con la función g(x), si None se usa la función default
    
    Retorna:
    - n: número de iteraciones realizadas
    - xn: lista con los valores de x en cada iteración
    - fm: lista con valores de f(x) en cada iteración
    - E: lista con errores en cada iteración
    """

    x = sp.symbols('x')

    # Funciones por defecto (según tu código MATLAB)
    if f_str is None:
        f = ((A * (10**-2)) / 8) * sp.sin(x - A * (10**-3)) - x
    else:
        f = sp.sympify(f_str)

    if g_str is None:
        g = ((A * (10**-2)) / 8) * sp.sin(x - A * (10**-3)) - x + x  # según código MATLAB
    else:
        g = sp.sympify(g_str)

    c = 0
    fm = [float(f.subs(x, x0))]
    fe = fm[0]
    E = [tol + 1]
    error = E[0]
    xn = [x0]
    N = [c]

    while error > tol and fe != 0 and c < niter:
        x_new = float(g.subs(x, x0))
        xn.append(x_new)

        f_new = float(f.subs(x, x_new))
        fm.append(f_new)

        e_new = abs(x_new - x0)
        E.append(e_new)

        error = e_new
        x0 = x_new

        c += 1
        N.append(c)
        fe = f_new

    # Mostrar resultados estilo tabla
    print(f'      n                Xn                   Fx                   Error')
    for i in range(len(xn)):
        print(f'{N[i]:7d} {xn[i]:18.8f} {fm[i]:20.8f} {E[i]:15.8f}')

    if fe == 0:
        print(f'\n{xn[-1]} es raíz de f(x)')
    elif error < tol:
        print(f'\n{xn[-1]} es una aproximación de una raíz con tolerancia {tol}')
    else:
        print(f'\nFracasó en {niter} iteraciones')

    return c, xn, fm, E

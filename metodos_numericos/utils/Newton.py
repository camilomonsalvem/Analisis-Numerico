import sympy as sp

def newton(func_str, x0, tol, niter):
    x = sp.symbols('x')
    f = sp.sympify(func_str)
    df = sp.diff(f, x)

    fm = float(f.subs(x, x0))
    dfm = float(df.subs(x, x0))

    c = 0
    E = tol + 1
    iteraciones = []

    print('\n-----------------------------------------------------------')
    print("| Iter |     Xn     |    F(Xn)    |   F\'(Xn)   |    Error   |")
    print('-----------------------------------------------------------')

    while E > tol and abs(fm) > 1e-12 and c < niter:
        xn = x0 - fm / dfm
        fm = float(f.subs(x, xn))
        dfm = float(df.subs(x, xn))

        if c > 0:
            E = abs(xn - x0)
        else:
            E = tol + 1

        iteraciones.append((c, xn, fm, dfm, E))

        x0 = xn
        c += 1

    # Imprimir tabla
    for it in iteraciones:
        print(f'| {it[0]:4d} | {it[1]:10.6f} | {it[2]:10.6f} | {it[3]:10.6f} | {it[4]:10.6f} |')
    print('-----------------------------------------------------------')

    if abs(fm) < 1e-12:
        print(f'\n{xn} es raíz de f(x)')
    elif E < tol:
        print(f'\n{xn} es una aproximación de una raíz con tolerancia {tol}')
    elif dfm == 0:
        print(f'\n{xn} es una posible raíz múltiple de f(x)')
    else:
        print(f'\nFracasó en {niter} iteraciones')

    return c, xn, fm, dfm, E

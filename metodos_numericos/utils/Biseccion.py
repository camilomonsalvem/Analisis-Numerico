import sympy as sp

def biseccion(func_str, xi, xs, tol, niter):
    x = sp.symbols('x')
    f = sp.sympify(func_str)  # Convierte la cadena a expresión simbólica

    fi = float(f.subs(x, xi))
    fs = float(f.subs(x, xs))

    if fi == 0:
        s = xi
        E = [0]
        print(f'{xi} es raíz de f(x)')
        return s, E, [fi]
    elif fs == 0:
        s = xs
        E = [0]
        print(f'{xs} es raíz de f(x)')
        return s, E, [fs]
    elif fi * fs < 0:
        c = 0
        xm = (xi + xs) / 2
        fm = [float(f.subs(x, xm))]
        E = [tol + 1]
        error = E[0]

        print('-----------------------------------------------------------------')
        print('| Iter |    xi    |    xs    |    xm    |  f(xm)   |   Error    |')
        print('-----------------------------------------------------------------')

        while error > tol and fm[c] != 0 and c < niter:
            print(f'|  {c:3d} | {xi:8.5f} | {xs:8.5f} | {xm:8.5f} | {fm[c]:8.5f} | {error:10.5e} |')

            if fi * fm[c] < 0:
                xs = xm
                fs = float(f.subs(x, xs))
            else:
                xi = xm
                fi = float(f.subs(x, xi))

            xa = xm
            xm = (xi + xs) / 2
            fm.append(float(f.subs(x, xm)))
            E.append(abs(xm - xa))
            error = E[-1]
            c += 1

        print(f'|  {c:3d} | {xi:8.5f} | {xs:8.5f} | {xm:8.5f} | {fm[c]:8.5f} | {error:10.5e} |')
        print('-----------------------------------------------------------------')

        if fm[c] == 0:
            s = xm
            print(f'{xm} es raíz de f(x)')
        elif error < tol:
            s = xm
            print(f'{xm} es una aproximación de una raíz de f(x) con una tolerancia = {tol}')
        else:
            s = xm
            print(f'El método fracasó después de {niter} iteraciones')

        return s, E, fm
    else:
        print('El intervalo es inadecuado')
        return None, None, None

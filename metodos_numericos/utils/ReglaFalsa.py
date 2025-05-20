import sympy as sp

def regla_falsa(a, b, tol, niter, A):
    x = sp.symbols('x')
    f = sp.exp(-2*x + A) - x
    # f = -sp.log(x) - x + A  # Alternativa comentada según MATLAB

    fa = float(f.subs(x, a))
    fb = float(f.subs(x, b))

    if fa * fb > 0:
        raise ValueError("El intervalo [a, b] no encierra una raíz. Cambie el intervalo.")

    c = 0
    xn = [a]
    E = [tol + 1]
    fm = [fa]

    print('\n-----------------------------------------------------------')
    print('| Iter |      Xn      |     f(Xn)     |     Error      |')
    print('-----------------------------------------------------------')

    while E[-1] > tol and c < niter:
        x_new = (a * fb - b * fa) / (fb - fa)
        f_new = float(f.subs(x, x_new))

        xn.append(x_new)
        fm.append(f_new)
        E.append(abs(xn[-1] - xn[-2]))

        print(f'|  {c:3d}  |  {xn[-1]:10.6f}  |  {fm[-1]:10.6f}  |  {E[-1]:10.6f}  |')

        if fa * f_new < 0:
            b = x_new
            fb = f_new
        else:
            a = x_new
            fa = f_new

        c += 1

    print('-----------------------------------------------------------')

    if fm[-1] == 0:
        print(f'{xn[-1]} es una raíz exacta.')
    elif E[-1] < tol:
        print(f'{xn[-1]} es una aproximación de la raíz con tolerancia {tol}.')
    else:
        print(f'El método fracasó después de {niter} iteraciones.')

    return c, xn, fm, E

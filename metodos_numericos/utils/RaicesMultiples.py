import sympy as sp

def raices_multiples(func_str, x0, tol=1e-5, niter=100):
    """
    Método de raíces múltiples para encontrar raíces con multiplicidad.

    Parámetros:
    - func_str: función como cadena (ejemplo: "x**3 - 3*x + 2")
    - x0: valor inicial (float)
    - tol: tolerancia para la convergencia (float)
    - niter: máximo número de iteraciones (int)

    Retorna:
    - xn: raíz aproximada
    - iter: número de iteraciones realizadas
    - errores: lista de errores por iteración
    """
    x = sp.symbols('x')
    f = sp.sympify(func_str)
    df = sp.diff(f, x)
    ddf = sp.diff(df, x)

    xn = x0
    errores = []

    for i in range(niter):
        f_val = float(f.subs(x, xn))
        df_val = float(df.subs(x, xn))
        ddf_val = float(ddf.subs(x, xn))

        denominador = df_val**2 - f_val * ddf_val
        if abs(denominador) < 1e-15:
            print("Denominador cerca de cero, posible división por cero. Parando.")
            break

        xn1 = xn - (f_val * df_val) / denominador
        error = abs(xn1 - xn)
        errores.append(error)

        if error < tol:
            print(f"Convergió en {i+1} iteraciones con error {error}")
            return xn1, i+1, errores

        xn = xn1

    print("No convergió en el número máximo de iteraciones")
    return xn, niter, errores

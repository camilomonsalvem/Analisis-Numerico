import numpy as np

def sor(A, b, x0, w, tol, niter):
    """
    Método SOR (Successive Over-Relaxation) para resolver Ax = b.
    
    Parámetros:
    - A: matriz cuadrada (numpy array)
    - b: vector resultado (numpy array)
    - x0: vector inicial (numpy array)
    - w: factor de relajación (float)
    - tol: tolerancia para el error relativo (float)
    - niter: máximo número de iteraciones (int)
    
    Retorna:
    - X: vector solución (numpy array)
    - errores_relativos: lista con errores relativos (norma 2) por iteración
    - errores_inf: lista con errores en norma infinita por iteración
    """
    n = len(b)
    X = x0.copy()
    errores_relativos = []
    errores_inf = []
    iter = 0
    Err = np.inf

    print('==============================================')
    print('Método SOR (Successive Over-Relaxation)')
    print(f'w (factor de relajación): {w:.2f}')
    print(f'Tolerancia: {tol:.4f} (3 cifras significativas)')
    print(f'Iteración inicial: X0 = {x0}')
    print('==============================================\n')

    encabezado_vars = '  '.join([f'x{i+1:2d}' for i in range(n)])
    print(f'Iter     {encabezado_vars}     Error Rel.       Error Inf.')
    print('-----------------------------------------------------------------------------')

    while Err > tol and iter < niter:
        X_old = X.copy()
        for i in range(n):
            suma1 = np.dot(A[i, :i], X[:i])
            suma2 = np.dot(A[i, i+1:], X_old[i+1:])
            X[i] = (1 - w) * X_old[i] + (w / A[i, i]) * (b[i] - suma1 - suma2)

        iter += 1
        Err_vector = (X - X_old) / X
        Err = np.linalg.norm(Err_vector)
        Err_inf = np.linalg.norm(Err_vector, np.inf)
        errores_relativos.append(Err)
        errores_inf.append(Err_inf)

        valores_iter = '  '.join([f'{val:8.4f}' for val in X])
        print(f'{iter:4d}     {valores_iter}     {Err:12.6f}    {Err_inf:10.6f}')

    print(f'\nConvergencia alcanzada en {iter} iteraciones.\n')

    return X, errores_relativos, errores_inf

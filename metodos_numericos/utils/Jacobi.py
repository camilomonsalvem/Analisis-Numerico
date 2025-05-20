import numpy as np

def jacobi(A, b, x0, tol=1e-5, max_iter=100):
    """
    Método de Jacobi para resolver Ax = b
    
    Parámetros:
    - A: matriz cuadrada (numpy array)
    - b: vector resultado (numpy array)
    - x0: vector inicial (numpy array)
    - tol: tolerancia para el error
    - max_iter: número máximo de iteraciones
    
    Retorna:
    - x: solución aproximada (numpy array)
    - errores: lista con errores norma infinita por iteración
    """
    n = len(b)
    x = x0.astype(float)
    errores = []

    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x_new[i] = (b[i] - suma) / A[i, i]

        error = np.linalg.norm(x_new - x, np.inf)
        errores.append(error)
        x = x_new

        if error < tol:
            print(f'Convergió en {k+1} iteraciones con error {error}')
            break
    else:
        print(f'No convergió en {max_iter} iteraciones')

    return x, errores

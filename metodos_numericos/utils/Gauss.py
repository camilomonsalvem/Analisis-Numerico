import numpy as np

def gauss_piv(A, b, piv):
    """
    Resuelve el sistema Ax = b usando eliminación de Gauss con:
    piv = 0: sin pivoteo
    piv = 1: pivoteo parcial
    piv = 2: pivoteo total
    
    Retorna:
    x: solución del sistema
    mark: orden de columnas para pivoteo total (si piv=2), o lista identidad
    """
    A = A.astype(float)  # asegurar tipo float
    b = b.astype(float)
    n = A.shape[0]
    Ab = np.hstack((A, b.reshape(-1,1)))  # matriz aumentada
    mark = np.arange(n)  # seguimiento de columnas para pivoteo total

    for k in range(n-1):
        if piv == 1:
            Ab = pivpar(Ab, n, k)
        elif piv == 2:
            Ab, mark = pivtot(Ab, mark, n, k)
        # Eliminación hacia adelante
        for i in range(k+1, n):
            if Ab[k, k] == 0:
                raise ZeroDivisionError("División por cero durante eliminación.")
            M = Ab[i, k] / Ab[k, k]
            Ab[i, k:n+1] = Ab[i, k:n+1] - M * Ab[k, k:n+1]

    x = sustreg(Ab, n)

    # Si pivoteo total, reordenar solución según mark
    if piv == 2:
        x_reordenado = np.zeros_like(x)
        for i, col in enumerate(mark):
            x_reordenado[col] = x[i]
        return x_reordenado, mark
    else:
        return x, mark

def pivpar(Ab, n, k):
    mayor = abs(Ab[k, k])
    maxrow = k
    for s in range(k+1, n):
        if abs(Ab[s, k]) > mayor:
            mayor = abs(Ab[s, k])
            maxrow = s
    if mayor == 0:
        raise ValueError("El sistema no tiene solución única")
    if maxrow != k:
        Ab[[k, maxrow], :] = Ab[[maxrow, k], :]  # intercambio de filas
    return Ab

def pivtot(Ab, mark, n, k):
    mayor = 0
    maxrow = k
    maxcol = k
    for r in range(k, n):
        for s in range(k, n):
            if abs(Ab[r, s]) > mayor:
                mayor = abs(Ab[r, s])
                maxrow = r
                maxcol = s
    if mayor == 0:
        raise ValueError("El sistema no tiene solución única")
    if maxrow != k:
        Ab[[k, maxrow], :] = Ab[[maxrow, k], :]
    if maxcol != k:
        Ab[:, [k, maxcol]] = Ab[:, [maxcol, k]]
        mark[k], mark[maxcol] = mark[maxcol], mark[k]
    return Ab, mark

def sustreg(Ab, n):
    """
    Sustitución regresiva para matriz aumentada Ab (n x n+1)
    """
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if Ab[i, i] == 0:
            raise ValueError("División por cero en sustitución regresiva")
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]
    return x

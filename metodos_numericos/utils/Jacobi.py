import numpy as np

def jacobi(A, b, x0, tolerancia, max_iter):
    """
    Implementa el método de Jacobi para resolver sistemas de ecuaciones lineales.

    Args:
        A (np.ndarray): Matriz de coeficientes del sistema.
        b (np.ndarray): Vector de términos independientes.
        x0 (np.ndarray): Vector inicial de aproximaciones.
        tolerancia (float): Tolerancia para el criterio de convergencia.
        max_iter (int): Número máximo de iteraciones.

    Returns:
        dict: Diccionario con los resultados del método.
    """
    n = len(b)
    x_old = np.copy(x0)  # Vector inicial
    iteraciones_resultado = []
    
    # Verificar dimensiones de A, b y x0
    if A.shape[0] != n or A.shape[1] != n:
        raise ValueError("La matriz A debe ser cuadrada.")
    if len(b) != n or len(x0) != n:
        raise ValueError("Las dimensiones de b y x0 deben coincidir con A.")
    
    for k in range(max_iter):
        x_new = np.zeros_like(x_old)
        
        # Actualización de cada componente de x
        for i in range(n):
            suma = np.dot(A[i, :], x_old) - A[i, i] * x_old[i]  # Sumar los términos fuera de la diagonal
            x_new[i] = (b[i] - suma) / A[i, i]  # La fórmula del método de Jacobi
        
        # Calcular el error absoluto de cada componente δi = |x_i(k) - x_i(k+1)|
        delta = np.abs(x_new - x_old)
        
        # Error absoluto total
        error_absoluto = np.max(delta)
        
        # Calcular el error relativo
        error_relativo = np.max(np.abs(delta) / np.abs(x_old))
        
        # Guardar el progreso de las iteraciones
        iteracion_info = {
            'iteracion': k + 1,
            'x': x_new.copy(),
            'error_absoluto': error_absoluto,
            'error_relativo': error_relativo
        }
        iteraciones_resultado.append(iteracion_info)
        
        # Verificar si se cumple la tolerancia
        if error_absoluto < tolerancia:
            break
        
        # Actualizar el valor de x_old para la siguiente iteración
        x_old = np.copy(x_new)
    
    resultado = {
        'solucion': x_new,
        'iteraciones': iteraciones_resultado,
        'convergencia': error_absoluto < tolerancia
    }
    
    return resultado


# A = np.array([[45,13,-4,8],[-5,-28,4,-14],[9,15,63,-7],[2,3,-8,-42]], dtype=float)
# b = np.array([-25,82,75,-43], dtype=float)
# x0 = np.array([2,2,2,2], dtype=float)  # Vector inicial de aproximaciones
# tolerancia = 5e-3
# max_iter = 25

# resultado = jacobi(A, b, x0, tolerancia, max_iter)

# print("Solución:", resultado['solucion'])
# print("¿Convergió?:", resultado['convergencia'])
# print("Iteración 0: x =", x0)
# for it in resultado['iteraciones']:
#     print(f"Iteración {it['iteracion']}: x = {it['x']}, error absoluto = {it['error_absoluto']:.2e}")

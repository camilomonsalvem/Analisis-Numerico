import numpy as np
import sympy as sp

def gauss_seidel(A, b, x0, tolerancia, max_iter):
    """
    Implementa el método de Gauss-Seidel para resolver sistemas de ecuaciones lineales.

    Args:
        A (np.ndarray): Matriz de coeficientes del sistema.
        b (np.ndarray): Vector de términos independientes.
        x0 (np.ndarray): Vector inicial de aproximaciones.
        tolerancia (float): Tolerancia para el criterio de convergencia.
        iteraciones (int): Número máximo de iteraciones.

    Returns:
        dict: Diccionario con los resultados del método.
    """
    def es_diagonal_dominante(A):
        """
        Verifica si la matriz A es diagonalmente dominante.
        """
        n = A.shape[0]
        for i in range(n):
            suma = np.sum(np.abs(A[i, :])) - np.abs(A[i, i])
            if np.abs(A[i, i]) <= suma:
                return False
        return True
    
    n = len(b)
    x = np.copy(x0)
    iteraciones_resultado = []
    #verificar que la diagonal no sea cero
    for i in range(n):
        if A[i, i] == 0:
            raise ZeroDivisionError(f"Error: Elemento diagonal A[{i},{i}] es cero, no se puede dividir.")
    
        
    # Verificar si la matriz es diagonalmente dominante
    if not es_diagonal_dominante(A):
        print("Advertencia: La matriz A no es diagonalmente dominante. El método puede no converger.")


    #verficar que las matrices A y b tengan dimensiones compatibles
    if A.shape[0] != b.shape[0]:
        raise ValueError("Error: Las dimensiones de A y b no son compatibles.")
    elif A.shape[1] != n:
        raise ValueError("Error: La matriz A debe ser cuadrada (n x n).")
    elif len(x0) != n:
        raise ValueError("Error: El vector inicial x0 debe tener la misma dimensión que b.")
    
  # Inicializar vector inicial si x0 no se proporciona
    if x0 is None:
        x = np.zeros_like(b, dtype=np.float64)
    else:
        x = np.copy(x0)
    

    for k in range(max_iter):
        x_old = np.copy(x)

        for i in range(n):
            suma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - suma) / A[i, i]

        error = np.linalg.norm(x - x_old, ord=np.inf)

        iteracion_info = {
            'iteracion': k + 1,
            'x': x.copy(),
            'error': error
        }
        iteraciones_resultado.append(iteracion_info)

        if error < tolerancia:
            break
     
    resultado = {
        'solucion': x,
        'iteraciones': iteraciones_resultado,
        'convergencia': error < tolerancia
    }
    return resultado

# def main():
#     # Definir la matriz A y el vector b y x0    
#     A = np.array([[45,13,-4,8],[-5,-28,4,-14],[9,15,63,-7],[2,3,-8,-42]], dtype=float)
#     b = np.array([-25,82,75,-43], dtype=float)
#     x0 = np.array([2,2,2,2], dtype=float)  # Vector inicial de aproximaciones
#     tolerancia = 5e-3
#     iteraciones = 100

#     resultado = gauss_seidel(A, b, x0, tolerancia, iteraciones)
#     print("Resultados del método de Gauss-Seidel:")
#     print ("Solución final:", resultado['solucion'])
#     print("¿Convergió?:", resultado['convergencia'])
    

# if __name__ == "__main__":  
#     main()

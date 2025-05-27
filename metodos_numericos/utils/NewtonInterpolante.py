import numpy as np
import sympy as sp

def newton_interpolante(puntos_x, puntos_y):
    """
    Implementa el método de interpolación de Newton usando diferencias divididas.
    
    Args:
        puntos_x (list): Lista de valores x de los puntos conocidos.
        puntos_y (list): Lista de valores y de los puntos conocidos.
        
    Returns:
        dict: Diccionario con los resultados del método.
    """
    
    # Validaciones iniciales
    if len(puntos_x) != len(puntos_y):
        return {
            "error": "Los vectores x e y deben tener la misma longitud",
            "success": False
        }
    
    if len(puntos_x) < 2:
        return {
            "error": "Se necesitan al menos 2 puntos para interpolar",
            "success": False
        }
    
    # Verificar que no hay valores x duplicados
    if len(set(puntos_x)) != len(puntos_x):
        return {
            "error": "Los valores de x no pueden repetirse",
            "success": False
        }
    
    n = len(puntos_x)
    
    # Crear tabla de diferencias divididas
    tabla_diferencias = np.zeros((n, n))
    
    # Primera columna son los valores y
    for i in range(n):
        tabla_diferencias[i][0] = puntos_y[i]
    
    # Calcular diferencias divididas
    for j in range(1, n):
        for i in range(n - j):
            tabla_diferencias[i][j] = (tabla_diferencias[i+1][j-1] - tabla_diferencias[i][j-1]) / (puntos_x[i+j] - puntos_x[i])
    
    # Construir el polinomio de Newton
    x = sp.symbols('x')
    polinomio = tabla_diferencias[0][0]  # Primer término (constante)
    
    # Agregar términos del polinomio
    producto = 1
    for i in range(1, n):
        producto *= (x - puntos_x[i-1])
        polinomio += tabla_diferencias[0][i] * producto
    
    # Expandir y simplificar el polinomio
    polinomio_expandido = sp.expand(polinomio)
    
    # Convertir a función evaluable
    polinomio_func = sp.lambdify(x, polinomio_expandido, 'numpy')
    
    # Crear tabla de diferencias para mostrar
    tabla_mostrar = []
    for i in range(n):
        fila = {
            'i': i,
            'xi': puntos_x[i],
            'yi': puntos_y[i],
            'diferencias': []
        }
        for j in range(n - i):
            if not np.isnan(tabla_diferencias[i][j]):
                fila['diferencias'].append(round(tabla_diferencias[i][j], 8))
        tabla_mostrar.append(fila)
    
    resultado = {
        'polinomio': str(polinomio_expandido),
        'polinomio_func': polinomio_func,
        'tabla_diferencias': tabla_mostrar,
        'coeficientes': [tabla_diferencias[0][i] for i in range(n)],
        'puntos_x': puntos_x,
        'puntos_y': puntos_y,
        'grado': n - 1,
        'success': True
    }
    
    return resultado
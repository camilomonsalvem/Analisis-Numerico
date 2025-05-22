import numpy as np
import sympy as sp

def biseccion(funcion_str, a, b, tolerancia, max_iteraciones):
    """
    Implementa el método de bisección para encontrar raíces de ecuaciones no lineales.
    
    Args:
        funcion_str (str): Expresión de la función como string.
        a (float): Límite inferior del intervalo inicial.
        b (float): Límite superior del intervalo inicial.
        tolerancia (float): Tolerancia para el criterio de parada.
        max_iteraciones (int): Número máximo de iteraciones.
        
    Returns:
        dict: Diccionario con los resultados del método.
    """
    # Convertir la función string a una función evaluable
    x = sp.symbols("x")
    funcion_expr = sp.sympify(funcion_str)
    f = sp.lambdify(x, funcion_expr)
    
    # Verificar que f(a) * f(b) < 0
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        return {
            "error": "El intervalo [a, b] no cumple con el teorema de Bolzano (f(a) * f(b) < 0)",
            "success": False
        }
    
    # Inicializar variables
    iteraciones = []
    error = float('inf')
    
    # Variables para el método
    a_n = a
    b_n = b
    c = None
    
    for i in range(max_iteraciones):
        # Guardar el valor de c anterior para calcular el error
        c_anterior = c
        
        # Calcular el punto medio
        c = (a_n + b_n) / 2
        fc = f(c)
        
        # Calcular error (absoluto)
        if c_anterior is not None:
            error = abs(c - c_anterior)
        
        # Guardar información de la iteración como diccionario (no como tupla)
        iteracion = {
            'iteracion': i + 1,
            'a': a_n,
            'b': b_n,
            'c': c,
            'fc': fc,
            'error': error if c_anterior is not None else None
        }
        
        iteraciones.append(iteracion)
        
        # Verificar si hemos encontrado la raíz
        if abs(fc) < 1e-10:  # consideramos f(c) = 0
            break
            
        # Verificar si se ha alcanzado la tolerancia
        if error < tolerancia and i > 0:
            break
            
        # Actualizar el intervalo para la siguiente iteración
        if fa * fc < 0:
            b_n = c
            fb = fc
        else:
            a_n = c
            fa = fc
    
    # Preparar resultados
    resultado = {
        'raiz': c,
        'error': error,
        'iteraciones': iteraciones,
        'convergencia': error < tolerancia,
        'funcion': funcion_str,
        'valor_funcion': fc,
        'num_iteraciones': len(iteraciones),
        'success': True
    }
    
    return resultado
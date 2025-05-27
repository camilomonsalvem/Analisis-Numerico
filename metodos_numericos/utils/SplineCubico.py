import numpy as np
import sympy as sp

def spline_cubico(puntos_x, puntos_y, tipo_frontera='natural'):
    """
    Implementa el método de interpolación por spline cúbico.
    
    Args:
        puntos_x (list): Lista de valores x de los puntos conocidos.
        puntos_y (list): Lista de valores y de los puntos conocidos.
        tipo_frontera (str): Tipo de condiciones de frontera ('natural' o 'sujeto').
        
    Returns:
        dict: Diccionario con los resultados del método.
    """
    
    # Validaciones iniciales
    if len(puntos_x) != len(puntos_y):
        return {
            "error": "Los vectores x e y deben tener la misma longitud",
            "success": False
        }
    
    if len(puntos_x) < 3:
        return {
            "error": "Se necesitan al menos 3 puntos para spline cúbico",
            "success": False
        }
    
    # Verificar que no hay valores x duplicados
    if len(set(puntos_x)) != len(puntos_x):
        return {
            "error": "Los valores de x no pueden repetirse",
            "success": False
        }
    
    # Ordenar puntos por x
    puntos_ordenados = sorted(zip(puntos_x, puntos_y))
    puntos_x_ord = [p[0] for p in puntos_ordenados]
    puntos_y_ord = [p[1] for p in puntos_ordenados]
    
    n = len(puntos_x_ord)
    h = [puntos_x_ord[i+1] - puntos_x_ord[i] for i in range(n-1)]
    
    # Construir sistema de ecuaciones para encontrar las segundas derivadas
    A = np.zeros((n, n))
    b = np.zeros(n)
    
    # Condiciones de frontera (spline natural: S''(x0) = S''(xn) = 0)
    if tipo_frontera == 'natural':
        A[0, 0] = 1
        A[n-1, n-1] = 1
        b[0] = 0
        b[n-1] = 0
    
    # Ecuaciones internas
    for i in range(1, n-1):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        b[i] = 6 * ((puntos_y_ord[i+1] - puntos_y_ord[i]) / h[i] - 
                    (puntos_y_ord[i] - puntos_y_ord[i-1]) / h[i-1])
    
    # Resolver sistema para obtener las segundas derivadas
    try:
        M = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return {
            "error": "Error al resolver el sistema de ecuaciones",
            "success": False
        }
    
    # Construir los polinomios cúbicos para cada segmento
    segmentos = []
    x = sp.symbols('x')
    
    for i in range(n - 1):
        x0, x1 = puntos_x_ord[i], puntos_x_ord[i + 1]
        y0, y1 = puntos_y_ord[i], puntos_y_ord[i + 1]
        M0, M1 = M[i], M[i + 1]
        hi = h[i]
        
        # Coeficientes del polinomio cúbico
        a = (M1 - M0) / (6 * hi)
        b_coef = M0 / 2
        c = (y1 - y0) / hi - hi * (2 * M0 + M1) / 6
        d = y0
        
        # Polinomio: S(x) = a(x-x0)³ + b(x-x0)² + c(x-x0) + d
        polinomio = a * (x - x0)**3 + b_coef * (x - x0)**2 + c * (x - x0) + d
        polinomio_expandido = sp.expand(polinomio)
        
        # Función evaluable
        func = sp.lambdify(x, polinomio_expandido, 'numpy')
        
        segmento = {
            'intervalo': f"[{x0}, {x1}]",
            'x0': x0,
            'x1': x1,
            'y0': y0,
            'y1': y1,
            'coeficientes': {'a': a, 'b': b_coef, 'c': c, 'd': d},
            'segunda_derivada': {'M0': M0, 'M1': M1},
            'ecuacion': str(polinomio_expandido),
            'funcion': func
        }
        
        segmentos.append(segmento)
    
    # Función de evaluación completa
    def evaluar_spline(x_val):
        """Evalúa el spline cúbico en un punto dado"""
        for segmento in segmentos:
            if segmento['x0'] <= x_val <= segmento['x1']:
                return segmento['funcion'](x_val)
        
        # Si está fuera del rango, usar extrapolación
        if x_val < puntos_x_ord[0]:
            return segmentos[0]['funcion'](x_val)
        else:
            return segmentos[-1]['funcion'](x_val)
    
    resultado = {
        'segmentos': segmentos,
        'puntos_x': puntos_x_ord,
        'puntos_y': puntos_y_ord,
        'segundas_derivadas': M.tolist(),
        'num_segmentos': len(segmentos),
        'tipo_frontera': tipo_frontera,
        'funcion_evaluacion': evaluar_spline,
        'matriz_sistema': A.tolist(),
        'vector_sistema': b.tolist(),
        'success': True
    }
    
    return resultado
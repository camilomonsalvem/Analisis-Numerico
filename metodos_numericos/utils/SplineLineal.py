import numpy as np
import sympy as sp

def spline_lineal(puntos_x, puntos_y):
    """
    Implementa el método de interpolación por spline lineal.
    
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
    
    # Ordenar puntos por x
    puntos_ordenados = sorted(zip(puntos_x, puntos_y))
    puntos_x_ord = [p[0] for p in puntos_ordenados]
    puntos_y_ord = [p[1] for p in puntos_ordenados]
    
    n = len(puntos_x_ord)
    
    # Crear los segmentos de spline lineal
    segmentos = []
    x = sp.symbols('x')
    
    for i in range(n - 1):
        x0, y0 = puntos_x_ord[i], puntos_y_ord[i]
        x1, y1 = puntos_x_ord[i + 1], puntos_y_ord[i + 1]
        
        # Calcular pendiente
        m = (y1 - y0) / (x1 - x0)
        
        # Ecuación de la recta: y = y0 + m(x - x0)
        ecuacion = y0 + m * (x - x0)
        ecuacion_simplificada = sp.expand(ecuacion)
        
        # Función evaluable
        func = sp.lambdify(x, ecuacion_simplificada, 'numpy')
        
        segmento = {
            'intervalo': f"[{x0}, {x1}]",
            'x0': x0,
            'x1': x1,
            'y0': y0,
            'y1': y1,
            'pendiente': m,
            'ecuacion': str(ecuacion_simplificada),
            'funcion': func
        }
        
        segmentos.append(segmento)
    
    # Función de evaluación completa
    def evaluar_spline(x_val):
        """Evalúa el spline en un punto dado"""
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
        'num_segmentos': len(segmentos),
        'funcion_evaluacion': evaluar_spline,
        'success': True
    }
    
    return resultado
import numpy as np
import sympy as sp

def punto_fijo(function_f_str, function_g_str, x0, tolerancia, max_iteraciones):
    """
    Implementa el método de punto fijo para encontrar raíces de f(x)=0 reformulando como x = g(x).

    Args:
        function_f_str (str): Cadena con la función f(x), por ejemplo "x**3 - x - 1"
        function_g_str (str): Cadena con la función g(x) para iterar, por ejemplo "(x + 1)**(1/3)"
        x0 (float): Valor inicial para la iteración
        tolerancia (float): Tolerancia para el criterio de parada basado en error
        max_iteraciones (int): Número máximo de iteraciones permitidas

    Returns:
        dict: Diccionario con resultados:
            - 'resultado_principal': aproximación final de la raíz
            - 'error': error final calculado
            - 'iteraciones': lista con detalles de cada iteración
            - 'convergencia': booleano indicando si convergió
            - 'num_iteraciones': número de iteraciones realizadas
            - 'success': True si el método fue exitoso, False si hubo error
            - 'message': mensaje descriptivo de la ejecución
    """

    # 1. Validaciones iniciales
    if tolerancia <= 0:
        return {"error": "La tolerancia debe ser un número positivo.", "success": False}

    if max_iteraciones <= 0:
        return {"error": "El número máximo de iteraciones debe ser positivo.", "success": False}

    # Inicializar símbolos y funciones
    x = sp.symbols('x')

    try:
        f_expr = sp.sympify(function_f_str)
        g_expr = sp.sympify(function_g_str)
    except Exception as e:
        return {"error": f"Error al interpretar las funciones: {str(e)}", "success": False}

    # Convertir a funciones numéricas para evaluación rápida
    f_num = sp.lambdify(x, f_expr, "numpy")
    g_num = sp.lambdify(x, g_expr, "numpy")

    # 2. Inicializar variables
    iteraciones = []
    error = float('inf')
    x_actual = x0

    # 3. Bucle principal del método
    for i in range(max_iteraciones):
        try:
            x_siguiente = g_num(x_actual)
            f_val = f_num(x_siguiente)
        except Exception as e:
            return {
                "error": f"Error numérico en iteración {i+1}: {str(e)}",
                "success": False,
            }

        # Calcular error absoluto entre iteraciones
        error = abs(x_siguiente - x_actual)

        # Guardar detalles de la iteración
        iteracion_info = {
            "iteracion": i + 1,
            "valor_actual": x_siguiente,
            "f_evaluado": f_val,
            "error": error,
        }
        iteraciones.append(iteracion_info)

        # Verificar criterio de parada
        if error < tolerancia or f_val == 0:
            message = (
                f"Convergió a raíz aproximada {x_siguiente} "
                f"con error {error} en {i+1} iteraciones."
            )
            return {
                "resultado_principal": x_siguiente,
                "error": error,
                "iteraciones": iteraciones,
                "convergencia": True,
                "num_iteraciones": i + 1,
                "success": True,
                "message": message,
            }

        # Preparar para siguiente iteración
        x_actual = x_siguiente

    # 4. Preparar resultados si no converge en máximo iteraciones
    return {
        "resultado_principal": x_actual,
        "error": error,
        "iteraciones": iteraciones,
        "convergencia": False,
        "num_iteraciones": max_iteraciones,
        "success": True,
        "message": f"No se alcanzó convergencia en {max_iteraciones} iteraciones.",
    }

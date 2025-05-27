import math

def secante_metodo(x0, x1, tolerance, max_iterations, function_f):
    """
    Implementa el método de la secante para encontrar raíces de una función no lineal.

    Args:
        x0 (float): Primer valor inicial para el método.
        x1 (float): Segundo valor inicial para el método.
        tolerance (float): Tolerancia para el criterio de parada.
        max_iterations (int): Número máximo de iteraciones permitidas.
        function_f (str): Función en formato string, que usa la variable 'x'.

    Returns:
        dict: Diccionario con los resultados del método, incluyendo iteraciones y estado.
    """

    # 1. Validaciones iniciales
    if tolerance <= 0:
        return {
            "error": "La tolerancia debe ser un número positivo",
            "success": False
        }
    if max_iterations <= 0:
        return {
            "error": "El máximo número de iteraciones debe ser un entero positivo",
            "success": False
        }

    # Evaluar función en puntos iniciales para verificar dominio y evitar errores
    try:
        x = x0
        f_x0 = eval(function_f)
        x = x1
        f_x1 = eval(function_f)
    except Exception as e:
        return {
            "error": f"Error al evaluar la función en los puntos iniciales: {str(e)}",
            "success": False
        }

    # Si f(x0) y f(x1) son iguales, división por cero en fórmula del método
    if f_x0 == f_x1:
        return {
            "error": "División por cero: f(x0) y f(x1) son iguales",
            "success": False
        }

    # 2. Inicializar variables
    iteraciones = []
    error = float('inf')
    iteracion_actual = 0
    x_prev = x0
    x_curr = x1

    # 3. Bucle principal del método
    while iteracion_actual < max_iterations and error > tolerance:
        iteracion_actual += 1

        # Evaluar función en puntos actuales
        x = x_prev
        f_prev = eval(function_f)
        x = x_curr
        f_curr = eval(function_f)

        # Calcular nuevo punto según fórmula del método de la secante
        try:
            x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
        except ZeroDivisionError:
            return {
                "error": "División por cero en la fórmula del método durante la iteración",
                "success": False
            }

        # Evaluar función en nuevo punto
        x = x_new
        f_new = eval(function_f)

        # Calcular error absoluto como diferencia entre iteraciones consecutivas
        error = abs(x_new - x_curr)

        # Guardar información de la iteración actual
        iteracion = {
            'iteracion': iteracion_actual,
            'x_prev': x_prev,
            'x_curr': x_curr,
            'f_x_prev': f_prev,
            'f_x_curr': f_curr,
            'x_new': x_new,
            'f_x_new': f_new,
            'error': error
        }
        iteraciones.append(iteracion)

        # Actualizar variables para siguiente iteración
        x_prev = x_curr
        x_curr = x_new

        # Si función evaluada es cero, raíz exacta encontrada
        if f_new == 0:
            break

    # 4. Preparar resultados finales
    resultado = {
        'resultado_principal': x_curr,
        'error': error,
        'iteraciones': iteraciones,
        'convergencia': error <= tolerance,
        'num_iteraciones': iteracion_actual,
        'success': error <= tolerance
    }

    return resultado

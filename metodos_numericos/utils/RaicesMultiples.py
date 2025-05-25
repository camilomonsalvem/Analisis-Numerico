import numpy as np
import sympy as sp

def raices_multiples(funcion, x0, tolerancia, max_iteraciones, multiplicidad):
    """
    Implementa el método de raíces múltiples para encontrar una raíz de una función que se repite (tiene multiplicidad > 1).

    Args:
        funcion (str): Función en forma de cadena, por ejemplo "x**3 - 3*x + 1".
        x0 (float): Valor inicial desde el cual comenzar las iteraciones.
        tolerancia (float): Criterio de parada basado en el error (absoluto).
        max_iteraciones (int): Límite máximo de iteraciones permitidas.
        multiplicidad (int): Multiplicidad conocida de la raíz buscada.

    Returns:
        dict: Diccionario con:
            - resultado_principal: Última aproximación obtenida.
            - error: Error final calculado.
            - iteraciones: Lista de diccionarios con el detalle por iteración.
            - convergencia: True si el método alcanzó la tolerancia.
            - num_iteraciones: Cantidad de iteraciones realizadas.
            - success: True si el método se ejecutó correctamente.
            - error: (opcional) Mensaje de error si algo falló.
    """

    # Definimos la variable simbólica
    x = sp.symbols("x")

    # 1. Validaciones iniciales
    try:
        # Intentamos convertir la función a una expresión simbólica
        f_expr = sp.sympify(funcion)
        # Derivada simbólica de la función
        f_prime_expr = sp.diff(f_expr, x)
    except Exception as e:
        # Error al interpretar la función
        return {
            "error": f"Error al interpretar la función: {str(e)}",
            "success": False
        }

    # Verificamos que la tolerancia sea un número positivo
    if not isinstance(tolerancia, (int, float)) or tolerancia <= 0:
        return {
            "error": "La tolerancia debe ser un número positivo",
            "success": False
        }

    # Verificamos que el número máximo de iteraciones sea un entero positivo
    if not isinstance(max_iteraciones, int) or max_iteraciones <= 0:
        return {
            "error": "El número máximo de iteraciones debe ser un entero positivo",
            "success": False
        }

    # 2. Inicializar variables

    # Se crean funciones evaluables numéricamente a partir de las expresiones simbólicas
    f = sp.lambdify(x, f_expr, modules=["math"])
    f_prime = sp.lambdify(x, f_prime_expr, modules=["math"])

    iteraciones = []              # Lista donde se almacenarán los resultados de cada iteración
    error = float('inf')          # Error inicial (infinito)
    x_actual = x0                 # Primer valor inicial para empezar el método

    # 3. Bucle principal del método
    for i in range(max_iteraciones):
        try:
            # Evaluamos la función y su derivada en el valor actual
            fx = f(x_actual)
            fpx = f_prime(x_actual)

            # Si la derivada es cero, no se puede continuar
            if fpx == 0:
                return {
                    "error": f"La derivada es cero en x = {x_actual}. No se puede continuar.",
                    "success": False
                }

            # Fórmula del método de raíces múltiples
            x_siguiente = x_actual - multiplicidad * (fx / fpx)

            # Calculamos el error absoluto
            error = abs(x_siguiente - x_actual)

            # Guardamos la información de la iteración actual
            iteracion = {
                'iteracion': i + 1,
                'valor': x_actual,
                'f_x': fx,
                'f_prime_x': fpx,
                'x_siguiente': x_siguiente,
                'error': error
            }   

            iteraciones.append(iteracion)

            # Si el error es menor que la tolerancia, se detiene el ciclo
            if error < tolerancia:
                break

            # Preparamos el siguiente ciclo
            x_actual = x_siguiente

        except Exception as e:
            # Error durante evaluación de función
            return {
                "error": f"Error durante la evaluación: {str(e)}",
                "success": False
            }

    # 4. Preparar resultados finales
    resultado = {
        'resultado_principal': x_actual,               # Última aproximación encontrada
        'error': error,                                # Error de la última iteración
        'iteraciones': iteraciones,                    # Historial de iteraciones
        'convergencia': error < tolerancia,            # Si se logró converger
        'num_iteraciones': len(iteraciones),           # Total de iteraciones realizadas
        'success': True                                # Indica que el método se ejecutó correctamente
    }

    return resultado

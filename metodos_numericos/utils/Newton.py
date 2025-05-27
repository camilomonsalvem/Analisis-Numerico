import sympy as sp

def newton_metodo(funcion_str, x0, tolerancia, max_iteraciones):
    """
    Implementa el método de Newton para encontrar raíces de una función no lineal.

    Args:
        funcion_str (str): Función en formato string, usando variable 'x'.
        x0 (float): Valor inicial para el método.
        tolerancia (float): Tolerancia para el criterio de parada.
        max_iteraciones (int): Número máximo de iteraciones.

    Returns:
        dict: Diccionario con resultados, incluyendo lista de iteraciones, error, convergencia, etc.
    """

    # 1. Validaciones iniciales para asegurar que los parámetros de tolerancia y iteraciones son correctos
    if tolerancia <= 0:
        return {
            "error": "La tolerancia debe ser un número positivo",
            "success": False
        }
    if max_iteraciones <= 0:
        return {
            "error": "El máximo número de iteraciones debe ser un entero positivo",
            "success": False
        }

    # 2. Preparar la función simbólica y su derivada usando sympy
    x = sp.symbols('x')
    try:
        f_expr = sp.sympify(funcion_str)   # Convertir el string a expresión simbólica
        df_expr = sp.diff(f_expr, x)       # Calcular derivada simbólica de f
    except Exception as e:
        return {
            "error": f"Error al interpretar la función: {str(e)}",
            "success": False
        }

    # 3. Convertir las expresiones simbólicas a funciones numéricas evaluables rápidamente
    f_num = sp.lambdify(x, f_expr)
    df_num = sp.lambdify(x, df_expr)

    # 4. Inicializar lista para almacenar detalles de cada iteración y variable para error inicial
    iteraciones = []
    error = float('inf')  # Empezamos con error infinito para forzar la primera iteración
    valor_actual = x0     # El punto inicial dado por el usuario

    # 5. Bucle principal que ejecuta el método hasta que se cumpla criterio de parada o se agoten iteraciones
    for i in range(max_iteraciones):
        try:
            # Evaluar función y derivada en el punto actual
            f_val = f_num(valor_actual)
            df_val = df_num(valor_actual)

            # Comprobar que la derivada no sea cero para evitar división por cero
            if df_val == 0:
                return {
                    "error": "Derivada cero, no se puede continuar.",
                    "success": False
                }

            # Aplicar fórmula de Newton para calcular el nuevo valor aproximado de la raíz
            valor_nuevo = valor_actual - f_val / df_val
        except Exception as e:
            # Captura errores durante el cálculo (evaluación o división)
            return {
                "error": f"Error durante cálculo en iteración {i+1}: {str(e)}",
                "success": False
            }

        # Calcular el error como diferencia absoluta entre iteraciones consecutivas (excepto la primera)
        if i == 0:
            error = float('inf')
        else:
            error = abs(valor_nuevo - valor_actual)

        # Guardar los datos de la iteración actual en un diccionario
        iteracion = {
            "iteracion": i + 1,
            "valor_actual": valor_actual,
            "f_evaluado": f_val,
            "df_evaluado": df_val,
            "valor_nuevo": valor_nuevo,
            "error": error,
        }
        iteraciones.append(iteracion)

        # Si el error es menor que la tolerancia, se detiene el proceso (criterio de paro)
        if error < tolerancia:
            break

        # Actualizar el valor actual para la siguiente iteración
        valor_actual = valor_nuevo

    # 6. Preparar el resultado final con todos los datos importantes para retornar
    resultado = {
        "resultado_principal": valor_nuevo,       # Mejor aproximación a la raíz
        "error": error,                           # Error de la última iteración
        "iteraciones": iteraciones,               # Lista con los detalles de cada iteración
        "convergencia": error < tolerancia,       # Indicador booleano si se alcanzó tolerancia
        "num_iteraciones": len(iteraciones),      # Número total de iteraciones realizadas
        "success": True                           # Indica que el método terminó correctamente
    }

    return resultado

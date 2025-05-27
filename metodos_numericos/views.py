import ast
from django.shortcuts import render
import numpy as np
<<<<<<< HEAD
from .utils import biseccion, generar_grafica, regla_falsa, punto_fijo, raices_multiples, secante_metodo, newton_metodo
from metodos_numericos.utils.sor_metodo import sor_metodo
from metodos_numericos.utils.Grafico import generar_grafica, plot_matrix_solution, plot_system_equations
from metodos_numericos.utils.Jacobi import jacobi
from metodos_numericos.utils.Vandermonde import vandermonde
from metodos_numericos.utils.Lagrange import lagrange
from metodos_numericos.utils.Gaussseidel import gauss_seidel
=======
from .utils import biseccion, generar_grafica, regla_falsa
from .utils.Gaussseidel import gauss_seidel
import ast
from .utils.Jacobi import jacobi
>>>>>>> 8645180 (Jacobi completo)

def index(request):
    """Vista de la página principal."""
    return render(request, 'home/index.html')

def capitulo1(request):
    """Vista del capítulo 1."""
    return render(request, 'capitulo1/index.html')

def capitulo2(request):
    """Vista del capítulo 2."""
    return render(request, 'capitulo2/index.html')

def capitulo3(request):
    """Vista del capítulo 3."""
    return render(request, 'capitulo3/index.html')

def biseccion_view(request):
    """Vista del método de bisección."""
    context = {
        'title': 'Método de Bisección'
    }
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            funcion = request.POST.get('funcion')
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))
            
            # Ejecutar método de bisección
            resultado = biseccion(funcion, a, b, tolerancia, max_iter)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido en el método de bisección')
                return render(request, 'capitulo1/biseccion.html', context)
            
            # Generar gráfica
            grafica = generar_grafica(funcion, a, b, resultado['raiz'], "Método de Bisección")
            
            # Agregar resultados al contexto
            context['resultado'] = resultado
            context['grafica'] = grafica
            
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo1/biseccion.html', context)

def regla_falsa_view(request):
    """Vista del método de regla falsa."""
    context = {
        'title': 'Método de Regla Falsa'
    }
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            funcion = request.POST.get('funcion')
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))
            
            # Ejecutar método de regla falsa
            resultado = regla_falsa(funcion, a, b, tolerancia, max_iter)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido en el método de regla falsa')
                return render(request, 'capitulo1/regla_falsa.html', context)
            
            # Generar gráfica
            grafica = generar_grafica(funcion, a, b, resultado['raiz'], "Método de Regla Falsa")
            
            # Agregar resultados al contexto
            context['resultado'] = resultado
            context['grafica'] = grafica
            
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo1/regla_falsa.html', context)


def punto_fijo_view(request):
    """
    Vista para el método de Punto Fijo.
    """

    context = {
        'title': 'Método de Punto Fijo'
    }

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            function_f = request.POST.get('function_f')
            function_g = request.POST.get('function_g')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))

            # Ejecutar el método
            resultado = punto_fijo(function_f, function_g, x0, tolerancia, max_iter)

            # Revisar si hubo error
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo1/punto_fijo.html', context)

            # Agregar resultados al contexto
            context['resultado'] = resultado

            # Generar gráfica (definimos intervalo pequeño alrededor de x0)
            a = x0 - 2
            b = x0 + 2
            grafica = generar_grafica(function_f, a, b, resultado['resultado_principal'], metodo="Método de Punto Fijo")
            context['grafica'] = grafica

        except Exception as e:
            context['error'] = f"Error: {str(e)}"

    return render(request, 'capitulo1/punto_fijo.html', context)


def raices_multiples_view(request):
    """
    Vista para el método de Raíces Múltiples.
    """

    context = {
        'title': 'Método de Raíces Múltiples'
    }

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            function_f = request.POST.get('function_f')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))
            multiplicidad = int(request.POST.get('multiplicidad'))

            # Ejecutar el método
            resultado = raices_multiples(function_f, x0, tolerancia, max_iter, multiplicidad)

            # Revisar si hubo error
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo1/raices_multiples.html', context)

            # Agregar resultados al contexto
            context['resultado'] = resultado

            # Generar gráfica (intervalo centrado en x0)
            a = x0 - 2
            b = x0 + 2
            grafica = generar_grafica(function_f, a, b, resultado['resultado_principal'], metodo="Método de Raíces Múltiples")
            context['grafica'] = grafica

        except Exception as e:
            context['error'] = f"Error: {str(e)}"

    return render(request, 'capitulo1/raices_multiples.html', context)


def secante_metodo_view(request):
    """
    Vista para el método de la secante.
    """

    context = {
        'title': 'Método de la Secante'
    }

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            function_f = request.POST.get('function_f')
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))

            # Ejecutar el método de la secante
            resultado = secante_metodo(x0, x1, tolerancia, max_iter, function_f)

            # Revisar si hubo error
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo1/secante_metodo.html', context)

            # Agregar resultados al contexto
            context['resultado'] = resultado

            # Generar gráfica (usar x0, x1 para intervalo)
            a, b = sorted([x0, x1])
            grafica = generar_grafica(function_f, a, b, resultado['resultado_principal'], metodo="Método de la Secante")
            context['grafica'] = grafica

        except Exception as e:
            context['error'] = f"Error: {str(e)}"

    return render(request, 'capitulo1/secante_metodo.html', context)

def newton_metodo_view(request):
    """
    Vista para el método de Newton.
    """
    context = {
        'title': 'Método de Newton',
    }

    if request.method == 'POST':
        try:
            funcion_str = request.POST.get('function_f')
            x0 = float(request.POST.get('x0'))
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))

            # Ejecutar método de Newton
            resultado = newton_metodo(funcion_str, x0, tolerancia, max_iter)

            # Verificar si hubo error
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo1/newton_method.html', context)

            # Generar gráfica con intervalo alrededor del valor inicial y raíz estimada
            a = x0 - 5
            b = x0 + 5
            grafica = generar_grafica(funcion_str, a, b, raiz=resultado['resultado_principal'], metodo='Método de Newton')

            context['resultado'] = resultado
            context['grafica'] = grafica

        except Exception as e:
            context['error'] = f"Error: {str(e)}"

    return render(request, 'capitulo1/newton_metodo.html', context)


def sor_metodo_view(request):
    context = {
        'title': 'Método SOR',
    }

    if request.method == 'POST':
        try:
            matrix_a_raw = request.POST.get('matrix_a', '').strip()
            vector_b_raw = request.POST.get('vector_b', '').strip()
            initial_x_raw = request.POST.get('initial_x', '').strip()
            relaxation_factor_raw = request.POST.get('relaxation_factor', '').strip()
            tolerance_raw = request.POST.get('tolerance', '').strip()
            max_iter_raw = request.POST.get('max_iter', '').strip()

            relaxation_factor = float(relaxation_factor_raw) if relaxation_factor_raw else 1.25
            tolerance = float(tolerance_raw) if tolerance_raw else 0.0001
            max_iter = int(max_iter_raw) if max_iter_raw else 100

            solver = sor_metodo()

            # Usar validate_input para transformar y validar las entradas
            validated = solver.validate_input(
                matrix_a_raw=matrix_a_raw,
                vector_b_raw=vector_b_raw,
                initial_guess_raw=initial_x_raw,
                tolerance=tolerance,
                max_iterations=max_iter,
                relaxation_factor=relaxation_factor,
                matrix_size=len(matrix_a_raw.split(';')),
            )

            if isinstance(validated, str):  # Si es error, es string con mensaje
                context['error'] = validated
                return render(request, 'capitulo2/sor_metodo.html', context)

            # validated es [A, b, x0]
            A, b, x0 = validated

            # Ahora sí llamar a solve con matrices listas
            resultado = solver.solve(
                A=A,
                b=b,
                x0=x0,
                tolerance=tolerance,
                max_iterations=max_iter,
                relaxation_factor=relaxation_factor,
                precision_type=1,
            )

            context['resultado'] = resultado

        except Exception as e:
            context['error'] = f"Error: {str(e)}"

    return render(request, 'capitulo2/sor_metodo.html', context)

def newton_interpolante_view(request):
    """Vista para el método de Newton Interpolante."""
    context = {
        'title': 'Newton Interpolante'
    }
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            puntos_x_str = request.POST.get('puntos_x', '').strip()
            puntos_y_str = request.POST.get('puntos_y', '').strip()
            puntos_evaluar_str = request.POST.get('puntos_evaluar', '').strip()
            
            # Procesar puntos X e Y
            puntos_x = [float(x.strip()) for x in puntos_x_str.split(',') if x.strip()]
            puntos_y = [float(y.strip()) for y in puntos_y_str.split(',') if y.strip()]
            
            # Validar límite de puntos
            if len(puntos_x) > 8:
                context['error'] = "Se admiten máximo 8 puntos."
                return render(request, 'capitulo3/newton_interpolante.html', context)
            
            # Ejecutar método
            from metodos_numericos.utils.NewtonInterpolante import newton_interpolante
            resultado = newton_interpolante(puntos_x, puntos_y)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo3/newton_interpolante.html', context)
            
            # Evaluar puntos específicos si se proporcionaron
            puntos_evaluados = []
            if puntos_evaluar_str:
                puntos_evaluar = [float(x.strip()) for x in puntos_evaluar_str.split(',') if x.strip()]
                for x_val in puntos_evaluar:
                    y_val = resultado['polinomio_func'](x_val)
                    puntos_evaluados.append({'x': x_val, 'y': y_val})
            
            # Generar gráfica
            from metodos_numericos.utils.Grafico import generar_grafica_interpolacion
            grafica = generar_grafica_interpolacion(resultado, "Newton Interpolante", puntos_evaluados)
            
            context['resultado'] = resultado
            context['puntos_evaluados'] = puntos_evaluados
            context['grafica'] = grafica
            
        except ValueError as e:
            context['error'] = "Error en el formato de los datos. Verifique que todos los valores sean numéricos."
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo3/newton_interpolante.html', context)


def spline_lineal_view(request):
    """Vista para el método de Spline Lineal."""
    context = {
        'title': 'Spline Lineal'
    }
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            puntos_x_str = request.POST.get('puntos_x', '').strip()
            puntos_y_str = request.POST.get('puntos_y', '').strip()
            puntos_evaluar_str = request.POST.get('puntos_evaluar', '').strip()
            
            # Procesar puntos X e Y
            puntos_x = [float(x.strip()) for x in puntos_x_str.split(',') if x.strip()]
            puntos_y = [float(y.strip()) for y in puntos_y_str.split(',') if y.strip()]
            
            # Validar límite de puntos
            if len(puntos_x) > 8:
                context['error'] = "Se admiten máximo 8 puntos."
                return render(request, 'capitulo3/spline_lineal.html', context)
            
            # Ejecutar método
            from metodos_numericos.utils.SplineLineal import spline_lineal
            resultado = spline_lineal(puntos_x, puntos_y)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo3/spline_lineal.html', context)
            
            # Evaluar puntos específicos si se proporcionaron
            puntos_evaluados = []
            if puntos_evaluar_str:
                puntos_evaluar = [float(x.strip()) for x in puntos_evaluar_str.split(',') if x.strip()]
                for x_val in puntos_evaluar:
                    y_val = resultado['funcion_evaluacion'](x_val)
                    puntos_evaluados.append({'x': x_val, 'y': y_val})
            
            # Generar gráfica
            from metodos_numericos.utils.Grafico import generar_grafica_interpolacion
            grafica = generar_grafica_interpolacion(resultado, "Spline Lineal", puntos_evaluados)
            
            context['resultado'] = resultado
            context['puntos_evaluados'] = puntos_evaluados
            context['grafica'] = grafica
            
        except ValueError as e:
            context['error'] = "Error en el formato de los datos. Verifique que todos los valores sean numéricos."
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo3/spline_lineal.html', context)


def spline_cubico_view(request):
    """Vista para el método de Spline Cúbico."""
    context = {
        'title': 'Spline Cúbico'
    }
    
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            puntos_x_str = request.POST.get('puntos_x', '').strip()
            puntos_y_str = request.POST.get('puntos_y', '').strip()
            puntos_evaluar_str = request.POST.get('puntos_evaluar', '').strip()
            
            # Procesar puntos X e Y
            puntos_x = [float(x.strip()) for x in puntos_x_str.split(',') if x.strip()]
            puntos_y = [float(y.strip()) for y in puntos_y_str.split(',') if y.strip()]
            
            # Validar límite de puntos
            if len(puntos_x) > 8:
                context['error'] = "Se admiten máximo 8 puntos."
                return render(request, 'capitulo3/spline_cubico.html', context)
            
            # Ejecutar método
            from metodos_numericos.utils.SplineCubico import spline_cubico
            resultado = spline_cubico(puntos_x, puntos_y)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido')
                return render(request, 'capitulo3/spline_cubico.html', context)
            
            # Evaluar puntos específicos si se proporcionaron
            puntos_evaluados = []
            if puntos_evaluar_str:
                puntos_evaluar = [float(x.strip()) for x in puntos_evaluar_str.split(',') if x.strip()]
                for x_val in puntos_evaluar:
                    y_val = resultado['funcion_evaluacion'](x_val)
                    puntos_evaluados.append({'x': x_val, 'y': y_val})
            
            # Generar gráfica
            from metodos_numericos.utils.Grafico import generar_grafica_interpolacion
            grafica = generar_grafica_interpolacion(resultado, "Spline Cúbico", puntos_evaluados)
            
            # Preparar datos para la tabla de segundas derivadas
            puntos_derivadas = []
            for i, (x_val, derivada) in enumerate(zip(resultado['puntos_x'], resultado['segundas_derivadas'])):
                puntos_derivadas.append({
                    'indice': i,
                    'x': x_val,
                    'derivada': derivada
                })
            
            context['resultado'] = resultado
            context['puntos_evaluados'] = puntos_evaluados
            context['puntos_derivadas'] = puntos_derivadas
            context['grafica'] = grafica
            
        except ValueError as e:
            context['error'] = "Error en el formato de los datos. Verifique que todos los valores sean numéricos."
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo3/spline_cubico.html', context)


def gauss_seidel_view(request):
    context = {
        'title': 'Método de Gauss-Seidel'
    }
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            matrizA_str = request.POST.get('matrizA')  # cadena con filas separadas por líneas
            vectorB_str = request.POST.get('vectorB')  # cadena con números separados por comas
            vectorX0_str = request.POST.get('vectorX0')  # cadena con números separados por comas
            
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))

            # Convertir la matriz A (cadena) a numpy array
            # Primero convertir la cadena en lista de listas (filas)
            A = []
            for fila in matrizA_str.strip().split('\n'):
                A.append([float(num) for num in fila.split(',')])
            A = np.array(A)

            # Convertir b y x0 a arrays
            b = np.array([float(num) for num in vectorB_str.split(',')])
            x0 = np.array([float(num) for num in vectorX0_str.split(',')]) if vectorX0_str else None

            # Ejecutar el método
            resultado = gauss_seidel(A, b, x0, tolerancia, max_iter)

            # Preparar datos para la plantilla
            context['resultado'] = resultado

        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    return render(request, 'capitulo2/gauss_seidel.html', context)

def jacobi_view(request):
    context = {
        'title': 'Método de Jacobi'
    }
    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            matrizA_str = request.POST.get('matrizA')  # cadena con filas separadas por líneas
            vectorB_str = request.POST.get('vectorB')  # cadena con números separados por comas
            vectorX0_str = request.POST.get('vectorX0')  # cadena con números separados por comas
            
            tolerancia = float(request.POST.get('tolerancia'))
            max_iter = int(request.POST.get('max_iter'))

            # Convertir la matriz A (cadena) a numpy array
            A = []
            for fila in matrizA_str.strip().split('\n'):
                A.append([float(num) for num in fila.split(',')])
            A = np.array(A)

            # Convertir b y x0 a arrays
            b = np.array([float(num) for num in vectorB_str.split(',')])
            x0 = np.array([float(num) for num in vectorX0_str.split(',')]) if vectorX0_str else None

            # Ejecutar el método de Jacobi
            resultado = jacobi(A, b, x0, tolerancia, max_iter)

            # Preparar datos para la plantilla
            context['resultado'] = resultado

        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    return render(request, 'capitulo2/jacobi.html', context)
<<<<<<< HEAD

def vandermonde_view(request):
    context = {
        'title': 'Interpolación con Matriz de Vandermonde'
    }
    
    if request.method == 'POST':
        try:
            # Obtener los puntos x e y del formulario
            x_points_str = request.POST.get('x_points')
            y_points_str = request.POST.get('y_points')
            
            # Convertir las cadenas a listas de números
            x_points = ast.literal_eval(x_points_str)
            y_points = ast.literal_eval(y_points_str)
            
            # Ejecutar el método de Vandermonde
            resultado = vandermonde(x_points, y_points)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido en la interpolación')
                return render(request, 'capitulo3/vandermonde.html', context)
            
            # Agregar resultados al contexto
            context['resultado'] = resultado
            
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo3/vandermonde.html', context)

def lagrange_view(request):
    context = {
        'title': 'Interpolación con Lagrange'
    }
    
    if request.method == 'POST':
        try:
            # Obtener los puntos x e y del formulario
            x_points_str = request.POST.get('x_points')
            y_points_str = request.POST.get('y_points')
            
            # Convertir las cadenas a listas de números
            x_points = ast.literal_eval(x_points_str)
            y_points = ast.literal_eval(y_points_str)
            
            # Ejecutar el método de Lagrange
            resultado = lagrange(x_points, y_points)
            
            if not resultado.get('success', False):
                context['error'] = resultado.get('error', 'Error desconocido en la interpolación')
                return render(request, 'capitulo3/lagrange.html', context)
            
            # Agregar resultados al contexto
            context['resultado'] = resultado
            
        except Exception as e:
            context['error'] = f"Error: {str(e)}"
    
    return render(request, 'capitulo3/lagrange.html', context)
=======
>>>>>>> 8645180 (Jacobi completo)

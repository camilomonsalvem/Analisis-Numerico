from django.shortcuts import render
import numpy as np
from .utils import biseccion, generar_grafica, regla_falsa
from .utils.Gaussseidel import gauss_seidel
import ast
from .utils.Jacobi import jacobi
from .utils.Vandermonde import vandermonde

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
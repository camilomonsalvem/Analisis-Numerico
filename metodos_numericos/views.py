from django.shortcuts import render
from .utils import biseccion, generar_grafica, regla_falsa, punto_fijo, raices_multiples, secante_metodo
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
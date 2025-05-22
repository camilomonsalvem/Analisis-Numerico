from django.shortcuts import render
from .utils import biseccion, generar_grafica, regla_falsa

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
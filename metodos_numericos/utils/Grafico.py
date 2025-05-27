import matplotlib
matplotlib.use('Agg')  # <--- importante
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import sympy as sp
from config.settings import BASE_DIR

def generar_grafica(funcion_str, a, b, raiz=None, metodo=""):
    """
    Genera una gráfica de la función con el intervalo y la raíz marcados.
    
    Args:
        funcion_str (str): Expresión de la función como string.
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.
        raiz (float, optional): Raíz encontrada. Default es None.
        metodo (str, optional): Nombre del método utilizado. Default es "".
        
    Returns:
        str: Imagen de la gráfica codificada en base64.
    """
    # Convertir la función string a una función evaluable
    x = sp.symbols('x')
    funcion_expr = sp.sympify(funcion_str)
    f = sp.lambdify(x, funcion_expr)
    
    # Crear la figura
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Generar puntos para la gráfica
    margen = (b - a) * 0.2
    x_vals = np.linspace(a - margen, b + margen, 500)
    y_vals = []
    
    # Evaluar función en los puntos, manejando posibles errores
    for val in x_vals:
        try:
            y = f(val)
            if not np.isnan(y) and not np.isinf(y) and abs(y) < 100:  # Filtrar valores extremos
                y_vals.append((val, y))
        except:
            pass
    
    if y_vals:
        x_plot = [p[0] for p in y_vals]
        y_plot = [p[1] for p in y_vals]
        ax.plot(x_plot, y_plot, 'b-', label=f'f(x) = {funcion_str}')
    
    # Graficar el eje X
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    
    # Marcar intervalo inicial
    ax.axvline(x=a, color='orange', linestyle='--', alpha=0.7, label=f'a = {a}')
    ax.axvline(x=b, color='orange', linestyle='--', alpha=0.7, label=f'b = {b}')
    
    # Marcar raíz si existe
    if raiz is not None:
        ax.axvline(x=raiz, color='r', linestyle='-', alpha=0.8)
        ax.plot(raiz, 0, 'ro', label=f'Raíz: x = {raiz:.6f}')
    
    # Configuración de la gráfica
    titulo = f'Gráfica de f(x) = {funcion_str}'
    if metodo:
        titulo = f'{metodo}: {titulo}'
    ax.set_title(titulo)
    
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    # Convertir la figura a una imagen en base64
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    return img_str



def plot_matrix_solution(iterations: dict, solution: list[float], spectral_radius: float):
    """
    Grafica las soluciones iterativas de un sistema de ecuaciones lineales (Jacobi para matrices 2x2).

    Args:
        iterations (dict): Diccionario con las iteraciones y los valores aproximados de X.
        solution (list[float]): Solución aproximada del sistema.
        spectral_radius (float): Radio espectral para mostrar en la gráfica.

    Returns:
        None: Genera un archivo SVG con la gráfica.
    """
    output_file = BASE_DIR / "static/img/numerical_method/matrix_solution_plot.svg"

    # Extraer valores de iteración
    x1_values = [iteration["X"][0] for iteration in iterations.values()]
    x2_values = [iteration["X"][1] for iteration in iterations.values()]
    iteration_numbers = list(iterations.keys())

    # Crear la figura
    plt.figure(figsize=(8, 6))

    # Graficar las soluciones x1 y x2 por iteración
    plt.plot(iteration_numbers, x1_values, label="x1 (iterativo)", marker="o", linestyle="-")
    plt.plot(iteration_numbers, x2_values, label="x2 (iterativo)", marker="o", linestyle="-")

    # Añadir la solución final
    plt.axhline(y=solution[0], color="blue", linestyle="-", label=f"x1 solución: {solution[0]:.4f}")
    plt.axhline(y=solution[1], color="green", linestyle="-", label=f"x2 solución: {solution[1]:.4f}")

    # Detalles de la gráfica
    plt.title(f"Evolución iterativa (Radio espectral: {spectral_radius:.4f})")
    plt.xlabel("Iteraciones")
    plt.ylabel("Valor de X")
    plt.legend()
    plt.grid(True)

    # Guardar la gráfica como SVG
    plt.savefig(output_file, format="svg")
    plt.close()


def plot_system_equations(A: list[list[float]], b: list[float], solution: list[float]):
    """
    Genera una gráfica de las ecuaciones de un sistema 2x2 y su solución.

    Args:
        A (list[list[float]]): Matriz de coeficientes (2x2).
        b (list[float]): Vector de términos independientes.
        solution (list[float]): Solución del sistema.

    Returns:
        None: Genera un archivo SVG con la gráfica.
    """
    output_file = BASE_DIR / "static/img/numerical_method/system_plot.svg"

    # Crear las ecuaciones como funciones de x
    x = np.linspace(-10, 10, 500)
    y1 = (b[0] - A[0][0] * x) / A[0][1]  # Primera ecuación
    y2 = (b[1] - A[1][0] * x) / A[1][1]  # Segunda ecuación

    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    
    # Graficar las ecuaciones con líneas continuas
    plt.plot(x, y1, label="Ecuación 1", color="blue", linestyle="-", linewidth=1.5)
    plt.plot(x, y2, label="Ecuación 2", color="green", linestyle="-", linewidth=1.5)
    
    # Añadir el punto de solución y su anotación
    plt.scatter(solution[0], solution[1], color="red", label="Solución", zorder=5)
    plt.text(
        solution[0],
        solution[1],
        f"({solution[0]:.4f}, {solution[1]:.4f})",
        fontsize=10,
        verticalalignment="bottom",
        horizontalalignment="right",
    )

    # Detalles de la gráfica
    plt.title("Sistema de ecuaciones 2x2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.axvline(0, color="black", linewidth=0.5)
    plt.grid(True)
    plt.legend()

    # Guardar la gráfica como SVG
    plt.savefig(output_file, format="svg")
    plt.close()

def generar_grafica_interpolacion(resultado, metodo="Interpolación", puntos_evaluacion=None):
    """
    Genera una gráfica para métodos de interpolación.
    
    Args:
        resultado (dict): Resultado del método de interpolación.
        metodo (str): Nombre del método utilizado.
        puntos_evaluacion (list, optional): Puntos adicionales para evaluar.
        
    Returns:
        str: Imagen de la gráfica codificada en base64.
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    puntos_x = resultado['puntos_x']
    puntos_y = resultado['puntos_y']
    
    # Rango para graficar
    x_min, x_max = min(puntos_x), max(puntos_x)
    margen = (x_max - x_min) * 0.1
    x_plot = np.linspace(x_min - margen, x_max + margen, 500)
    
    # Graficar según el tipo de método
    if 'segmentos' in resultado:  # Spline lineal o cúbico
        # Graficar cada segmento
        for i, segmento in enumerate(resultado['segmentos']):
            x_seg = np.linspace(segmento['x0'], segmento['x1'], 100)
            y_seg = [segmento['funcion'](x) for x in x_seg]
            ax.plot(x_seg, y_seg, '-', linewidth=2, 
                   label=f'Segmento {i+1}' if len(resultado['segmentos']) <= 5 else None)
    
    elif 'polinomio_func' in resultado:  # Newton interpolante
        # Graficar el polinomio completo
        y_plot = []
        for x_val in x_plot:
            try:
                y_val = resultado['polinomio_func'](x_val)
                if not np.isnan(y_val) and not np.isinf(y_val) and abs(y_val) < 1000:
                    y_plot.append(y_val)
                else:
                    y_plot.append(None)
            except:
                y_plot.append(None)
        
        # Filtrar valores válidos
        x_valid = []
        y_valid = []
        for x_val, y_val in zip(x_plot, y_plot):
            if y_val is not None:
                x_valid.append(x_val)
                y_valid.append(y_val)
        
        if x_valid:
            ax.plot(x_valid, y_valid, 'b-', linewidth=2, label='Polinomio interpolante')
    
    # Graficar puntos originales
    ax.plot(puntos_x, puntos_y, 'ro', markersize=8, label='Puntos dados', zorder=5)
    
    # Anotar los puntos
    for i, (x_val, y_val) in enumerate(zip(puntos_x, puntos_y)):
        ax.annotate(f'P{i+1}({x_val}, {y_val})', 
                   (x_val, y_val), 
                   xytext=(5, 5), 
                   textcoords='offset points',
                   fontsize=9,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Graficar puntos de evaluación si existen
    if puntos_evaluacion:
        for punto in puntos_evaluacion:
            x_eval, y_eval = punto['x'], punto['y']
            ax.plot(x_eval, y_eval, 'go', markersize=6, zorder=4)
            ax.annotate(f'({x_eval:.3f}, {y_eval:.3f})', 
                       (x_eval, y_eval), 
                       xytext=(5, -15), 
                       textcoords='offset points',
                       fontsize=8,
                       color='green')
    
    # Configuración de la gráfica
    ax.set_title(f'{metodo} - Gráfica de Interpolación', fontsize=14, fontweight='bold')
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)
    
    # Convertir la figura a una imagen en base64
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    
    return img_str
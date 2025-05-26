import matplotlib
matplotlib.use('Agg')  # <--- importante
import matplotlib.pyplot as plt
import numpy as np
import io
import base64
import sympy as sp

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

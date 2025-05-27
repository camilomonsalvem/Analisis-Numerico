import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def lagrange(x_points, y_points):
    """
    Interpolación polinómica usando método de Lagrange.

    Args:
        x_points (list/array): Lista o array con valores x.
        y_points (list/array): Lista o array con valores y.

    Returns:
        dict: Diccionario con coeficientes, función evaluadora, gráfica codificada, errores, etc.
    """
    x = np.array(x_points, dtype=float)
    y = np.array(y_points, dtype=float)

    n = len(x)
    if len(y) != n:
        return {"error": "x e y deben tener la misma cantidad de elementos.", "success": False}
    if len(np.unique(x)) != n:
        return {"error": "Los valores de x deben ser únicos para interpolar.", "success": False}

    # Construir polinomio de Lagrange
    pol = np.poly1d([0.])
    for i in range(n):
        # Construir polinomio base Li(x)
        li = np.poly1d([1.])
        for j in range(n):
            if j != i:
                # Polinomio (x - x_j) / (x_i - x_j)
                denom = x[i] - x[j]
                if denom == 0:
                    return {"error": "Error en denominador cero.", "success": False}
                li *= np.poly1d([1, -x[j]]) / denom
        pol += y[i] * li

    # Evaluar el polinomio en los puntos originales
    y_fit = pol(x)
    error_por_punto = np.abs(y - y_fit)
    error_total = np.sum(error_por_punto)

    # Grado y coeficientes
    grado = pol.order
    coef_array = pol.coeffs  # coeficientes en orden decreciente

    # Formatear coeficientes como texto legible
    coef_text = " + ".join(
        f"{coef:.6g}*x^{grado - i}" for i, coef in enumerate(coef_array[:-1]) if abs(coef) > 1e-12
    )
    if abs(coef_array[-1]) > 1e-12:
        coef_text += f" + {coef_array[-1]:.6g}"

    # Función evaluadora
    def polinomio_eval(xv):
        return pol(xv)

    # Generar gráfica codificada en base64
    def generar_grafica():
        x_eval = np.linspace(np.min(x), np.max(x), 1000)
        y_eval = pol(x_eval)

        plt.figure(figsize=(8,5))
        plt.plot(x, y, 'ro', label='Puntos originales')
        plt.plot(x_eval, y_eval, 'b-', label='Polinomio interpolante')
        plt.title('Interpolación usando método de Lagrange')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode('ascii')
        return img_base64

    grafica_base64 = generar_grafica()

    return {
        "coeficientes": coef_text,
        "coef_array": coef_array,
        "grado": grado,
        "error_por_punto": error_por_punto,
        "error_total": error_total,
        "polinomio_eval": polinomio_eval,
        "grafica": grafica_base64,
        "success": True
    }

import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def vandermonde(x_points, y_points):
    """
    Interpolación polinómica usando matriz de Vandermonde.

    Args:
        x_points (list/array): Lista o array con valores x.
        y_points (list/array): Lista o array con valores y.

    Returns:
        dict: Diccionario con coeficientes, errores, función evaluadora, gráfica codificada, etc.
    """
    x = np.array(x_points, dtype=float)
    y = np.array(y_points, dtype=float)

    n = len(x)
    if len(y) != n:
        return {
            "error": "x e y deben tener la misma cantidad de elementos.",
            "success": False
        }
    if len(np.unique(x)) != n:
        return {
            "error": "Los valores de x deben ser únicos para interpolar.",
            "success": False
        }

    # Matriz de Vandermonde (potencias decrecientes)
    V = np.vander(x, N=n, increasing=False)

    try:
        a = np.linalg.solve(V, y)
    except np.linalg.LinAlgError:
        return {
            "error": "La matriz de Vandermonde es singular, no se puede resolver.",
            "success": False
        }

    # Dominio para evaluación suave
    x_eval = np.linspace(np.min(x), np.max(x), 1000)
    y_eval = np.polyval(a, x_eval)
    y_fit = np.polyval(a, x)

    # Error absoluto en puntos originales
    error_por_punto = np.abs(y - y_fit)
    error_total = np.sum(error_por_punto)

    # Formatear coeficientes en texto legible
    grado = n - 1
    coef_text = " + ".join(f"{coef:.6g}*x^{grado - i}" for i, coef in enumerate(a[:-1]))
    coef_text += f" + {a[-1]:.6g}"

    # Función evaluadora
    def polinomio_eval(xv):
        return np.polyval(a, xv)

    # Generar gráfica y codificar en base64 para enviar al template
    def generar_grafica():
        plt.figure(figsize=(8,5))
        plt.plot(x, y, 'ro', label='Puntos originales')
        plt.plot(x_eval, y_eval, 'b-', label='Polinomio interpolante')
        plt.title('Interpolación usando método de Vandermonde')
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
        "coef_array": a,
        "grado": grado,
        "error_por_punto": error_por_punto,
        "error_total": error_total,
        "polinomio_eval": polinomio_eval,
        "grafica": grafica_base64,
        "success": True
    }


# # Ejemplo de uso:
# if __name__ == "__main__":
#     x_pts = [1.5, 8.5, 22, 35]
#     y_pts = [-1, 9, 29, 25]

#     res = vandermonde(x_pts, y_pts)
#     res['graficar']()
#     res['graficar']()

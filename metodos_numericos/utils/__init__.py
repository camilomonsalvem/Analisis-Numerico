from .Biseccion import biseccion
from .Grafico import generar_grafica, plot_matrix_solution, plot_system_equations
from .ReglaFalsa import regla_falsa
from .PuntoFijo import punto_fijo
from .RaicesMultiples import raices_multiples
from .Secante import secante_metodo
from .Newton import newton_metodo
from .sor_metodo import sor_metodo  # Importa tu clase SOR

__all__ = [
    "biseccion",
    "generar_grafica",
    "plot_matrix_solution",
    "plot_system_equations",
    "regla_falsa",
    "punto_fijo",
    "raices_multiples",
    "secante_metodo",
    "newton_metodo",
    "sor_metodo",  # Exporta la clase SOR
]

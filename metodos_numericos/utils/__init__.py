from .Biseccion import biseccion
from .Grafico import generar_grafica, plot_matrix_solution, plot_system_equations
from .ReglaFalsa import regla_falsa
from .PuntoFijo import punto_fijo
from .RaicesMultiples import raices_multiples
from .Secante import secante_metodo
from .Newton import newton_metodo
from .sor_metodo import sor_metodo
from .NewtonInterpolante import newton_interpolante
from .SplineLineal import spline_lineal
from .SplineCubico import spline_cubico
from .Jacobi import jacobi
from .Vandermonde import vandermonde
from .Lagrange import lagrange
from .Gaussseidel import gauss_seidel
from .Jacobi import jacobi

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
    "sor_metodo",
    "newton_interpolante",
    "spline_lineal",
    "spline_cubico",
    "jacobi_metodo",
    "vandermonde_metodo",
    "lagrange_metodo",
    "gauss_seidel_metodo",
    
]

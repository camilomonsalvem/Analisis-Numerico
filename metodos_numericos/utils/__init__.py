from .Biseccion import biseccion
from .Newton import newton
from .PuntoFijo import punto_fijo
from .Gauss import gauss_piv
from .SOR import sor
from .Secante import secante_method
from .ReglaFalsa import regla_falsa
from .Grafico import grafico
from .Jacobi import jacobi

__all__ = [
    "biseccion",
    "newton",
    "punto_fijo",
    "gauss_piv",
    "sor",
    "secante_method",
    "regla_falsa",
    "grafico",
    "jacobi",
]
# __all__ is a list of public objects of that module, as interpreted by import *
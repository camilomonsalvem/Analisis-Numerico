from abc import ABC, abstractmethod
from typing import List, Union

class matriz(ABC):
    @abstractmethod
    def solve(
        self,
        A: List[List[float]],
        b: List[float],
        x0: List[float],
        tolerance: float,
        max_iterations: int,
        **kwargs,
    ) -> dict:
        """
        Resuelve el sistema lineal Ax = b usando un método iterativo específico.

        Args:
            A (List[List[float]]): Matriz de coeficientes (cuadrada).
            b (List[float]): Vector de términos independientes.
            x0 (List[float]): Vector inicial de aproximación.
            tolerance (float): Tolerancia para el criterio de parada.
            max_iterations (int): Número máximo de iteraciones.
            **kwargs: Parámetros adicionales específicos del método.

        Returns:
            dict: Diccionario con resultados, incluyendo:
                - solution: aproximación a la solución
                - iterations: detalles por iteración
                - converged: booleano indicando si el método convergió
                - spectral_radius (opcional): radio espectral del método
                - message (opcional): mensaje descriptivo
        """
        pass

    @abstractmethod
    def validate_input(
        self,
        matrix_a_raw: str,
        vector_b_raw: str,
        initial_guess_raw: str,
        tolerance: float,
        max_iterations: int,
        **kwargs,
    ) -> Union[str, List]:
        """
        Valida las entradas recibidas y retorna un error descriptivo o los datos parseados.

        Args:
            matrix_a_raw (str): Matriz A como texto (e.g. filas separadas por ';' y valores por espacios).
            vector_b_raw (str): Vector b como texto (valores separados por espacios).
            initial_guess_raw (str): Vector inicial x0 como texto.
            tolerance (float): Tolerancia.
            max_iterations (int): Número máximo de iteraciones.
            **kwargs: Parámetros adicionales.

        Returns:
            str | List: Mensaje de error o lista con [A, b, x0] parseados.
        """
        pass

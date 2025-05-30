from django.urls import path
from . import views

app_name = 'metodos_numericos'

urlpatterns = [
    # Página principal
    path('', views.index, name='home'),
    
    # Capítulo 1
    path('capitulo1/', views.capitulo1, name='capitulo1'),
    path('capitulo1/biseccion/', views.biseccion_view, name='biseccion'),
    path('capitulo1/regla-falsa/', views.regla_falsa_view, name='regla_falsa'),
    path('capitulo1/punto-fijo/', views.punto_fijo_view, name='punto_fijo'),
    path('capitulo1/raices_multiples/', views.raices_multiples_view, name='raices_multiples'),
    path('capitulo1/secante-metodo/', views.secante_metodo_view, name='secante_metodo'),
    path('capitulo1/newton-metodo/', views.newton_metodo_view, name='newton_metodo'),


    
    # Capítulo 2
    path('capitulo2/', views.capitulo2, name='capitulo2'),
    path('capitulo2/gauss-seidel/', views.gauss_seidel_view, name='gauss_seidel'),
    path('capitulo2/jacobi/', views.jacobi_view, name='jacobi'),
    path('capitulo2/sor-metodo/', views.sor_metodo_view, name='sor_metodo'),
    
    # Capítulo 3
    path('capitulo3/', views.capitulo3, name='capitulo3'),
    path('capitulo3/vandermonde/', views.vandermonde_view, name='vandermonde'),
    path('capitulo3/lagrange/', views.lagrange_view, name='lagrange'),
    path('capitulo3/newton-interpolante/', views.newton_interpolante_view, name='newton_interpolante'),
    path('capitulo3/spline-lineal/', views.spline_lineal_view, name='spline_lineal'),
    path('capitulo3/spline-cubico/', views.spline_cubico_view, name='spline_cubico'),
]
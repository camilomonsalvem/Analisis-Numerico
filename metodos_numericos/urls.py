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
    
    # Capítulo 2
    path('capitulo2/', views.capitulo2, name='capitulo2'),
    path('capitulo2/gauss-seidel/', views.gauss_seidel_view, name='gauss_seidel'),
    path('capitulo2/jacobi/', views.jacobi_view, name='jacobi'),
    
    # Capítulo 3
    path('capitulo3/', views.capitulo3, name='capitulo3'),
]
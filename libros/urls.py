from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('libros/', views.libros, name='libros'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('libros/crear', views.crear_libro, name='crear_libro'),
    path('libros/<int:id_libro>', views.edit_libro, name='edit_libro'),
    path('libros/<int:id_libro>/eliminar', views.eliminar_libro, name='eliminar_libro')

    
]
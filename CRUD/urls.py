from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarReal/', views.registrarReal),
    path('eliminarReal/<nombre>', views.eliminarReal),
    path('edicionReal/<nombre>', views.edicionReal),
    path('editarReal/', views.editarReal),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index" ),
    path("about", views.about, name="about" ),
    # path("dolar", views.dolar, name="dolar" ),
    # path("dolar-api", views.dolar_service, name="dolar_service" ),
    path("cursos", views.cursos, name="cursos"),
    path("nuevo-curso", views.nuevo_curso, name="nuevo_curso" ),
]
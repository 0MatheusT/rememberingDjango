from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_enquete>/", views.detalhes, name="detalhes"),
    path("<int:id_enquete>/resultados/", views.resultados, name="resultados"),
    path("<int:id_enquete>/votar/", views.votar, name="votar"),
]

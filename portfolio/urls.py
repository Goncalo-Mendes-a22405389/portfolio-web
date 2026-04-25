## portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("",views.licenciatura_view,),
    path("tfcs/",views.tfc_view,name = "tfcs"),
    path("licenciaturas/", views.licenciatura_view, name = "licenciaturas"),
    path("licenciaturas/<int:id>/", views.detalhe_licenciatura, name="detalhe_licenciatura"),
    path("anos/<int:id>/", views.detalhe_ano, name="detalhe_ano"),
    path("docentes/<int:id>/", views.detalhe_docente, name="detalhe_docente"),
    path("projetos/", views.projetos_view, name="projetos"),
    path("tecnologias/", views.tecnologias_view, name="tecnologias"),
    path("competencias/", views.competencias_view, name="competencias"),
    path("makingof/", views.makingof_view,name="makingof"),
]
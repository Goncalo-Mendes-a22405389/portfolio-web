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
    path("formacoes/", views.formacao_view, name = "formacoes"),
    path('projeto/novo', views.novo_projeto_view, name="novo_projeto"),
    path('projeto/<int:projeto_id>/edita', views.edita_projeto_view,name="edita_projeto"),
    path('projeto/<int:projeto_id>/apaga', views.apaga_projeto_view,name="apaga_projeto"),
    path("tecnologia/nova", views.nova_tecnologia_view, name = "nova_tecnologia"),
    path("tecnologia/<int:tecnologia_id>/edita", views.edita_tecnologia_view, name = "edita_tecnologia"),
    path("tecnologia/<int:tecnologia_id>/apaga", views.apaga_tecnologia_view,name = "apaga_tecnologia"),
    path("competencia/nova", views.nova_competencia_view, name = "nova_competencia"),
    path("competencia/<int:competencia_id>/edita", views.edita_competencia_view, name ="edita_competencia"),
    path("competencia/<int:competencia_id>/apaga", views.apaga_competencia_view, name = "apaga_competencia"),
    path("formacao/novo",views.nova_formacao_view, name = "nova_formacao"),
    path("formacao/<int:formacao_id>/edita", views.edita_formacao_view, name = "edita_formacao"),
    path("formacao/<int:formacao_id>/apaga", views.apaga_formacao_view, name = "apaga_formacao"),
    
]
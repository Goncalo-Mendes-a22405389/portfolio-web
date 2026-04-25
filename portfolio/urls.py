## portfolio/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("",views.index_view, name = "index"),
    path("tfcs/",views.tfc_view,name = "tfcs"),
    path("licenciaturas/", views.licenciatura_view, name = "licenciaturas"),
    path("licenciaturas/<int:id>/", views.detalhe_licenciatura, name="detalhe_licenciatura"),
    
]
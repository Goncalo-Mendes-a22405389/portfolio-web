from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artigos, name='artigos'),
    path('novo/', views.criar_artigo, name='criar_artigo'),
    path('<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
    path('<int:artigo_id>/apaga', views.apaga_artigo_view, name="apaga_artigo"),
    path('like/<int:artigo_id>/', views.like_artigo, name='like_artigo'),
    path('<int:artigo_id>/', views.detalhe_artigo, name='detalhe_artigo'),
]
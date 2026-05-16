from django.contrib import admin
from .models import *

# Register your models here.

class ArtigosAdmin(admin.ModelAdmin):
    list_display = ("autor", "texto", "data_criacao")
    ordering = ("autor",)
    search_fields = ("autor", "texto", "data_criacao")
    
admin.site.register(Artigo,ArtigosAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("autor", "texto", "data_criacao")
    ordering = ("autor",)
    search_fields = ("autor", "texto", "data_criacao")
    
admin.site.register(Comentario,ComentarioAdmin)

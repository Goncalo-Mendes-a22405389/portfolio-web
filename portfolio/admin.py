from django.contrib import admin
from .models import *

# Register your models here.

class LicenciaturaAdmin(admin.ModelAdmin):
    list_display = ("nome", "sigla", "universidade", "duracao_anos")
    ordering = ("nome",)
    search_fields = ("nome", "sigla", "universidade")

admin.site.register(Licenciatura, LicenciaturaAdmin)

class AnoAdmin(admin.ModelAdmin):
    list_display = ("ano", "licenciatura")
    ordering = ("licenciatura", "ano")
    search_fields = ("licenciatura__nome",)

admin.site.register(Ano, AnoAdmin)

class DocenteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "degree")
    ordering = ("nome",)
    search_fields = ("nome", "email")

admin.site.register(Docente, DocenteAdmin)

class UnidadeCurricularAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo", "ano", "semestre", "ects")
    ordering = ("ano", "semestre", "nome")
    search_fields = ("nome", "codigo")

admin.site.register(UnidadeCurricular, UnidadeCurricularAdmin)

class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nome", "website",)
    ordering = ("nome",)
    search_fields = ("nome",)

admin.site.register(Tecnologia, TecnologiaAdmin)

class CompetenciaAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo",)
    ordering = ("nome",)
    search_fields = ("nome", "tipo")

admin.site.register(Competencia, CompetenciaAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "uc", )
    ordering = ("titulo",)
    search_fields = ("titulo", "uc__nome", "github_url")

admin.site.register(Projeto, ProjetoAdmin)

class FormacaoAdmin(admin.ModelAdmin):
    list_display = ("nome", "entidade", )
    ordering = ("nome",)
    search_fields = ("nome", "entidade")

admin.site.register(Formacao, FormacaoAdmin)

class TFCAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "orientador", "classificacao")
    ordering = ("titulo", "autor","orientador")
    search_fields = ("titulo", "autor", "orientador")

admin.site.register(TFC, TFCAdmin)

class MakingOfAdmin(admin.ModelAdmin):
    list_display = ("titulo", )
    ordering = ("titulo",)
    search_fields = ("titulo",)

admin.site.register(MakingOf, MakingOfAdmin)
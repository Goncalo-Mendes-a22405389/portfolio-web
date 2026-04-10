from django.db import models

# Create your models here.

from django.db import models

class Licenciatura(models.Model):
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=20)
    descricao = models.TextField()
    duracao_anos = models.IntegerField()
    universidade = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Ano(models.Model):
    licenciatura = models.ForeignKey(Licenciatura, on_delete=models.CASCADE, related_name='anos')
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.ano}º Ano - {self.licenciatura.sigla}"

class Docente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cardCode = models.IntegerField()
    regimen = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    pagina_lusofona = models.URLField(blank=True)


    def __str__(self):
        return self.nome

class UnidadeCurricular(models.Model):
    ano = models.ForeignKey(Ano, on_delete=models.CASCADE, related_name='ucs')
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20)
    semestre = models.CharField(max_length=100)
    descricao = models.TextField()
    docentes = models.ManyToManyField(Docente, related_name='ucs', blank = True)
    ects = models.IntegerField()
    image = models.ImageField(upload_to="uc/", blank = True)

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    website = models.URLField()
    image = models.ImageField(upload_to="tecnologias/",blank=True)

    def __str__(self):
        return self.nome

class Competencia(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField()
    tecnologias = models.ManyToManyField(Tecnologia, related_name='competencias', blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    uc = models.ForeignKey(UnidadeCurricular, on_delete=models.CASCADE, related_name='projetos')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    conceitos_aplicados = models.TextField()
    github_url = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    image = models.ImageField(upload_to="projetos/", blank = True)

    def __str__(self):
        return self.titulo

class Formacao(models.Model):
    nome = models.CharField(max_length=200)
    entidade = models.CharField(max_length=200)
    descricao = models.TextField()
    certificado_url = models.URLField()
    competencias = models.ManyToManyField(Competencia, related_name='formacoes')

    def __str__(self):
        return self.nome

class TFC(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    orientador = models.CharField(max_length=100)
    licenciatura = models.CharField(max_length=100)
    pdf = models.URLField(blank=True)
    image = models.URLField(blank=True)
    descricao = models.TextField()
    area = models.CharField(max_length=100)
    palavras_chaves = models.CharField(max_length=100)
    tecnologias = models.CharField(max_length=100)
    classificacao = models.FloatField()

    def __str__(self):
        return f"{self.titulo}"

class MakingOf(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ficheiro = models.FileField(upload_to="registos/")

    def __str__(self):
        return self.titulo
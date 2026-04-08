from portfolio.models import *
import json

TFC.objects.all().delete()

with open("portfolio/data/tfcs.json", "r", encoding="utf-8") as f:
    tfcs = json.load(f)

    for tfc in tfcs:
        TFC.objects.create(
            titulo = tfc["Titulo"],
            autor = tfc["Nome"],
            email = tfc["Email"],
            orientador = tfc["Orientador"],
            licenciatura = tfc["Licenciatura"],
            pdf = tfc["Pdf"],
            image = tfc["Imagem"],
            descricao = tfc["Resumo"],
            area = tfc["Áreas"],
            palavras_chaves = tfc["Palavras chave"],
            tecnologias = tfc["Tecnologias usadas"],
            classificacao = tfc["Rating"]
        )


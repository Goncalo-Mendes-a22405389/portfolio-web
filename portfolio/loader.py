from portfolio.models import *
import json

UnidadeCurricular.objects.all().delete()
Docente.objects.all().delete()
Ano.objects.all().delete()
Licenciatura.objects.all().delete()

with open("portfolio/data/files/ULHT260-PT.json", encoding="utf-8") as f:
    data = json.load(f)

lic = Licenciatura.objects.create(
    nome="Engenharia Informática",
    sigla="LEI",
    descricao="Licenciatura em Engenharia Informática",
    duracao_anos=3,
    universidade="Universidade Lusófona"
)

anos = {
    1: Ano.objects.create(licenciatura=lic, ano=1),
    2: Ano.objects.create(licenciatura=lic, ano=2),
    3: Ano.objects.create(licenciatura=lic, ano=3),
}

for t in data.get("teachers"):
    Docente.objects.create(
        nome=t.get("fullName"),
        email=t.get("email", "None"),
        cardCode=t.get("cardCode", 0),
        regimen=t.get("regimen", "None"),
        degree=t.get("degree", "None"),
        pagina_lusofona=""
    )

for uc in data.get("courseFlatPlan"):
    code = uc.get("curricularIUnitReadableCode")
    year = uc.get("curricularYear")

    descricao = "None"

    with open(f"portfolio/data/files/{code}-PT.json", encoding="utf-8") as f_uc:
        uc_data = json.load(f_uc)
        descricao = uc_data.get("presentation", "None")

    UnidadeCurricular.objects.create(
        nome=uc.get("curricularUnitName"),
        codigo=code,
        ano=anos.get(year),
        semestre=uc.get("semester"),
        descricao=descricao,
        ects = uc.get("ects")
    )
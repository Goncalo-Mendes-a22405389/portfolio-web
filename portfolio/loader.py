from portfolio.models import *
import json

Docente.objects.all().delete()

with open("portfolio/data/files/ULHT260-PT.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    for docente in data["teachers"]:
        Docente.objects.create(
            nome=docente["fullName"],
            email=docente.get("email", "None"),
            cardCode= docente["cardCode"],
            regimen = docente["regimen"],
            degree = docente.get("degree","None"),
            pagina_lusofona=""
        )

import os

from django.conf import settings
from django.core.files import File

from portfolio.models import *   # adaptar ao modelo


for obj in MakingOf.objects.all():   ### alterar  Projeto Curso UC Tecnologia 

    if obj.ficheiro and obj.ficheiro.name: ## altear para image

        # caminho físico do ficheiro em media/
        local_path = os.path.join(settings.MEDIA_ROOT, obj.ficheiro.name)

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.ficheiro.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )

            print(f"Migrado: {obj}")

        else:
            print(f"Ficheiro não encontrado: {local_path}")
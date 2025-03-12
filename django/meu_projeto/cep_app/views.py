from django.shortcuts import render

from django.shortcuts import render
import requests


def consulta_cep(request):
    endereco = None
    error = None

    if request.method == "POST":
        cep = request.POST.get("cep")
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

        if response.ok:
            endereco = response.json()
        else:
            error = "CEP não encontrado"

    return render(request, "index.html", {"endereco": endereco, "error": error})

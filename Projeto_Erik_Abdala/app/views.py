from django.shortcuts import render
from django.http.response import HttpResponse
from . models import *
from django.http import JsonResponse
from .serializers import QuestaoSerializer
from rest_framework import viewsets
import requests

# Create your views here.

def area(request):

    areas = {
        'areas':Area.objects.all()
    }

    return render(request, 'exibicao/area/area.html', areas)

def subarea(request):

    subareas = {
        'subareas':Subarea.objects.all()
    }

    return render(request, 'exibicao/subarea/subarea.html', subareas)

def topico(request):

    topicos = {
        'topicos':Topico.objects.all()
    }

    return render(request, 'exibicao/topico/topico.html', topicos)

def fisico(request):

    fisicos = {
        'fisicos':Fisico.objects.all()
    }

    return render(request, 'exibicao/fisico/fisico.html', fisicos)

def invencao(request):

    invencoes = {
        'invencoes':Invencao.objects.all()
    }

    return render(request, 'exibicao/invencao/invencao.html', invencoes)

def questionario(request):

    questionarios = {
        'questionarios':Questionario.objects.all()
    }

    return render(request, 'exibicao/questionario/invencao.html', questionarios)

def ocupacao(request):

    ocupacoes = {
        'ocupacoes':Ocupacao.objects.all()
    }

    return render(request, 'exibicao/ocupacao/ocupacao.html', ocupacoes)

def pessoa(request):

    pessoas = {
        'pessoas':Pessoa.objects.all()
    }

    return render(request, 'exibicao/pessoa/pessoa.html', pessoas)

def Temporario(request):

    response = requests.get("http://127.0.0.1:8000/temporario/q/")

    if request.method == "GET":

        if response.status_code == 200:

            try:

                questao = response.json()

                return render(request, 'temp.html', {'questao':questao}) # return render(request, 'temp.html')
            
            except ValueError as e:

                print("Não foi possível extrair os dados JSON")

        else:

            print("A solicitação falhou: {response.status_code}")

        return JsonResponse ({"error":"Erro ao recuperar dados"}, status = 500)
    
    else:

        resposta = request.POST.get("Q1")

        if resposta == "A":

            return HttpResponse("Acertou!")
        
        else:

            return HttpResponse("Errou!")
        
class QuestaoViewsSet(viewsets.ModelViewSet):

    queryset = Questao.objects.all()

    serializer_class = QuestaoSerializer
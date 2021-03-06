from django.http import HttpResponse, Http404, HttpResponseRedirect

# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from .models import Pergunta, Escolha


# def index(request):
#    ultimas_perguntas_lista = Pergunta.objects.order_by("data_publicacao")[:5]
#    # saida = ", ".join([p.texto_pergunta for p in ultimas_perguntas_lista])
#    # return HttpResponse(saida)  //Sem template
#    template = loader.get_template("enquetes/index.html")
#    conteudo = {
#        "ultimas_perguntas_lista": ultimas_perguntas_lista,
#    }
#    return HttpResponse(template.render(conteudo, request))


# De uma forma mais curta a função de renderização anterior
def index(request):
    ultimas_perguntas_lista = Pergunta.objects.order_by("data_publicacao")[:5]
    conteudo = {"ultimas_perguntas_lista": ultimas_perguntas_lista}
    return render(request, "enquetes/index.html", conteudo)


""" def detalhes(request, id_enquete):
    # return HttpResponse("Você está olhando para a enquete: %s." % id_enquete)
    try:
        pergunta = Pergunta.objects.get(pk=id_enquete)
    except Pergunta.DoesNotExist:
        raise Http404("Inexistente!")
    return render(request, "enquetes/detalhes.html", {"pergunta": pergunta}) """


def detalhes(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    return render(request, "enquetes/detalhes.html", {"pergunta": pergunta})


"""def resultados(request, id_enquete):
    resposta = "Você está olhando os resultados da enquete: %s."
    return HttpResponse(resposta % id_enquete)
"""


def resultados(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    return render(request, "enquetes/resultados.html", {"pergunta": pergunta})


"""def votar(request, id_enquete):
    return HttpResponse("Você está votando na seguinte enquete: %s." % id_enquete)"""


def votar(request, id_enquete):
    pergunta = get_object_or_404(Pergunta, pk=id_enquete)
    try:
        selected_choice = pergunta.escolha_set.get(pk=request.POST["escolha"])
    except (KeyError, Escolha.DoesNotExist):

        # Redisplay the question voting form.
        return render(
            request,
            "enquetes/detalhes.html",
            {
                "pergunta": pergunta,
                "error_message": "Você não selecionou uma resposta.",
            },
        )
    else:
        selected_choice.votos += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("enquetes:resultados", args=(pergunta.id,)))

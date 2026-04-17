from django.shortcuts import render, redirect
from .forms import EventoForm

eventos = [{"nome": "Seminário de estatística", "local": "Laboratório 01",},
	{"nome": "Semana da TI", "local": "Auditório"}]

def home(request):
    return render(request, 'home.html', {"eventos": eventos})

def novo_evento(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            eventos.append({
                "nome": form.cleaned_data["nome"],
                "local": form.cleaned_data["local"]
            })
            return redirect('home')
    else:
        form = EventoForm()

    return render(request, 'novo.html', {"form": form})
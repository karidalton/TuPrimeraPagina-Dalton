from django.shortcuts import redirect, render
from . import models
from . import forms

def index(request):
    return render(request, "Gimnasio/index.html")

def sede_list(request):
    consulta = models.Sede.objects.all()
    contexto = {"sedes": consulta}
    return render(request, "Gimnasio/sede_list.html", contexto)
    

def plan_list(request):
    consulta= models.Plan.objects.all()
    contexto = {"planes": consulta}
    return render(request, "Gimnasio/plan_list.html", contexto)

def suscriptor_list(request):
    consulta= models.Suscriptor.objects.all()
    contexto = {"suscriptores": consulta}
    return render(request, "Gimnasio/suscriptor_list.html", contexto)

def suscriptor_por_sede(request):
    consulta= models.SuscriptoPorSede.objects.all()
    contexto = {"suscriptores": consulta}
    return render(request, "Gimnasio/suscriptor_por_sede.html", contexto)


def suscriptor_form(request):
    if request.method == "POST":
        form = forms.SuscriptorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suscriptor_list")
    else:
        form = forms.SuscriptorForm()
    return render(request, "Gimnasio/suscriptor_form.html", {"form": form})


def sede_form(request):
    if request.method == "POST":
        form = forms.SedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sede_list")
    else:
        form = forms.SedeForm()
    return render(request, "Gimnasio/sede_form.html", {"form": form})

def asignar_sede_form(request):
    if request.method == "POST":
        form = forms.SuscriptoPorSedeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("suscriptor_por_sede")
    else:
        form = forms.SuscriptoPorSedeForm()
    return render(request, "Gimnasio/asignacion_sede_form.html", {"form": form})
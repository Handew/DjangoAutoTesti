from app.models import Auto, Myyja
from django.shortcuts import redirect, render
from .models import Myyja, Auto

def landingview(request):
    return render (request, 'landing.html')


# MYYJÄ PUOLI
def myyjalistanakyma(request):
    myyjatlista = Myyja.objects.all()
    context = {'myyjat': myyjatlista}
    return render (request, "myyjat.html", context)

def lisaamyyja(request):
    a = request.POST['nimi']
    b = request.POST['puhelinnumero']
    c = request.POST['email']
    Myyja(nimi = a, puhelinnumero = b, email = c).save()
    return redirect(request.META['HTTP_REFERER'])

def poistamyyja(request, id):
    Myyja.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])

# AUTO PUOLI
def autolistanakyma(request):
    autotlista = Auto.objects.all()
    context = {'autot': autotlista}
    return render (request, "autot.html", context)

def lisaaauto(request):
    a = request.POST['merkki']
    b = request.POST['malli']
    c = request.POST['vuosimalli']
    d = request.POST['mittarilukema']
    e = request.POST['hinta']
    f = request.POST['vari']
    g = request.POST['myyja']
    Auto(merkki = a, malli = b, vuosimalli = c, mittarilukema = d, hinta = e, vari = f, myyja = Myyja.objects.get(id=g)).save()
    return redirect(request.META['HTTP_REFERER'])

def poistaauto(request, id):
    Auto.objects.filter(id = id).delete()
    return redirect(request.META['HTTP_REFERER'])
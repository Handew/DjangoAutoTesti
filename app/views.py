from app.models import Auto, Myyja
from django.shortcuts import redirect, render
from .models import Myyja, Auto
from django.contrib.auth import authenticate, login, logout

def landingview(request):
    return render (request, 'landing.html')

# KIRJAUTUMINEN
def loginnakyma(request):
    return render(request, "login.html")

def login_action(request):
    user = request.POST['kayttajanimi']
    passw = request.POST['salasana']
    user = authenticate(username = user, password = passw)
    if user:
        login(request, user)
        context = {'name': user}
        return render(request,'landing.html',context)
    else:
        return render(request, 'loginerror.html')

def logout_action(request):
    logout(request)
    return render(request, 'login.html')



# MYYJÄ PUOLI
def myyjalistanakyma(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        myyjatlista = Myyja.objects.all()
        context = {'myyjat': myyjatlista}
        return render (request, "myyjat.html", context)

def lisaamyyja(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        a = request.POST['nimi']
        b = request.POST['titteli']
        c = request.POST['puhelinnumero']
        d = request.POST['email']
        Myyja(nimi = a, titteli = b, puhelinnumero = c, email = d).save()
        return redirect(request.META['HTTP_REFERER'])

def poistamyyja(request, id):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:    
        Myyja.objects.filter(id = id).delete()
        return redirect(request.META['HTTP_REFERER'])

# AUTO PUOLI
def autolistanakyma(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        autotlista = Auto.objects.all()
        myyjatlista = Myyja.objects.all()
        context = {'autot': autotlista, 'myyjat': myyjatlista}
        return render (request, "autot.html", context)

def lisaaauto(request):
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:    
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
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        Auto.objects.filter(id = id).delete()
        return redirect(request.META['HTTP_REFERER'])
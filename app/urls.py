from django.urls import path
from django.urls import path
from .views import autolistanakyma, landingview, lisaaauto, lisaamyyja, loginnakyma, myyjalistanakyma, poistaauto, poistamyyja, login_action, logout_action

urlpatterns = [
    path('landing/', landingview),

    # LOGIN
    path('', loginnakyma),
    path('login/', login_action),
    path('logout/', logout_action),

    # MYYJÄT
    path('myyjat/', myyjalistanakyma),
    path('lisaa-myyja/', lisaamyyja),
    path('poista-myyja/<int:id>/', poistamyyja),

    # AUTOT
    path('autot/', autolistanakyma),
    path('lisaa-auto/', lisaaauto),
    path('poista-auto/<int:id>/', poistaauto),
]
from django.urls import path
from django.urls import path
from .views import autolistanakyma, landingview, lisaaauto, lisaamyyja, myyjalistanakyma, poistaauto, poistamyyja

urlpatterns = [
    path('landing/', landingview),

    # MYYJÄT
    path('myyjat/', myyjalistanakyma),
    path('lisaa-myyja/', lisaamyyja),
    path('poista-myyja/<int:id>/', poistamyyja),

    # AUTOT
    path('autot/', autolistanakyma),
    path('lisaa-auto/', lisaaauto),
    path('poista-auto/<int:id>/', poistaauto),
]
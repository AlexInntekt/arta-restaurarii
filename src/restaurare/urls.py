from django.urls import path
from restaurare.views import restaurare_main, lemn, piatra

urlpatterns = [
    path('prezentare', restaurare_main, name="restaurare_main"),
    path('lemn', lemn, name="lemn"),
    path('piatra', piatra, name="piatra"),

] 
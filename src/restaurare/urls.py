from django.urls import path
from restaurare.views import restaurare_main

urlpatterns = [
    path('prezentare', restaurare_main, name="restaurare_main"),

]
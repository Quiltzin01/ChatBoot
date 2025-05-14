from django.urls import path
from .views import procesar_txt

urlpatterns = [
    path('procesar/', procesar_txt, name='procesar_txt'),
]

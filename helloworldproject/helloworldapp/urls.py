from django.urls import path
from .views import hello_function

urlpatterns = [
    path('world/', hello_function),
]

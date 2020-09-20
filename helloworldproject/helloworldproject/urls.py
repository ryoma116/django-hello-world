from django.contrib import admin
from django.urls import path
from .views import hello_world_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world_function)
]

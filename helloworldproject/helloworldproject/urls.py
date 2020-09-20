from django.contrib import admin
from django.urls import path
from .views import hello_world_function, HelloWorldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hello_world_function),
    path('helloworld2/', HelloWorldView.as_view())
]

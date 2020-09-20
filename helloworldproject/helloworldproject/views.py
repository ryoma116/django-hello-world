from django.http import HttpResponse


def hello_world_function(request):
    return HttpResponse('<h1>hello world</h1>')

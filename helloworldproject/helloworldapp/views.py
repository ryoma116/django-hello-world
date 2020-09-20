from django.http import HttpResponse


# Create your views here.
def hello_function(request):
    response = HttpResponse('hello')
    return response

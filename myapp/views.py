
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("<h1>estas viendo la seccion About</h1>")

def gallery(request):
    return HttpResponse("<h1>estas viendo la seccion Gallery</h1>")
    

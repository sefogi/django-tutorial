
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>index page.</h2>")
def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello world {}</h2>".format(username) )

def about(request):
    return HttpResponse("<h1>estas viendo la seccion About</h1>")

def gallery(request):
    return HttpResponse("<h1>estas viendo la seccion Gallery</h1>")
    

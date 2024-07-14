
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse("<h2>index page.</h2>")

def entero(request,id):
    print(entero)
    return HttpResponse("<h2>El numero es {}</h2>".format(id))
def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello world {}</h2>".format(username) )

def about(request):
    return HttpResponse("<h1>estas viendo la seccion About</h1>")

def gallery(request):
    return HttpResponse("<h1>estas viendo la seccion Gallery</h1>")

def Projects(request): 
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def Tasks(request,title):
    task =get_object_or_404 (Task, title=title)
    return HttpResponse('task:{}'.format(task.title))

     


from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render


# Create your views here.

def index(request):
    return render (request,'index.html')

def entero(request,id):
    print(entero)
    return HttpResponse("<h2>El numero es {}</h2>".format(id))
def hello(request, username):
    print(username)
    return HttpResponse("<h2>Hello world {}</h2>".format(username) )

def about(request):
    return render(request,"about.html")

def gallery(request):
    return HttpResponse("<h1>estas viendo la seccion Gallery</h1>")

def projects(request): 
   projects = Project.objects.all()
   return render (request, 'projects.html', {'projects': projects})

def tasks(request):
   tasks = Task.objects.all ()
   return render(request, 'tasks.html',{
        'tasks': tasks
    })

     

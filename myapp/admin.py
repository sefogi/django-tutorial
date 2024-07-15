from django.contrib import admin
from .models import Project,Task

# Register your models here.
# aqui usamos el objecto admin que django importa llamamos al andmin del site y el metodo register
admin.site.register(Project)
admin.site.register(Task)


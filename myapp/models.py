from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    # esta funcion me permite ver el nombre de las opciones del 'projects'
    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title + '-' + self.Project.name 
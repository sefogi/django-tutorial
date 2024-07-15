from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index ),
    path('about/',views.about),
    path('gallery/', views.gallery),
    path('hello/<str:username>', views.hello ),
    path('entero/<int:id>', views.entero),
    path('Projects/',views.Projects),
    path('Tasks/<str:title>',views.Tasks),
    
]

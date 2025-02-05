from django.shortcuts import render

# Create your views here.
rom .models import Proyecto

def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'home.html', {'proyectos': proyectos})
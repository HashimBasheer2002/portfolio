from django.shortcuts import render
from .import models

# Create your views here.

from django.shortcuts import render
from .models import Project  # ✅ Add this line

# views.py
from django.shortcuts import render
from .models import Project

from .models import Experience

def home(request):
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    for project in projects:
        project.tech_list = [tech.strip() for tech in project.tech_stack.split(',')]

    return render(request, 'home.html', {'projects': projects, 'experiences': experiences})


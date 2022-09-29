from django.shortcuts import render
from .models import Developer,Question,Choice
# Create your views here.

def index(request):
    developers = Developer.objects.all()
    context = {
        'developers': developers,
    }
    return render(request, 'index.html', context=context)
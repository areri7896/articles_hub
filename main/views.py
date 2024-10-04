from django.shortcuts import render
from .models import article
# Create your views here.
def home(request):
    arts = article.objects.all()
    return render(request, 'index.html', {'arts': arts})

def about(request):
    arts = article.objects.all()
    return render (request, 'about.html', {'arts': arts})
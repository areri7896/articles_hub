from django.shortcuts import render, get_object_or_404
from .models import Article
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.http import Http404

from . import forms
# Create your views here.
def home(request):
    art_list = Article.objects.all()
    paginator = Paginator(art_list, 6)
    page_number = request.GET.get('page', 1)
    arts = paginator.page(page_number)
    return render(request, 'index.html', {'arts': arts})

def post(request, id):
    # posts = article.objects.get(id=id)
    try:
        post = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404("No Article found.")
    return render (request, 'about.html', {'post': post})

def login(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')
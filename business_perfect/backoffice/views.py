from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, Project
from .forms import ArticleForm, ProjectForm

# Create your views here.
def home(request):
    return render(request, 'backoffice/public/home.html')

def blog(request):
    latest_articles = Article.objects.all().order_by('-id')[:4]
    return render(request, 'backoffice/public/blog.html', {'articles': latest_articles})

def portfolio(request):
    latest_projects = Project.objects.all().order_by('-id')[:15]
    return render(request, 'backoffice/public/portfolio.html', {'projects': latest_projects})

def contact(request):
    return render(request, 'backoffice/public/contact.html')

def admin(request):
    return render(request, 'backoffice/admin/admin_home.html')

def admin_url(request, nom_url):
    form = None
    if nom_url == 'add_article':
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin')
        else:
            form = ArticleForm()
    else:
        if request.method == 'POST':
            form = ProjectForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin')
        else:
            form = ProjectForm()

    return render(request, 'backoffice/admin/add_form.html', {'nom_url': nom_url, 'form': form})


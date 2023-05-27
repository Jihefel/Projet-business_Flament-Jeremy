from django.shortcuts import render
from .models import Article, Project

# Create your views here.
def home(request):
    return render(request, 'backoffice/public/home.html')

def blog(request):
    articles = Article.objects.all()
    return render(request, 'backoffice/public/blog.html', {'articles': articles})

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'backoffice/public/portfolio.html', {'projects': projects})

def contact(request):
    return render(request, 'backoffice/public/contact.html')

def admin(request):
    return render(request, 'backoffice/admin/admin.html')

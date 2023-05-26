from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'backoffice/home.html')

def blog(request):
    return render(request, 'backoffice/blog.html')

def portfolio(request):
    return render(request, 'backoffice/portfolio.html')

def contact(request):
    return render(request, 'backoffice/contact.html')

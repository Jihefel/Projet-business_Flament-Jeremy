"""
URL configuration for azz project.

The  list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backoffice import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_post, name='blog_post'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:post_id>/', views.project_post, name='project_post'),
    path('contact/', views.contact, name='contact'),
    # Admin interface
    path('admin/', views.admin, name='admin'),
    path('admin/<str:nom_url>/', views.admin_url, name='admin_url'),
]

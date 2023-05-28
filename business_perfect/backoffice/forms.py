from django import forms
from .models import Article, Project

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
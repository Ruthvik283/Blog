from django.forms import  ModelForm
from django import forms
from .models import *
class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    return render(request,'accounts/js.html')

def blogs(request):
    form = Blogs.objects.all()
    context = {"form":form}
    return render(request, 'accounts/index.html', context)

def blog(request, pk):
    form = Blogs.objects.get(id=pk)
    context = {"form":form}
    return render(request, 'accounts/index1.html', context)
    
def addblog(request):
    form = BlogForm
    form1 = Blogs.objects.all()
    
    if request.method == 'POST':
        form= BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blogs')
    context = {'form':form,"form1":form1}
    return render(request,'accounts/index3.html',context)
       

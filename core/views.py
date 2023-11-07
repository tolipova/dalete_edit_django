from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def company(request):
    comp = Company.objects.all()
    context = {
        'comp':comp
    }
    return render(request, 'table.html', context)

def add(request):
    form = CompanyForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('company')
    else:
        form = CompanyForm()    
    return render(request, 'add.html', {'form':form})   


def delete(request, id):
    post = Company.objects.get(id=id)
    post.delete()
    return redirect('company')



def edit(request,id):
    post = Company.objects.get(id=id)
    context = {
        'post':post
    }
    return render(request, 'update.html', context)

def editrecord(request,id):
    name = request.POST['name']
    about = request.POST['about']
    logo = request.POST['logo']

    info = Company.objects.get(id=id)
    info.name = name
    info.about = about
    info.logo = logo

    info.save()
    return redirect('company')
    
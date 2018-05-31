from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

@login_required
def top(request):
    user = request.user.username
    people = Person.objects.using(user).all()
    return render(request, 'top.html', {'user':user,'people':people})

@login_required
def add_person(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        user = request.user.username
        name  = request.POST.get('name')
        age   = request.POST.get('age')
        person = Person(name=name, age=age)
        person.save(using=user)
        return redirect('myapp:view_top')

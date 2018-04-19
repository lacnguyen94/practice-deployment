
from django.utils.crypto import get_random_string
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime
from random import randint
from apps.courses.models import *
from django.contrib import messages


def index(request):
    return render(request,'courses/index.html')

def create(request):
    errors = Course.objects.validation(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/process')

def process(request):
    context = {
    'courses': Course.objects.all()
    }
    print(context)
    return render(request, 'courses/index.html',context)

def remove(request,number):
    context = {
    'Course': Course.objects.get(id=number)
    }
    return render(request, 'courses/remove.html',context)

def destroy(request,number):
    Course.objects.get(id=number).delete()
    return redirect('/process')
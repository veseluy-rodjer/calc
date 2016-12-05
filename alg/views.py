# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Solution
from .forms import PostForm, AddForm
import time

# Create your views here.

i = 0
a = time.time()

def process(request):
    global i
    task_ = Solution.objects.all()[i].task
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            got = form.save(commit=False)
            got.task = task_
            got.resh()
            if got.sol == got.answer:
                form = PostForm()
                ans = 'Молодец!'
                i += 1
                if i > (len(Solution.objects.all()) - 1):
                    i = 0
                    return redirect('begin')
                task_ = Solution.objects.all()[i].task
            else:
                ans = 'Да ты двоечник!'
    else:
        form = PostForm()
        ans = ''
    return render(request, 'alg/process.html', {'form':form, 'task_':task_, 'ans':ans})
	
def addd(request):
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddForm()
    return render(request, 'alg/addd.html', {'form':form})

def begin(request):
    return render(request, 'alg/begin.html', {})

def end(request):
    return render(request, 'alg/end.html', {})

b = time.time()
if b - a == 12:
    redirect('end')
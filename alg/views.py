# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Solution
from .forms import PostForm

# Create your views here.

i = 0

def process(request):
    global i
    task_ = Solution.objects.all()[i].task
    if request.POST:
        form = PostForm(request.POST)
        got = form.save(commit=False)
        got.task = task_
        got.resh()
        if got.sol == got.answer:
            ans = 'Молодец!'
            i += 1
            if i > (len(Solution.objects.all()) - 1):
                i = 0
                return redirect('process')
            task_ = Solution.objects.all()[i].task
        else:
            ans = 'Фу-у-у-у!'
    else:
        form = PostForm()
        ans = ''
    return render(request, 'alg/process.html', {'form':form, 'task_':task_, 'ans':ans})
	
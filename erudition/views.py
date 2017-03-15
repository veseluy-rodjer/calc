from django.shortcuts import render, redirect
from .models import Erudmodel
import time
from .forms import Addform

# Create your views here.

i = 0
a = time.time()
counter = 0

def erudition_add(request):
    if request.method == "POST":
        form = Addform(request.POST)
        if form.is_valid():
            form.save()
    form = Addform()
    return render(request, 'erudition/add.html', {'form':form})

def start_erudition(request):
    return render(request, 'erudition/start_erudition.html', {})

def erudition_process1(request):
    global i
    global a
    global counter
    i = 0
    a = time.time()
    counter = 0
    return redirect('erudition_process')

def erudition_process(request):
    return redirect('erudition_process')

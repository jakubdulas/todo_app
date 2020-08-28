from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Task
from django.http import HttpResponseRedirect
from .forms import AddTaskForm
from django.contrib import messages
# Create your views here.

class HomeView(ListView):
    model = Task
    template_name = 'home.html'
    ordering = ['complete', '-important']
    


def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST or None)
        if form.is_valid():
            messages.success(request, ('You added new task successfully!'))
            form.save()
    return redirect('home')


def complete(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        #if task is completed
        if task.complete:
            task.complete = False
            task.save()
        else:
            task.complete = True
            task.save()
    return redirect('home')


def delete(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        task.delete()
        messages.success(request, ('Task: "{}" has been deleted!'.format(task.text)))
    return redirect('home')


def set_as_important(request, pk):
    if request.method == 'POST':
        task = Task.objects.get(pk=pk)
        #if task is important
        if task.important:
            task.important = False
            task.save()
        else:
            task.important = True
            task.save()
    return redirect('home')


        
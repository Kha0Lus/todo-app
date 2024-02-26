from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_task(request):
    tasks = Task.objects.all()
    return render(request, 'todo/list_task.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('list-task')
    return render(request, 'todo/add_task.html')


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('list-task')


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('list-task')

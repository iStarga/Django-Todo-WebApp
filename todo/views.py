from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    if request.method == "POST":
        taskTitle = request.POST["taskTitle"]
        task = Task(title=taskTitle)
        task.save()
        return redirect("/")
    else:
        return render(request, 'todo/index.html', context)


def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        update_task = request.POST["update_task"]
        completed = request.POST.get("task_completed", False)
        if completed == 'on':
            task.complete = True
        else:
            task.title = update_task
        task.save()
        return redirect("/")
    else:
        return render(request, 'todo/update.html', {'task': task})


def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("/")
    else:
        context = {'task': task}
        return render(request, 'todo/delete.html', context)

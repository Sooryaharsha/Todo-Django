
from http.client import HTTPResponse
from django.shortcuts import render
from todos.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('-modified_at')
    completed_tasks = Task.objects.filter(is_completed = True)
    #print(completed_tasks)
    context = {
        'tasks' : tasks,
        'completed_tasks' : completed_tasks,
    }
    return render(request,'home.html',context)
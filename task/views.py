from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
# view to handle home request
def home(request):
    tasks = Task.objects.all()
    return render(request,'index.html',{'tasks': tasks})
# view to add task into db   
def add_task(request):
    task1 = request.POST["task"]
    date1 = request.POST["task-date"]
    tasks = Task(task=task1,date=date1)
    tasks.save()
    return redirect('home')
# view to delete task from database
def delete_task(request,task_id):
    tasks = Task.objects.get(id=task_id)
    tasks.delete()
    return redirect('home')
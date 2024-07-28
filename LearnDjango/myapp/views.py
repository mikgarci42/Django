from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, id):
    print(id)
    return HttpResponse("Hello World %s" % id)

def about(request):
    username = 'mikgarci'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def task(request):
    #task = Task.objects.get(id=id)
    #tasks = Task.objects.all()
    tasks = Task.objects.all()
    return render(request, 'task.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(name=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST["name"])
        print(project)
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
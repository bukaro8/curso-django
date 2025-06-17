"""Views for the myapp application."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Project, Task


def index(request):
    """Render the index page."""
    return render(request, "index.html", {})


def about(request):
    """Render the about page."""
    return render(request, "about.html", {})


def hello(request, username):
    """Greet a user by their username."""
    context = {
        'username': username
    }
    return render(request, "hello.html", context)


def projects(request):
    """Return a JSON list of all projects."""
    projects = list(Project.objects.values())  # Rename variable if needed
    return JsonResponse(projects, safe=False)


def tasks(request, id):  # Rename 'id' to avoid built-in conflict
    """Display tasks for a given task ID."""
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'tasks :{task.title}')

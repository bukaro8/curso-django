"""Views for the myapp application."""
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Project, Task


def index(request):
    """Render the index page."""
    return HttpResponse("Index page")


def hello(request, username):
    """Greet a user by their username."""
    return HttpResponse(f"Hello {username}")


def about(request):
    """Render the about page."""
    return HttpResponse("about")


def projects(request):
    """Return a JSON list of all projects."""
    projects = list(Project.objects.values())  # Rename variable if needed
    return JsonResponse(projects, safe=False)


def tasks(request, id):  # Rename 'id' to avoid built-in conflict
    """Display tasks for a given task ID."""
    # task = Task.objects.get(id=id)
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'tasks :{task.title}')

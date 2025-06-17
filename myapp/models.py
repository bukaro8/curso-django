from django.db import models
from django.db.models import Manager


# Create your models here.


class Project(models.Model):
    """Model to add project with name and id"""
    name = models.CharField(max_length=200)
    objects: Manager = models.Manager()

    def __str__(self):
        return self.name


class Task(models.Model):
    """Model to add task with title,description, id and project_id"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    objects: Manager = models.Manager()

    def __str__(self):
        return f"{self.title} -- {self.project.name}"

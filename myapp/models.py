from django.db import models

# Create your models here.


class Project(models.Model):
    """Model to add project with name and id"""
    name = models.CharField(max_length=200)


class Task(models.Model):
    """Model to add task with title,description, id and project_id"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

from django.db import models
from django.contrib import admin


# Module model
class Module(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"
from django.db import models
from django.contrib import admin


# Module model
class Module(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/",blank=True, null=True)
    def __str__(self):
        return f"{self.name}"

class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.name}"

class TopicAdmin(admin.ModelAdmin):
    list_display = ['module', 'name']
    list_filter = ['module']

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f"{self.email}"
    
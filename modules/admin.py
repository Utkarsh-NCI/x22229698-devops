from django.contrib import admin

# Register your models here.
from .models import Module,Topic
admin.site.register(Module)
admin.site.register(Topic)


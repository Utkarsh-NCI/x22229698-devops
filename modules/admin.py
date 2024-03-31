from django.contrib import admin

# Register your models here.
from .models import Module, Topic, TopicAdmin, Feedback

admin.site.register(Module)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Feedback)

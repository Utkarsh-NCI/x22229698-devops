'"Modules application routes"'
from django.urls import path
from . import views

app_name = "modules"  # pylint: disable=invalid-name
urlpatterns = [
    path("", views.index, name="index"),
    path("module/<int:module_id>/", views.show, name="module"),
    path("feedback/", views.feedback, name="feedback"),
]

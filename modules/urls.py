from django.urls import path
from . import views

app_name='modules'
urlpatterns = [
    path('', views.index, name='index'),
    path('module/<int:module_id>/', views.show, name='module'),
    ]
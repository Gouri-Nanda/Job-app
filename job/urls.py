from django.urls import path

from . import views

app_name='job'


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.admin1, name='upload'),
    path('apply/', views.apply, name='apply'),
]
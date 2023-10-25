from django.urls import path

from .import views

urlpatterns = [

    path('', views.home, name="Home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('courses', views.courses, name="courses")

]
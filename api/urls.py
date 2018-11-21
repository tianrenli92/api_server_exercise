from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('student', views.student_list, name='student_list'),
]

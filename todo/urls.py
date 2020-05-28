from django.urls import path
from .views import *


app_name = 'todo'
urlpatterns = [
	path('', index, name='index'),
	path('delete/<int:pk>', delete_task, name='delete_task'),
	path('update/<int:pk>', update_task, name='update_task'),
]
from django.urls import path
from .views import add_course,update_course,show_course,delete_course
urlpatterns = [
    path('add/',add_course,name='add_url'),
    path('show/',show_course,name='show_url'),
    path('update/<int:pk>/',update_course,name='update_url'),
    path('delete/<int:pk>/',delete_course,name='delete_url')
]
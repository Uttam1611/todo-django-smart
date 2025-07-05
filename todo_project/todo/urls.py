from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

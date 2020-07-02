from django.urls import path
from hierarchical import views

urlpatterns = [
    path('', views.show_files, name='homepage'),
    path('addfiles/', views.add_files)
]
from django.urls import path
from hierarchical import views

urlpatterns = [
    path('', views.show_desserts, name='homepage'),
    path('add/', views.add_dessert)
]
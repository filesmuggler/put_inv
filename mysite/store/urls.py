from django.urls import path
from . import views

urlpatterns = [
    path('',views.part_list, name='part_list'),
    path('part/<int:pk>/', views.part_detail, name='part_detail'),
]
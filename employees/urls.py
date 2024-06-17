from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('new/', views.employee_create, name='employee_new'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('<int:pk>/edit/', views.employee_update, name='employee_edit'),
    path('<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    
]

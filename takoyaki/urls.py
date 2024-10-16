from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name = 'about'),
    path('', views.homepage, name = 'home'),
    path('menu/', views.menu_index, name='menu_index'),  # Read
    path('menu/create/', views.menu_create, name='menu_create'),  # Create
    path('menu/update/<int:menu_id>/', views.menu_update, name='menu_update'),  # Update
    path('menu/delete/<int:menu_id>/', views.menu_delete, name='menu_delete'),  # Delete
]
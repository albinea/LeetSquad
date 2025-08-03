from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    path('', auth_views.LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # Main pages
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-group/', views.create_group, name='create_group'),
    path('join-group/', views.join_group, name='join_group'),
    path('group/<int:group_id>/', views.group_detail, name='group_detail'),
    path('update-stats/', views.update_stats, name='update_stats'),
    
    # API endpoints
    path('api/group/<int:group_id>/members/', views.get_group_members, name='get_group_members'),
]

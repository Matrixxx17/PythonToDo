from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='Home'),
    
    path('login/', views.LoginInterfaceView.as_view(), name='Login'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='Logout'),
    path('signup/', views.SignUpView.as_view(), name='Signup'),

]
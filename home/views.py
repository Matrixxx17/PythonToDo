from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

#Create your views here
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'smart/codesnippets'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('snippet_list')
        return super().get(request, *args, **kwargs)
    
class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
class HomeView(TemplateView):
    template_name = 'home/welcome.html'


    

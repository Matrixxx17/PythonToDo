from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView,ListView, DetailView, UpdateView, DeleteView

import codesnip
from .models import Codesnip
from .form import CodesnipForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# List view
class SnippetDeleteView(LoginRequiredMixin, DeleteView):
    model = Codesnip
    success_url = '/smart/codesnips/'
    template_name = 'codesnips/codesnip_delete.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.codesnip.all()

class SnippetUpdateView(LoginRequiredMixin, UpdateView):
    model = Codesnip
    success_url = '/smart/codesnips/'
    form_class = CodesnipForm
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.codesnip.all()
    


class SnippetListView(LoginRequiredMixin, ListView):
    model = Codesnip
    template_name = 'codesnips/codesnip_list.html'
    context_object_name = 'snip'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.codesnip.all()

# Detail view
class SnippetDetailView(LoginRequiredMixin, DetailView):
    model = Codesnip
    template_name = 'codesnips/codesnip_detail.html'
    context_object_name = 'snippet'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.codesnip.all()



class SnipsCreateView(LoginRequiredMixin, CreateView):
    model = Codesnip
    
    template_name = 'codesnips/codesnip_form.html'
    success_url = '/smart/codesnips/'
    form_class = CodesnipForm
    login_url = "/login"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
# from django.views.generic import ListView, DetailView
# from .models import Codesnip

# # List view
# class SnippetListView(ListView):
#     model = Codesnip
#     template_name = 'codesnips/codesnip_list.html'
#     context_object_name = 'snip'

# # Detail view
# class SnippetDetailView(DetailView):
#     model = Codesnip
#     template_name = 'codesnips/codesnip_detail.html'
#     context_object_name = 'snippet'

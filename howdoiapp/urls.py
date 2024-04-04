from django.urls import path
from . import views

urlpatterns = [
    path('howdoi/', views.howdoi_view, name='howdoi'),
]

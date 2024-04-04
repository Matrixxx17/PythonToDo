from django.urls import path
from . import views

urlpatterns = [
    path('codesnips/', views.SnippetListView.as_view(), name='snippet_list'),
    path('codesnips/<int:pk>', views.SnippetDetailView.as_view(),  name='snippet_detail'),
    path('codesnips/<int:pk>/edit', views.SnippetUpdateView.as_view(),  name='snippet_update'),
    path('codesnips/<int:pk>/delete', views.SnippetDeleteView.as_view(),  name='snippet_delete'),
    path('codesnips/new', views.SnipsCreateView.as_view(),  name='snippet_create')
]

##
# from django.urls import path
# from .views import SnippetListView, SnippetDetailView

# urlpatterns = [
#     path('list/', SnippetListView.as_view(), name='snippet_list'),
#     path('detail/<int:pk>/', SnippetDetailView.as_view(), name='snippet_detail'),
# ]

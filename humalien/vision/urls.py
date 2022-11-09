from django.urls import path, re_path
from . import views
#namespace
app_name = 'vision'
urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('', views.TaskListView.as_view(), name='task_list'),
    #retrive single task object
    re_path(r'^(?P<pk>\d+)/$', views.TaskDetailView.as_view(),name='task_detail'),
            
    re_path(r'^(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(),name='task_update'),
            
    re_path(r'^(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(),name='task_delete'),
]         

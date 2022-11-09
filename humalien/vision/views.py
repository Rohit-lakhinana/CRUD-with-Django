from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse,reverse_lazy
from .models import dmt
from .forms import sony

from django.views.generic import ListView,DetailView,\
     CreateView,UpdateView,DeleteView

class TaskListView(ListView):
   model=dmt
   context_object_name='vision'
   
class TaskDetailView(DetailView):
   model=dmt
class TaskCreateView(CreateView):
   model=dmt
   form_class = sony
   success_url = reverse_lazy('vision:task_list')
   
class TaskUpdateView(UpdateView):
   model=dmt
   form_class = sony
   success_url = reverse_lazy('vision:task_list')

class TaskDeleteView(DeleteView):
   model= dmt
   success_url = reverse_lazy('vision:task_list')
   


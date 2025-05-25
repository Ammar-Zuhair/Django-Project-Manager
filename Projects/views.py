from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from . import forms
from . import models
# Create your views here.
class ProjectListView(ListView):
    model = models.Project
    template_name = 'project/list.html'

class ProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('Project_List')

class ProjectUpdateView(UpdateView):
    model = models.Project
    form_class = forms.ProjectUpdateForm
    template_name = 'project/update.html'
    def get_success_url(self):
        return reverse('Project_Update',args=[self.object.id]) # object here reference to the project

class ProjectDeleteView(DeleteView):
    model = models.Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_List')

class TaskCreateView(CreateView):
    model = models.Task
    fields=['project','description']
    http_method_names = ['post'] #only post requests allowed
    def get_success_url(self):
        return reverse('Project_Update',args=[self.object.project.id]) # object here reference to the project


class TaskUpdateView(UpdateView):
    model = models.Task
    fields=['is_completed']
    http_method_names = ['post'] #only post requests allowed
    def get_success_url(self):
        return reverse('Project_Update',args=[self.object.project.id]) # object here reference to the project


class TaskDeleteView(DeleteView):
    model = models.Task

    def get_success_url(self):
        return reverse('Project_Update',args=[self.object.project.id]) # object here reference to the project

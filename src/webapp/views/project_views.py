from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = '-created_at'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    pk_url_kwarg = 'pk'


class ProjectAddView(CreateView):
    model = Project
    template_name = 'project/project_add.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectEditView(UpdateView):
    model = Project
    template_name = 'project/project_edit.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/project_delete.html'
    success_url = reverse_lazy('projects')



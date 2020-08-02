from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import ProjectForm, SimpleSearchForm
from webapp.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    ordering = '-created_at'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(title__icontains=self.search_value)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issues.order_by('-created_at')
        context['issues'] = issues
        return context


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



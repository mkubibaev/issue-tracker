from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue, Project


class IssueListView(ListView):
    model = Issue
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issue/issue_detail.html'
    pk_url_kwarg = 'pk'


class IssueCreateView(CreateView):
    model = Issue
    template_name = 'issue/issue_add.html'
    form_class = IssueForm

    def form_valid(self, form):
        project_pk = self.kwargs.get('pk')
        project = get_object_or_404(Project, pk=project_pk)
        project.issues.create(**form.cleaned_data)
        return redirect('project_detail', pk=project_pk)


class IssueEditView(UpdateView):
    model = Issue
    template_name = 'issue/issue_edit.html'
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    model = Issue
    template_name = 'issue/issue_delete.html'
    success_url = reverse_lazy('index')

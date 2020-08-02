from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm, SimpleSearchForm
from webapp.models import Issue, Project


class IssueListView(ListView):
    model = Issue
    template_name = 'issue/index.html'
    context_object_name = 'issues'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1

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
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


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

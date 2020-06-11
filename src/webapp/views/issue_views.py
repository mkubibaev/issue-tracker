from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, ListView, DetailView, CreateView

from webapp.forms import IssueForm
from webapp.models import Issue


class IssueListView(ListView):
    template_name = 'issue/index.html'
    model = Issue
    context_object_name = 'issues'
    ordering = ['-created_at']
    paginate_by = 3
    paginate_orphans = 1


class IssueDetailView(DetailView):
    template_name = 'issue/issue_detail.html'
    model = Issue
    pk_url_kwarg = 'pk'


class IssueCreateView(CreateView):
    template_name = 'issue/issue_add.html'
    model = Issue
    form_class = IssueForm

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueEditView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'type': issue.type,
            'status': issue.status
        })
        return render(request, 'issue/issue_edit.html', {'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.type = form.cleaned_data['type']
            issue.status = form.cleaned_data['status']
            issue.save()
            return redirect('issue_detail', pk=issue.pk)
        else:
            return render(request, 'issue/issue_edit.html', {'form': form, 'issue': issue})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return render(request, 'issue/issue_delete.html', {'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        issue.delete()
        return redirect('index')

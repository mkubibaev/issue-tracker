from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import IssueForm, StatusForm, TypeForm
from webapp.models import Issue, Status, Type


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issues = Issue.objects.all()
        context['issues'] = issues
        return context


class IssueDetail(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue_pk = kwargs.get('pk')
        context['issue'] = get_object_or_404(Issue, pk=issue_pk)
        return context


class IssueCreateView(View):
    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, 'issue_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.create(
                summary=form.cleaned_data['summary'],
                description=form.cleaned_data['description'],
                type=form.cleaned_data['type'],
                status=form.cleaned_data['status'],
            )
            return redirect('issue_detail', pk=issue.pk)
        else:
            return render(request, 'issue_add.html', {'form': form})


class IssueEditView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        form = IssueForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'type': issue.type,
            'status': issue.status
        })
        return render(request, 'issue_edit.html', {'form': form, 'issue': issue})

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
            return render(request, 'issue_edit.html', {'form': form, 'issue': issue})


class IssueDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        return render(request, 'issue_delete.html', {'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs.get('pk'))
        issue.delete()
        return redirect('index')


class StatusListView(TemplateView):
    template_name = 'status/status_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statuses = Status.objects.all()
        context['statuses'] = statuses
        return context


class StatusEditView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data={
            'label': status.label
        })
        return render(request, 'status/status_edit.html', {'form': form, 'status': status})

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.label = form.cleaned_data['label']
            status.save()
            return redirect('statuses')
        else:
            return render(request, 'status/status_edit.html', {'form': form})


class StatusAddView(View):
    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, 'status/status_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(data=request.POST)
        if form.is_valid():
            Status.objects.create(label=form.cleaned_data['label'])
            return redirect('statuses')
        else:
            return render(request, 'status/status_add.html', {'form': form})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        return render(request, 'status/status_delete.html', {'status': status})

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs.get('pk'))
        status.delete()
        return redirect('statuses')


class TypeListView(TemplateView):
    template_name = 'type/type_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        types = Type.objects.all()
        context['types'] = types
        return context


class TypeEditView(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data={
            'label': type.label
        })
        return render(request, 'type/type_edit.html', {'form': form, 'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        form = TypeForm(data=request.POST)
        if form.is_valid():
            type.label = form.cleaned_data['label']
            type.save()
            return redirect('types')
        else:
            return render(request, 'type/type_edit.html', {'form': form})


class TypeAddView(View):
    def get(self, request, *args, **kwargs):
        form = TypeForm()
        return render(request, 'type/type_add.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TypeForm(data=request.POST)
        if form.is_valid():
            Type.objects.create(label=form.cleaned_data['label'])
            return redirect('types')
        else:
            return render(request, 'type/type_add.html', {'form': form})


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        return render(request, 'type/type_delete.html', {'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('types')

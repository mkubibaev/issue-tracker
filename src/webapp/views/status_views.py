from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import StatusForm
from webapp.models import Status


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

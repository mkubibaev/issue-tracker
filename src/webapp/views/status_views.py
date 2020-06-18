from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from webapp.forms import StatusForm
from webapp.models import Status


class StatusListView(ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'


class StatusAddView(CreateView):
    model = Status
    template_name = 'status/status_add.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('statuses')


class StatusEditView(UpdateView):
    model = Status
    template_name = 'status/status_edit.html'
    form_class = StatusForm

    def get_success_url(self):
        return reverse('statuses')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/status_delete.html'
    success_url = reverse_lazy('statuses')

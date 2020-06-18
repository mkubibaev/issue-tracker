from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from webapp.forms import TypeForm
from webapp.models import Type


class TypeListView(ListView):
    template_name = 'type/type_list.html'
    model = Type
    context_object_name = 'types'


class TypeAddView(CreateView):
    template_name = 'type/type_add.html'
    model = Type
    form_class = TypeForm

    def get_success_url(self):
        return reverse('types')


class TypeEditView(UpdateView):
    model = Type
    template_name = 'type/type_edit.html'
    form_class = TypeForm

    def get_success_url(self):
        return reverse('types')


class TypeDeleteView(DeleteView):
    model = Type
    template_name = 'type/type_delete.html'
    success_url = reverse_lazy('types')

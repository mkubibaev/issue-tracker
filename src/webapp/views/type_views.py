from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View, CreateView, ListView

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


class TypeDeleteView(View):
    def get(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        return render(request, 'type/type_delete.html', {'type': type})

    def post(self, request, *args, **kwargs):
        type = get_object_or_404(Type, pk=kwargs.get('pk'))
        type.delete()
        return redirect('types')

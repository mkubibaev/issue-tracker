from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from webapp.forms import TypeForm
from webapp.models import Type


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

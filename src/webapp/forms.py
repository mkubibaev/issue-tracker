from django import forms
from django.forms import widgets

from webapp.models import Status, Type, Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['label']


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['label']

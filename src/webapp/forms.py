from django import forms
from django.forms import widgets

from webapp.models import Status, Type, Issue, Project


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


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

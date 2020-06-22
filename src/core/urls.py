"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import IssueListView, IssueDetailView, IssueCreateView, IssueEditView, IssueDeleteView, \
    StatusListView, StatusEditView, StatusAddView, StatusDeleteView, \
    TypeListView, TypeEditView, TypeAddView, TypeDeleteView, \
    ProjectListView, ProjectAddView, ProjectDetailView, ProjectEditView, ProjectDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='index'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issue_detail'),
    path('issues/add', IssueCreateView.as_view(), name='issue_add'),
    path('issues/<int:pk>/edit', IssueEditView.as_view(), name='issue_edit'),
    path('issues/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete'),
    path('statuses', StatusListView.as_view(), name='statuses'),
    path('statuses/add', StatusAddView.as_view(), name='status_add'),
    path('statuses/<int:pk>/edit', StatusEditView.as_view(), name='status_edit'),
    path('statuses/<int:pk>/delete', StatusDeleteView.as_view(), name='status_delete'),
    path('types', TypeListView.as_view(), name='types'),
    path('types/add', TypeAddView.as_view(), name='type_add'),
    path('types/<int:pk>/edit', TypeEditView.as_view(), name='type_edit'),
    path('types/<int:pk>/delete', TypeDeleteView.as_view(), name='type_delete'),
    path('projects', ProjectListView.as_view(), name='projects'),
    path('projects/add', ProjectAddView.as_view(), name='project_add'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit', ProjectEditView.as_view(), name='project_edit'),
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),

    path('admin/', admin.site.urls),
]

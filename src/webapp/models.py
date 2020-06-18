from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Summary')
    description = models.TextField(max_length=2000, verbose_name='Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    status = models.ForeignKey('webapp.Status', related_name='issues', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey('webapp.Type', related_name='issues', on_delete=models.PROTECT, verbose_name='Type')
    project = models.ForeignKey('webapp.Project', related_name='issues', on_delete=models.PROTECT,
                                verbose_name='Project')

    def __str__(self):
        return self.summary


class Status(models.Model):
    label = models.CharField(max_length=40, verbose_name='Status')

    def __str__(self):
        return self.label


class Type(models.Model):
    label = models.CharField(max_length=40, verbose_name='Type')

    def __str__(self):
        return self.label


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=4000, verbose_name='Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')

    def __str__(self):
        return self.title

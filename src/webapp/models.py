from django.db import models


class Issue(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Summary')
    description = models.TextField(max_length=2000, verbose_name='Description', null=True, blank=True)
    status = models.ForeignKey('webapp.Status', related_name='status', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey('webapp.Type', related_name='type', on_delete=models.PROTECT, verbose_name='Type')

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

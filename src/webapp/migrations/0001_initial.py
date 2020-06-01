# Generated by Django 3.0.6 on 2020-06-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Summary')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.Status', verbose_name='Status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.Type', verbose_name='Type')),
            ],
        ),
    ]

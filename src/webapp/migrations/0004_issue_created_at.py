# Generated by Django 3.0.6 on 2020-06-02 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200601_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2020-01-01', verbose_name='Created at'),
            preserve_default=False,
        ),
    ]

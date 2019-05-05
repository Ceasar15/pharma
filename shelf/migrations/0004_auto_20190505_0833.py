# Generated by Django 2.2 on 2019-05-05 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20190503_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='groupsale',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

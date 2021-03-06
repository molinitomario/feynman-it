# Generated by Django 3.2.6 on 2021-08-11 20:48

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='step_one_iterations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='note',
            name='step_three',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='note',
            name='step_two_iterations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='note',
            name='understand',
            field=models.BooleanField(default=False),
        ),
    ]

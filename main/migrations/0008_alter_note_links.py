# Generated by Django 3.2.6 on 2021-08-13 18:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_note_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True), default=list, size=3), blank=True, default=list, size=None),
        ),
    ]

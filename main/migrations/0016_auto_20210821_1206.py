# Generated by Django 3.2.6 on 2021-08-21 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_iteration_general'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iteration',
            name='general',
        ),
        migrations.AddField(
            model_name='link',
            name='general',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='general_links', to='main.note'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-16 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_subject_folder'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folder_notes', to='main.folder'),
        ),
    ]

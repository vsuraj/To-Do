# Generated by Django 4.1.2 on 2022-10-22 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0005_alter_add_task_created_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_task',
            new_name='task',
        ),
    ]
# Generated by Django 3.2.8 on 2022-03-31 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizoApp', '0022_alter_quiz_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
    ]
# Generated by Django 3.2.8 on 2022-03-12 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizoApp', '0009_question_difficultylevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
    ]

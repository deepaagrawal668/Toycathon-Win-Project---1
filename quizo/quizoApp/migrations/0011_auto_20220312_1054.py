# Generated by Django 3.2.8 on 2022-03-12 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizoApp', '0010_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]

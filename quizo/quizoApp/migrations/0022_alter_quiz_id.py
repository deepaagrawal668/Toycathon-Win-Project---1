# Generated by Django 3.2.8 on 2022-03-31 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizoApp', '0021_quiz_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.1.7 on 2021-10-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='question1',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='name',
            name='question2',
            field=models.CharField(default=None, max_length=50),
        ),
    ]

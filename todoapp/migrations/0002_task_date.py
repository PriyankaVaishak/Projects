# Generated by Django 4.1.4 on 2023-01-01 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2012-02-22'),
            preserve_default=False,
        ),
    ]

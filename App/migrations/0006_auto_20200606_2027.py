# Generated by Django 2.2.7 on 2020-06-06 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_memorial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorial',
            name='overview',
            field=models.TextField(max_length=200),
        ),
    ]

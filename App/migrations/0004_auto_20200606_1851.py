# Generated by Django 2.2.7 on 2020-06-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_condetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condetails',
            name='our_current_number',
            field=models.CharField(max_length=16),
        ),
    ]

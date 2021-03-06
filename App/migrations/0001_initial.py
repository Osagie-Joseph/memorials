# Generated by Django 2.2.7 on 2020-06-06 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=16)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'People contacting us',
            },
        ),
    ]

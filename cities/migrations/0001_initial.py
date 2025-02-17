# Generated by Django 3.1.3 on 2024-10-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='City')),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['name'],
            },
        ),
    ]

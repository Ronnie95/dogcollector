# Generated by Django 4.2.2 on 2023-07-08 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(max_length=250)),
                ('img', models.CharField(max_length=250)),
                ('life_expectancy', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['breed'],
            },
        ),
    ]

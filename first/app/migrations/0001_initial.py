# Generated by Django 4.0.1 on 2022-01-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('chemistry', models.CharField(max_length=30)),
                ('physics', models.CharField(max_length=30)),
                ('maths', models.CharField(max_length=30)),
                ('english', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]
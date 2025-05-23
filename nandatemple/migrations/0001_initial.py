# Generated by Django 5.1.5 on 2025-03-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=500)),
                ('gender', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('total_person', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

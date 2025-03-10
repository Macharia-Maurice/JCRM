# Generated by Django 5.1.6 on 2025-02-20 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('leader', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='ministries/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MinistryMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('ministry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='ministries.ministry')),
            ],
        ),
    ]

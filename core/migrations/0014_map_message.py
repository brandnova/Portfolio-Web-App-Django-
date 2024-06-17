# Generated by Django 4.2.7 on 2024-06-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_contacts_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('iFrame_link', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Map',
                'ordering': ('location',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ('name',),
            },
        ),
    ]

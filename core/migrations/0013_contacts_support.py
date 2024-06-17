# Generated by Django 4.2.7 on 2024-06-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_socials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Contact list',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(null=True, upload_to='pageFiles/supportimages')),
            ],
            options={
                'verbose_name_plural': 'Support Images',
                'ordering': ('name',),
            },
        ),
    ]

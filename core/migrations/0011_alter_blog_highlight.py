# Generated by Django 4.2.7 on 2024-06-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='highlight',
            field=models.CharField(max_length=500),
        ),
    ]
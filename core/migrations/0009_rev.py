# Generated by Django 4.2.7 on 2024-06-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_cta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('comment', models.TextField()),
                ('img', models.ImageField(blank=True, null=True, upload_to='pageFiles/reviweimages')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'ordering': ('name',),
            },
        ),
    ]

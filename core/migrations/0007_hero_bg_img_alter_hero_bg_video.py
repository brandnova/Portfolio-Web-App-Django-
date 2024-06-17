# Generated by Django 4.2.7 on 2024-06-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_faq_showcase'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='bg_img',
            field=models.ImageField(blank=True, null=True, upload_to='pageFiles/images'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='bg_video',
            field=models.FileField(blank=True, null=True, upload_to='pageFiles/Videos'),
        ),
    ]
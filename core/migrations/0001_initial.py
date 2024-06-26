# Generated by Django 4.2.7 on 2024-05-17 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ab_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pageFiles/images')),
            ],
        ),
        migrations.CreateModel(
            name='Ab_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_title', models.CharField(max_length=255)),
                ('hero_content', models.CharField(max_length=255)),
                ('button_url', models.CharField(max_length=255)),
                ('bg_video', models.FileField(blank=True, upload_to='pageFiles/Videos')),
            ],
            options={
                'verbose_name_plural': 'Hero Content',
                'ordering': ('hero_title',),
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=255)),
                ('ab_img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='core.ab_img')),
                ('ab_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Feat', to='core.ab_list')),
            ],
        ),
    ]

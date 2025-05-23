# Generated by Django 5.1.4 on 2025-05-13 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_collaboration_multtiple_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.project')),
            ],
        ),
    ]

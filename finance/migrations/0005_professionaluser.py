# Generated by Django 5.0.6 on 2024-07-12 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessionalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('avaliability', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
                ('social_media', models.URLField(blank=True)),
                ('certifications', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

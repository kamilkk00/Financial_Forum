# Generated by Django 5.0.6 on 2024-07-14 20:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_alter_like_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('if_save', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save', to='finance.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

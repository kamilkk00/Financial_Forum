# Generated by Django 5.0.6 on 2024-07-16 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0013_remove_user_is_professional'),
    ]

    operations = [
        migrations.AddField(
            model_name='professionaluser',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0025_rating_user_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('zakladanie_firmy', 'Company Formation'), ('finance_inwestycje', 'Finance and Investments'), ('marketing_sprzedaz', 'Marketing and Sales'), ('zarządzanie_operacje', 'Management and Operations'), ('prawo_regulacje', 'Law and Regulations'), ('rozwoj_osobisty', 'Personal Development and Networking'), ('inne', 'Others')], default='inne', max_length=50),
        ),
    ]

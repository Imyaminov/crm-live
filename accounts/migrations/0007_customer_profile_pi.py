# Generated by Django 4.0.4 on 2022-06-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pi',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

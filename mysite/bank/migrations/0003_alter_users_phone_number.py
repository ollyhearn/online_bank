# Generated by Django 4.1.3 on 2022-11-26 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_alter_users_amount_of_funds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]

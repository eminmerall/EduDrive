# Generated by Django 3.2.7 on 2024-01-05 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='Account'),
        ),
    ]

# Generated by Django 3.2.7 on 2023-12-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0011_auto_20231216_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_cover',
            field=models.ImageField(default=1, upload_to='Drive', verbose_name='Dosya Resmi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.ImageField(upload_to='Drive', verbose_name='Dosya Adı'),
        ),
    ]
# Generated by Django 3.2.7 on 2023-12-30 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0025_auto_20231230_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_cover',
            field=models.ImageField(blank=True, null=True, upload_to='Drive', verbose_name='Dosya Resmi'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.FileField(blank=True, null=True, upload_to='Drive', verbose_name='Dosya'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Dosya Başlığı'),
        ),
    ]

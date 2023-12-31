# Generated by Django 3.2.7 on 2023-12-09 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0002_alter_outhor_biography'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Owner',
            new_name='User',
        ),
        migrations.AlterModelOptions(
            name='file',
            options={'verbose_name': 'Dosya', 'verbose_name_plural': 'Dosyalar'},
        ),
        migrations.AlterModelOptions(
            name='outhor',
            options={'verbose_name': 'Yazar', 'verbose_name_plural': 'Yazarlar'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Sahip', 'verbose_name_plural': 'Dosyalar'},
        ),
        migrations.AlterField(
            model_name='file',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.MinLengthValidator(15)], verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(max_length=200, verbose_name='Dosya Adı'),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Başlık'),
        ),
    ]

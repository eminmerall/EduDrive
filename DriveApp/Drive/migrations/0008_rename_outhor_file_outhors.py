# Generated by Django 3.2.7 on 2023-12-14 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0007_auto_20231214_2313'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='outhor',
            new_name='outhors',
        ),
    ]
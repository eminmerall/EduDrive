# Generated by Django 3.2.7 on 2023-12-14 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0008_rename_outhor_file_outhors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='outhors',
        ),
        migrations.AddField(
            model_name='file',
            name='outhor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Drive.outhor'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.7 on 2023-12-16 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0013_alter_file_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('text', models.TextField(max_length=500)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commets', to='Drive.file')),
            ],
        ),
    ]

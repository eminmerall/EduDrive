# Generated by Django 3.2.7 on 2023-12-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Drive', '0003_auto_20231209_2338'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'İletişim', 'verbose_name_plural': 'İletişimler'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Bölüm', 'verbose_name_plural': 'Bölümler'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Ders', 'verbose_name_plural': 'Dersler'},
        ),
        migrations.AlterModelOptions(
            name='scholl',
            options={'verbose_name': 'Okul', 'verbose_name_plural': 'Okullar'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Kullanıcı', 'verbose_name_plural': 'Kullanıcılar'},
        ),
        migrations.AddField(
            model_name='file',
            name='is_active',
            field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name='file',
            name='is_home',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='adress',
            field=models.CharField(max_length=400, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Posta'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone1',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon 1'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon 2'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Bölüm(Departman) Adı'),
        ),
        migrations.AlterField(
            model_name='file',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Yüklenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_cover',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dosya Resmi'),
        ),
        migrations.AlterField(
            model_name='file',
            name='language',
            field=models.CharField(max_length=100, verbose_name='Dil'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Ders Adı'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='biography',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Özgeçmiş'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='gender',
            field=models.CharField(choices=[('M', 'Erkek'), ('F', 'Kadin')], max_length=1, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='image_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Profil Resmi'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Soyadı'),
        ),
        migrations.AlterField(
            model_name='outhor',
            name='title_type',
            field=models.CharField(choices=[('1', 'Profesör'), ('2', 'Doçent'), ('3', 'Doktor'), ('4', 'Öğretim Görevlisi'), ('5', 'Araştirma Görevlisi'), ('6', 'Öğretmen'), ('7', 'Yazar'), ('8', 'Araştirmaci'), ('9', 'Üye')], max_length=1, verbose_name='Ünvan'),
        ),
        migrations.AlterField(
            model_name='scholl',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Okul(Üniversite) Adı'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Adı'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Erkek'), ('F', 'Kadin')], max_length=1, null=True, verbose_name='Cinsiyet'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Profil Resmi'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Soyadı'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, verbose_name='Kullanıcı Adı'),
        ),
    ]

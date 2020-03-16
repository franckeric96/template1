# Generated by Django 2.2.10 on 2020-03-14 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceuil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('icon', models.CharField(choices=[('Vimeo', 'fa-vimeo'), ('Facebook', 'fa-facebook'), ('twitter', 'fa-twitter'), ('Google-plus', 'fa-google-plus'), ('Instagram', 'fa-instagram')], max_length=20)),
                ('image', models.ImageField(upload_to='images/Acceuil')),
                ('description', models.TextField()),
                ('lien', models.URLField()),
                ('new', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Acceuil',
                'verbose_name_plural': 'Acceuils',
            },
        ),
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('site_map', models.URLField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Localisation',
                'verbose_name_plural': 'Localisations',
            },
        ),
    ]
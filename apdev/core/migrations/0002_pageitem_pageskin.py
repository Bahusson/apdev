# Generated by Django 3.0.3 on 2020-02-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pageitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang_flag', models.ImageField(upload_to='images')),
                ('headtitle', models.CharField(max_length=200)),
                ('mainpage', models.CharField(max_length=200)),
                ('aboutus', models.CharField(max_length=200)),
                ('offer', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('gallery', models.CharField(max_length=200)),
                ('main_intro', models.TextField()),
                ('about_intro', models.TextField()),
                ('save_time', models.CharField(max_length=200)),
                ('design', models.CharField(max_length=200)),
                ('credit', models.CharField(max_length=200)),
                ('management', models.CharField(max_length=200)),
                ('remodelling', models.CharField(max_length=200)),
                ('cookie_alert', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PageSkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('themetitle', models.CharField(max_length=200)),
                ('position', models.IntegerField()),
                ('offerimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('infoimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('serviceimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('fileimagedefault', models.ImageField(blank=True, null=True, upload_to='skins')),
                ('logo_main', models.ImageField(blank=True, null=True, upload_to='skins')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]

# Generated by Django 3.2.15 on 2022-09-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='img',
            field=models.ImageField(default='bing', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
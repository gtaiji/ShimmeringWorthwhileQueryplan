# Generated by Django 3.1 on 2020-09-08 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
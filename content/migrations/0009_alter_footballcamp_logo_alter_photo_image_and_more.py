# Generated by Django 4.2.7 on 2023-12-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_footballcamp_logo_tournaments_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballcamp',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/static/content/images'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='content/static/content/images'),
        ),
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/static/content/images'),
        ),
        migrations.AlterField(
            model_name='tournaments',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/static/content/images'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_standing_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/images/logo'),
        ),
    ]

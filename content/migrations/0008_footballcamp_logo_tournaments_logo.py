# Generated by Django 4.2.7 on 2023-12-05 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_contact_footballcamp_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='footballcamp',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/static/content/images/FootballCamps'),
        ),
        migrations.AddField(
            model_name='tournaments',
            name='logo',
            field=models.ImageField(null=True, upload_to='content/static/content/images/Tournaments'),
        ),
    ]
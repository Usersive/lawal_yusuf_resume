# Generated by Django 3.2 on 2024-02-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvitae', '0007_auto_20240221_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profileupdate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

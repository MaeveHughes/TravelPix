# Generated by Django 3.2 on 2022-01-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolog', '0010_auto_20220120_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
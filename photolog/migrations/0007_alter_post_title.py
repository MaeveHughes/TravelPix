# Generated by Django 3.2 on 2022-01-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photolog', '0006_alter_post_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]

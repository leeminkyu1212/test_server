# Generated by Django 3.2.16 on 2022-11-09 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postdata', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='media/default_image.csv', upload_to=''),
        ),
    ]

# Generated by Django 3.2.9 on 2021-11-14 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, upload_to='post/comment/'),
        ),
    ]

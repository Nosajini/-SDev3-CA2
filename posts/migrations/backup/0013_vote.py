# Generated by Django 3.2.9 on 2021-12-13 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('posts', '0012_alter_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='None', max_length=255)),
                ('votes', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postvote_category', to='shop.category')),
            ],
            options={
                'verbose_name_plural': 'votes',
                'ordering': ('date',),
            },
        ),
    ]

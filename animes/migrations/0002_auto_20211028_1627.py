# Generated by Django 3.2.8 on 2021-10-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='img',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='anime',
            name='mal_id',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

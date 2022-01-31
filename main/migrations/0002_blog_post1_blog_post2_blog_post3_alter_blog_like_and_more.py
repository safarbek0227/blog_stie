# Generated by Django 4.0 on 2022-01-31 02:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post1',
            field=models.TextField(default=datetime.datetime(2022, 1, 31, 2, 42, 37, 493034, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='post2',
            field=models.TextField(default=datetime.datetime(2022, 1, 31, 2, 42, 42, 765249, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='post3',
            field=models.TextField(default=datetime.datetime(2022, 1, 31, 2, 42, 46, 901470, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post',
            field=models.TextField(),
        ),
    ]

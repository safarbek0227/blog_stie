# Generated by Django 4.0.2 on 2022-02-08 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_generalcomment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeneralComment',
            new_name='Contact',
        ),
    ]
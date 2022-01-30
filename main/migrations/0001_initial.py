# Generated by Django 4.0 on 2022-01-30 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='category')),
                ('slug', models.SlugField(verbose_name='*')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='Title:')),
                ('slug', models.SlugField(max_length=25, verbose_name='*')),
                ('post', models.CharField(max_length=80, verbose_name='Post:')),
                ('image', models.ImageField(upload_to='post/', verbose_name='Post image')),
                ('like', models.PositiveIntegerField()),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tag')),
            ],
        ),
    ]
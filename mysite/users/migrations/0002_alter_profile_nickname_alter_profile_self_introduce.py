# Generated by Django 4.2.4 on 2023-08-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='default_nickname', max_length=60),
        ),
        migrations.AlterField(
            model_name='profile',
            name='self_introduce',
            field=models.TextField(default='Hello world!'),
        ),
    ]
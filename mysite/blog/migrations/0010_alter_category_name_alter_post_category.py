# Generated by Django 4.2.4 on 2023-08-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('workouts', '운동'), ('diary', '다이어리'), ('travel', '여행'), ('uncategorized', '미분류')], default='uncategorized', max_length=15),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-24 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('workouts', '운동'), ('diary', '다이어리'), ('travel', '여행'), ('uncategorized', '미분류')], max_length=15),
        ),
    ]

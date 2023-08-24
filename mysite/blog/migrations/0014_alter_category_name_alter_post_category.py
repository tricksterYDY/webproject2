# Generated by Django 4.2.4 on 2023-08-24 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('diary', 'diary'), ('travel', 'travel'), ('workouts', 'workouts')], max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('diary', 'diary'), ('travel', 'travel'), ('workouts', 'workouts')], default='uncategorized', max_length=15),
        ),
    ]

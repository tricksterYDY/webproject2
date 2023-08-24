# Generated by Django 4.2.4 on 2023-08-24 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('workouts', 'workouts'), ('diary', 'diary'), ('travel', 'travel'), ('uncategorized', 'uncategorized')], max_length=15),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(choices=[('workouts', 'workouts'), ('diary', 'diary'), ('travel', 'travel'), ('uncategorized', 'uncategorized')], default='uncategorized', on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]

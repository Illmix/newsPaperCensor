# Generated by Django 4.0.6 on 2022-08-01 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_comment_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='user_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='NE', on_delete=django.db.models.deletion.CASCADE, to='news.author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]

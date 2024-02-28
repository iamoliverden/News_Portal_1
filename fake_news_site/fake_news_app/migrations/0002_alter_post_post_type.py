# Generated by Django 5.0.2 on 2024-02-27 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_news_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('A', 'article'), ('N', 'news')], default='A', max_length=16),
        ),
    ]
# Generated by Django 3.2.12 on 2022-04-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_article_publish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='publish',
        ),
    ]

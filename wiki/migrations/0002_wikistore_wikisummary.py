# Generated by Django 2.0.1 on 2018-06-01 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikistore',
            name='wikisummary',
            field=models.CharField(default='', max_length=400),
        ),
    ]

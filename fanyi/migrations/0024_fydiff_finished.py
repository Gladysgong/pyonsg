# Generated by Django 2.0.1 on 2018-07-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0023_auto_20180709_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='fydiff',
            name='finished',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.0.1 on 2018-07-09 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0021_auto_20180709_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diffcontent',
            name='status',
        ),
    ]

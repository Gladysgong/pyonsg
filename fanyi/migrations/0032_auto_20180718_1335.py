# Generated by Django 2.0.1 on 2018-07-18 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0031_auto_20180716_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fyxmldiff',
            old_name='queyruser',
            new_name='queryuser',
        ),
    ]

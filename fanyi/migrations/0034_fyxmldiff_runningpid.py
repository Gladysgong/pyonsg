# Generated by Django 2.0.1 on 2018-07-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0033_auto_20180718_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='fyxmldiff',
            name='runningPID',
            field=models.CharField(default='', max_length=20),
        ),
    ]
# Generated by Django 2.0.1 on 2018-05-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0015_host_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='runningPID',
            field=models.CharField(default='', max_length=20),
        ),
    ]
# Generated by Django 2.0.1 on 2018-07-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0024_fydiff_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='fydiff',
            name='diffnum',
            field=models.IntegerField(default=0),
        ),
    ]

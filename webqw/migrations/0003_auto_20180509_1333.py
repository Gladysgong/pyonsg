# Generated by Django 2.0.1 on 2018-05-09 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webqw', '0002_auto_20180429_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='webqwqps',
            name='press_expid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webqwqps',
            name='press_rate',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webqwqps',
            name='testtag',
            field=models.CharField(default='', max_length=500),
        ),
    ]

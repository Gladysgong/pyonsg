# Generated by Django 2.0.1 on 2018-05-02 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webqo', '0004_webqoqps_press_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='webqoqps',
            name='press_expid',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='webqoqps',
            name='press_rate',
            field=models.IntegerField(),
        ),
    ]

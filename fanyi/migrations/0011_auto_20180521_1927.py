# Generated by Django 2.0.1 on 2018-05-21 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0010_bbk_req_info_fy_monitor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bbk_req_info',
            name='user_fk',
        ),
        migrations.DeleteModel(
            name='Bbk_req_Info',
        ),
    ]
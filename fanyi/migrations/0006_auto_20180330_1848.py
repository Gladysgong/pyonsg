# Generated by Django 2.0.1 on 2018-03-30 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0005_reqinfo_c_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_email',
            new_name='user_name',
        ),
    ]

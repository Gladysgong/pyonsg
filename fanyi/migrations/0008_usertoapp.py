# Generated by Django 2.0.1 on 2018-04-06 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0007_auto_20180406_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanyi.Application')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanyi.UserInfo', to_field='user_name')),
            ],
        ),
    ]

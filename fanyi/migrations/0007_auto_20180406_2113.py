# Generated by Django 2.0.1 on 2018-04-06 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0006_auto_20180330_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reqinfo',
            name='user_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanyi.UserInfo', to_field='user_name'),
        ),
    ]
# Generated by Django 2.0.1 on 2018-07-18 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0032_auto_20180718_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xmldiffcontent',
            name='diff_task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanyi.FyXmlDiff'),
        ),
    ]

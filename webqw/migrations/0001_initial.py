# Generated by Django 2.0.1 on 2018-04-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='webqwqps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(default='', max_length=50)),
                ('start_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('step', models.IntegerField(default=-1)),
                ('testitem', models.IntegerField(default=0)),
                ('newdataip', models.CharField(default='', max_length=500)),
                ('newdatauser', models.CharField(default='', max_length=500)),
                ('newdatapassw', models.CharField(default='', max_length=500)),
                ('newdatapath', models.CharField(default='', max_length=500)),
                ('newdata_topath', models.CharField(default='', max_length=500)),
                ('newconfip', models.CharField(default='', max_length=500)),
                ('newconfuser', models.CharField(default='', max_length=500)),
                ('newconfpassw', models.CharField(default='', max_length=500)),
                ('newconfpath', models.CharField(default='', max_length=500)),
                ('runningIP', models.CharField(default='', max_length=50)),
                ('testsvn', models.TextField(default='')),
                ('basesvn', models.TextField(default='')),
                ('errorlog', models.TextField(default='')),
                ('cost_test', models.TextField(default='')),
                ('cost_base', models.TextField(default='')),
                ('just_run_test', models.BooleanField(default=False)),
                ('just_run_base', models.BooleanField(default=False)),
                ('press_qps', models.IntegerField()),
                ('press_time', models.IntegerField()),
            ],
        ),
    ]

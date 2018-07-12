# Generated by Django 2.0.1 on 2018-06-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0016_host_runningpid'),
    ]

    operations = [
        migrations.CreateModel(
            name='FyDiff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(default='', max_length=50)),
                ('start_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('hubcfgip', models.CharField(default='', max_length=500)),
                ('hubcfguser', models.CharField(default='', max_length=500)),
                ('hubcfgpassw', models.CharField(default='', max_length=500)),
                ('hubcfgpath', models.CharField(default='', max_length=500)),
                ('hubdatapath', models.CharField(default='', max_length=500)),
                ('sercfgip', models.CharField(default='', max_length=500)),
                ('sercfguser', models.CharField(default='', max_length=500)),
                ('sercfgpassw', models.CharField(default='', max_length=500)),
                ('sercfgpath', models.CharField(default='', max_length=500)),
                ('serdatapath', models.CharField(default='', max_length=500)),
                ('runningIP', models.CharField(default='', max_length=50)),
                ('hubsvn', models.TextField(default='')),
                ('sersvn', models.TextField(default='')),
                ('errorlog', models.TextField(default='')),
                ('testtag', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
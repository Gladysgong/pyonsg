# Generated by Django 2.0.1 on 2018-08-03 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0035_remove_fyxmldiff_create_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBleu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('test_url', models.CharField(default='', max_length=500)),
                ('base_url', models.CharField(default='', max_length=500)),
                ('user', models.CharField(max_length=50)),
                ('queryip', models.CharField(default='', max_length=500)),
                ('queryuser', models.CharField(default='', max_length=500)),
                ('querypassw', models.CharField(default='', max_length=500)),
                ('querypath', models.CharField(default='', max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('errorlog', models.TextField(default='')),
                ('testtag', models.CharField(default='', max_length=500)),
                ('finished', models.IntegerField(default=0)),
                ('diffnum', models.IntegerField(default=0)),
                ('runningPID', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='host',
            name='gpuid',
            field=models.IntegerField(default=0),
        ),
    ]

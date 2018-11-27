# Generated by Django 2.0 on 2018-11-27 10:58

import datetime
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20181019_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresses',
            name='add_time',
        ),
        migrations.AddField(
            model_name='addresses',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='creator',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='delete_flag',
            field=models.BooleanField(default=True, verbose_name='有效标识'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='modify',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='transaction_id',
            field=models.BigIntegerField(default=1, verbose_name='事务ID'),
        ),
        migrations.AddField(
            model_name='addresses',
            name='version',
            field=models.IntegerField(default=1, verbose_name='版本号'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='address_detail',
            field=models.CharField(default='详细地址', max_length=100, verbose_name='详细地址'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='city',
            field=models.CharField(default='beijing', max_length=100, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='district',
            field=models.CharField(default='dongcheng', max_length=100, verbose_name='区域'),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='province',
            field=models.CharField(default='beijing', max_length=100, verbose_name='省份'),
        ),
    ]

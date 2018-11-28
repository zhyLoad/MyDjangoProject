# Generated by Django 2.0 on 2018-11-27 10:58

import datetime
from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('system_manage', '0002_auto_20181126_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='manager',
            name='creator',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='manager',
            name='delete_flag',
            field=models.BooleanField(default=True, verbose_name='有效标识'),
        ),
        migrations.AddField(
            model_name='manager',
            name='modify',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='manager',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='manager',
            name='transaction_id',
            field=models.BigIntegerField(default=1, verbose_name='事务ID'),
        ),
        migrations.AddField(
            model_name='manager',
            name='version',
            field=models.IntegerField(default=1, verbose_name='版本号'),
        ),
        migrations.AddField(
            model_name='organization',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='organization',
            name='delete_flag',
            field=models.BooleanField(default=True, verbose_name='有效标识'),
        ),
        migrations.AddField(
            model_name='organization',
            name='modify',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='organization',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='organization',
            name='transaction_id',
            field=models.BigIntegerField(default=1, verbose_name='事务ID'),
        ),
        migrations.AddField(
            model_name='organization',
            name='version',
            field=models.IntegerField(default=1, verbose_name='版本号'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='creator',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='delete_flag',
            field=models.BooleanField(default=True, verbose_name='有效标识'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='modify',
            field=models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='modify_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='transaction_id',
            field=models.BigIntegerField(default=1, verbose_name='事务ID'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='version',
            field=models.IntegerField(default=1, verbose_name='版本号'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='管理员名称'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='机构名称'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, verbose_name='租户邮箱'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='租户名称'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='租户电话'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, '可用'), (2, '冻结')], default=1, verbose_name='租户状态'),
        ),
    ]
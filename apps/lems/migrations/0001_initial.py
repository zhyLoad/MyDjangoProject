# Generated by Django 2.0 on 2018-12-25 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system_manage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('creator', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('modify', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者')),
                ('transaction_id', models.BigIntegerField(default=1, verbose_name='事务ID')),
                ('version', models.IntegerField(default=1, verbose_name='版本号')),
                ('category_picture_type', models.IntegerField(blank=True, choices=[(0, '图标'), (1, '海报')], default=0, verbose_name='目录图片类型')),
                ('file', models.FileField(blank=True, null=True, upload_to='.', verbose_name='文件')),
                ('delete_flag', models.BooleanField(default=True, verbose_name='有效标识')),
            ],
            options={
                'verbose_name': '目录图片资源',
                'verbose_name_plural': '目录图片资源',
            },
        ),
        migrations.CreateModel(
            name='MultiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('creator', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('modify', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者')),
                ('transaction_id', models.BigIntegerField(default=1, verbose_name='事务ID')),
                ('version', models.IntegerField(default=1, verbose_name='版本号')),
                ('category_type', models.IntegerField(blank=True, choices=[(0, '直播'), (1, '资讯'), (2, '音乐'), (3, '点播'), (4, '餐饮'), (5, '商城')], default=1, verbose_name='目录类型')),
                ('show_order', models.IntegerField(default=9999, null=True, verbose_name='排序字段')),
                ('delete_flag', models.BooleanField(default=True, verbose_name='有效标识')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lems.MultiCategory', verbose_name='父目录')),
                ('tenant', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='system_manage.Tenant', verbose_name='租户')),
            ],
            options={
                'verbose_name': '目录',
                'verbose_name_plural': '目录',
            },
        ),
        migrations.CreateModel(
            name='MultilanguageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('creator', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='创建者')),
                ('modify_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='修改时间')),
                ('modify', models.CharField(default=users.models.UserProfile, max_length=100, verbose_name='修改者')),
                ('transaction_id', models.BigIntegerField(default=1, verbose_name='事务ID')),
                ('version', models.IntegerField(default=1, verbose_name='版本号')),
                ('phoneticize', models.CharField(blank=True, max_length=100, null=True, verbose_name='拼音名称')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='多语言名称')),
                ('language_code', models.CharField(blank=True, default='chi', max_length=50, verbose_name='语言编码')),
                ('description', models.TextField(max_length=4096, null=True, verbose_name='描述')),
                ('delete_flag', models.BooleanField(default=True, verbose_name='有效标识')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lems.MultiCategory', verbose_name='目录')),
            ],
            options={
                'verbose_name': '图文多语言',
                'verbose_name_plural': '图文多语言',
            },
        ),
        migrations.AddField(
            model_name='categorypicture',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lems.MultiCategory', verbose_name='目录'),
        ),
    ]

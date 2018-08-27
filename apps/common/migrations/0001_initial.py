# Generated by Django 2.0.2 on 2018-08-27 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(default='', max_length=100, verbose_name='省份')),
                ('city', models.CharField(default='', max_length=100, verbose_name='城市')),
                ('district', models.CharField(default='', max_length=100, verbose_name='区域')),
                ('address_detail', models.CharField(default='', max_length=100, verbose_name='详细地址')),
                ('signer_mobile', models.CharField(default='', max_length=11, verbose_name='电话')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('address_type', models.IntegerField(choices=[(1, '管理员地址'), (2, '用户住址'), (3, '用户工作地址'), (4, '门店地址')], help_text='1-管理员地址，2-用户住址，3-用户工作地址,4-门店地址', verbose_name='地址类型')),
            ],
            options={
                'verbose_name': '地址',
                'verbose_name_plural': '地址',
            },
        ),
    ]

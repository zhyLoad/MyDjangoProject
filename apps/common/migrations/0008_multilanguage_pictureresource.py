# Generated by Django 2.0 on 2018-12-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_auto_20181220_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Multilanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='多语言名称')),
                ('language_code', models.CharField(blank=True, default='chi', max_length=50, verbose_name='语言编码')),
                ('description', models.TextField(max_length=4096, null=True, verbose_name='描述')),
                ('delete_flag', models.BooleanField(default=True, verbose_name='有效标识')),
            ],
            options={
                'verbose_name': '多语言',
                'verbose_name_plural': '多语言',
            },
        ),
        migrations.CreateModel(
            name='PictureResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(null=True, verbose_name='图片大小')),
                ('resource_url', models.CharField(default='', max_length=4096, verbose_name='图片路径')),
                ('original_name', models.TextField(default='', max_length=100, verbose_name='原文件名')),
                ('name', models.TextField(default='', max_length=100, verbose_name='文件名')),
                ('horizontal_resoution', models.IntegerField(null=True, verbose_name='垂直分辨率')),
                ('vertical_resoution', models.IntegerField(null=True, verbose_name='水平分辨率')),
                ('delete_flag', models.BooleanField(default=True, verbose_name='有效标识')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
    ]

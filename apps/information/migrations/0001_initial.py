# Generated by Django 2.0 on 2018-11-26 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system_manage', '0002_auto_20181126_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(null=True, verbose_name='文件大小')),
                ('resource_url', models.CharField(max_length=4096, null=True, verbose_name='文件路径')),
                ('original_name', models.TextField(max_length=100, verbose_name='原文件名')),
                ('name', models.TextField(max_length=100, verbose_name='文件名')),
            ],
            options={
                'verbose_name': '文件资源',
                'verbose_name_plural': '文件资源',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_type', models.IntegerField(blank=True, choices=[(0, '新闻'), (1, '图片'), (2, '文档')], verbose_name='图文类型')),
                ('information_status', models.IntegerField(blank=True, choices=[(0, '待审核'), (1, '审核中'), (2, '审核通过'), (3, '审核不通过'), (4, '已发布')], verbose_name='图文状态')),
                ('audit_reason', models.CharField(blank=True, max_length=2048, verbose_name='审核原因')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_manage.Tenant', verbose_name='租户')),
            ],
            options={
                'verbose_name': '图文',
                'verbose_name_plural': '图文',
            },
        ),
        migrations.CreateModel(
            name='MultilanguageInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='多语言名称')),
                ('language_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='语言编码')),
                ('description', models.TextField(max_length=4096, verbose_name='描述')),
                ('information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Information', verbose_name='图文')),
            ],
            options={
                'verbose_name': '图文多语言',
                'verbose_name_plural': '图文多语言',
            },
        ),
        migrations.CreateModel(
            name='PosterResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField(null=True, verbose_name='文件大小')),
                ('resource_url', models.CharField(max_length=4096, null=True, verbose_name='文件路径')),
                ('original_name', models.TextField(max_length=100, verbose_name='原文件名')),
                ('name', models.TextField(max_length=100, verbose_name='文件名')),
                ('horizontal_resoution', models.IntegerField(null=True, verbose_name='垂直分辨率')),
                ('vertical_resoution', models.IntegerField(null=True, verbose_name='水平分辨率')),
                ('information', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Information', verbose_name='图文')),
            ],
            options={
                'verbose_name': '图片资源',
                'verbose_name_plural': '图片资源',
            },
        ),
        migrations.AddField(
            model_name='fileresource',
            name='information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.Information', verbose_name='图文'),
        ),
    ]

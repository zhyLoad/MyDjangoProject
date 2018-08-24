# Generated by Django 2.0.2 on 2018-08-24 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.IntegerField(choices=[(1, '管理员地址'), (2, '用户住址'), (3, '用户工作地址'), (4, '门店地址')], help_text='1-管理员地址，2-用户住址，3-用户工作地址,4-门店地址', verbose_name='地址类型'),
        ),
    ]
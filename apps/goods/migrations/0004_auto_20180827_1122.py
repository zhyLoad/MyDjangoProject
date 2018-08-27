# Generated by Django 2.0.2 on 2018-08-27 11:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20180827_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='closing_time',
            field=models.TimeField(blank=True, verbose_name='关门时间'),
        ),
        migrations.AlterField(
            model_name='store',
            name='identify',
            field=models.CharField(default=uuid.UUID('9381120f-b4b3-4b17-8b97-395493be89d7'), help_text='门店标识号', max_length=30, verbose_name='门店标识号'),
        ),
        migrations.AlterField(
            model_name='store',
            name='opening_time',
            field=models.TimeField(blank=True, verbose_name='开始营业时间'),
        ),
    ]

# Generated by Django 2.0.2 on 2018-03-11 15:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('user_operation', '0002_auto_20180213_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='district',
            new_name='area',
        ),
    ]

# Generated by Django 2.0 on 2018-12-21 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileresource',
            name='information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_resources', to='information.Information', verbose_name='图文'),
        ),
        migrations.AlterField(
            model_name='multilanguageinformation',
            name='information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='multi_language_informations', to='information.Information', verbose_name='图文'),
        ),
        migrations.AlterField(
            model_name='posterresource',
            name='information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='poster_resources', to='information.Information', verbose_name='图文'),
        ),
    ]
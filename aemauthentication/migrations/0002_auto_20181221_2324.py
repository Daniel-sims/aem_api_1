# Generated by Django 2.1.3 on 2018-12-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aemauthentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]

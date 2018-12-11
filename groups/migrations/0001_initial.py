# Generated by Django 2.1.3 on 2018-12-11 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_field', models.SlugField(unique=True)),
                ('linked_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aemgroup', to='auth.Group')),
            ],
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-30 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0012_auto_20200430_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
    ]

# Generated by Django 3.0.3 on 2020-04-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0016_auto_20200430_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date_recieved',
            field=models.DateTimeField(),
        ),
    ]

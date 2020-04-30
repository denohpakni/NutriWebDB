# Generated by Django 3.0.3 on 2020-04-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0005_auto_20200422_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='Order_Number',
            field=models.CharField(blank=True, default='order number', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='Sample_Reciever',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]

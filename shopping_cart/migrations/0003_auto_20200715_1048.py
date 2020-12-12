# Generated by Django 3.0.6 on 2020-07-15 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0001_initial'),
        ('shopping_cart', '0002_serviceitem_number_of_samples'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitem',
            name='number_of_samples',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Webapp.Services'),
        ),
    ]
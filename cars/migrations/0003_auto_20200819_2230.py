# Generated by Django 3.1 on 2020-08-19 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20200819_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.PositiveSmallIntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]),
        ),
    ]
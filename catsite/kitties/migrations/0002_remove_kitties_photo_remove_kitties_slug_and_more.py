# Generated by Django 4.2.4 on 2023-08-28 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kitties', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kitties',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='kitties',
            name='slug',
        ),
        migrations.AlterField(
            model_name='kitties',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='kitties.category'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-12-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pblog_web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='id',
            name='age',
            field=models.IntegerField(),
        ),
    ]

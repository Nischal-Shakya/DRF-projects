# Generated by Django 4.0.4 on 2022-12-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=2)),
                ('lookingForJob', models.BooleanField(default=False)),
            ],
        ),
    ]

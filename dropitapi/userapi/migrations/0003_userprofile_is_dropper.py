# Generated by Django 3.2.3 on 2021-08-07 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapi', '0002_auto_20210806_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_dropper',
            field=models.BooleanField(default=False),
        ),
    ]

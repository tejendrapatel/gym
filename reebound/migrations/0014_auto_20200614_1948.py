# Generated by Django 3.0.7 on 2020-06-15 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reebound', '0013_auto_20200614_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='weekdays',
        ),
        migrations.DeleteModel(
            name='DAYS',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-15 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reebound', '0014_auto_20200614_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField(max_length=20)),
                ('mondayworkout', models.TextField(max_length=20)),
                ('monday_trainer', models.TextField(max_length=20)),
                ('Tuesdayworkout', models.TextField(max_length=20)),
                ('Tuesday_trainer', models.TextField(max_length=20)),
                ('Wednesdayworkout', models.TextField(max_length=20)),
                ('Wednesday_trainer', models.TextField(max_length=20)),
                ('Thusdayworkout', models.TextField(max_length=20)),
                ('Thusday_trainer', models.TextField(max_length=20)),
                ('Fridayworkout', models.TextField(max_length=20)),
                ('Friday_trainer', models.TextField(max_length=20)),
                ('Saturdayworkout', models.TextField(max_length=20)),
                ('Saturday_trainer', models.TextField(max_length=20)),
                ('Sundayworkout', models.TextField(max_length=20)),
                ('Sunday_trainer', models.TextField(max_length=20)),
            ],
        ),
    ]

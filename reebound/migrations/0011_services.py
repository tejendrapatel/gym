# Generated by Django 3.0.7 on 2020-06-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reebound', '0010_auto_20200612_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]

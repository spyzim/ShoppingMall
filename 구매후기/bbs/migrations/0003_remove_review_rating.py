# Generated by Django 2.2.13 on 2020-09-16 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20200910_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
    ]

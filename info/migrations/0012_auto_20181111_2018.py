# Generated by Django 2.1.2 on 2018-11-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_auto_20181111_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=15),
        ),
    ]

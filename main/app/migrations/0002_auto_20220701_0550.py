# Generated by Django 3.1.14 on 2022-07-01 00:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='file',
            field=models.FileField(blank=True, upload_to='C://Coding_assignment//main//main//static_files'),
        ),
        migrations.AlterField(
            model_name='order',
            name='datetimestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 1, 5, 50, 14, 843081)),
        ),
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(default=[0], related_name='ordered_item', to='app.Item'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('success', 'SUCCESS'), ('pending', 'PENDING'), ('failed', 'FAILED')], default='success', max_length=10),
        ),
    ]
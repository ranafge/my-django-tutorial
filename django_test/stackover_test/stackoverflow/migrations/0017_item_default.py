# Generated by Django 3.1.7 on 2021-04-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0016_auto_20210409_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='default',
            field=models.CharField(blank=True, default='this is my default', max_length=150, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0004_auto_20210328_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='upload',
            field=models.ImageField(blank=True, default='/home/rana/Pictures/images.png', null=True, upload_to='up/'),
        ),
    ]

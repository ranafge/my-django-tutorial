# Generated by Django 3.1.7 on 2021-03-28 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stackoverflow', '0002_auto_20210328_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='work',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stackoverflow.work'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-16 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_alter_resultmodel_percent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResultModel',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-12 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0006_alter_quesmodel_question_resultmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultmodel',
            name='total',
        ),
    ]

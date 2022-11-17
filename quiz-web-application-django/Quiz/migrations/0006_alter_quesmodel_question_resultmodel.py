# Generated by Django 4.0.5 on 2022-06-12 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Quiz', '0005_auto_20210512_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='question',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='ResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField(max_length=10)),
                ('score', models.IntegerField(max_length=10)),
                ('total', models.IntegerField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 2.2.4 on 2019-08-31 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]

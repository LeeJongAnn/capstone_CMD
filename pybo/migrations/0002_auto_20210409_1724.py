# Generated by Django 3.1.7 on 2021-04-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmd_information',
            name='user_num',
            field=models.IntegerField(),
        ),
    ]
# Generated by Django 3.1.7 on 2021-06-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_auto_20210608_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_apply',
            name='assign_num',
            field=models.CharField(max_length=4),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-10 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_business_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_apply',
            name='business_num',
            field=models.IntegerField(),
        ),
    ]

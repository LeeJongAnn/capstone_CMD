# Generated by Django 3.1.7 on 2021-04-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0002_auto_20210426_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

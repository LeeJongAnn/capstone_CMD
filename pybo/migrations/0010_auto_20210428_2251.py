# Generated by Django 3.1.7 on 2021-04-28 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0009_cmd_information_bussiness_num'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cmd_information',
            old_name='bussiness_num',
            new_name='cmd_bussiness_num',
        ),
        migrations.RemoveField(
            model_name='cmd_information',
            name='user_num',
        ),
        migrations.RemoveField(
            model_name='question',
            name='position_end',
        ),
        migrations.RemoveField(
            model_name='question',
            name='position_start',
        ),
        migrations.RemoveField(
            model_name='question',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time_end',
        ),
        migrations.RemoveField(
            model_name='question',
            name='time_start',
        ),
        migrations.AddField(
            model_name='cmd_information',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cmd_information',
            name='position_end',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cmd_information',
            name='position_start',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cmd_information',
            name='time_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cmd_information',
            name='time_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-29 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Car_num', models.CharField(max_length=15)),
                ('Car_variety', models.CharField(max_length=10)),
                ('Car_manager', models.CharField(max_length=10)),
                ('bussiness_num', models.CharField(max_length=15)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CMD_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('Car_num', models.CharField(max_length=15)),
                ('bussiness_manager', models.CharField(max_length=10)),
                ('bussiness_num', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField()),
                ('start_pos', models.CharField(max_length=10)),
                ('destination_pos', models.CharField(max_length=10)),
                ('depart_date', models.CharField(max_length=25)),
                ('arrive_date', models.CharField(max_length=25)),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('Lat', models.CharField(max_length=30)),
                ('Long', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CMD_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('cmd_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.cmd_question')),
            ],
        ),
        migrations.CreateModel(
            name='business_apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=15)),
                ('assign_num', models.IntegerField()),
                ('Living', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=5)),
                ('create_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.question')),
            ],
        ),
    ]

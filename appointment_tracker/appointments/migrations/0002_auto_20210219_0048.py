# Generated by Django 3.1.6 on 2021-02-18 22:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.IntegerField(default='', primary_key=True, serialize=False, unique=True)),
                ('appointment_text', models.TextField()),
                ('appointment_date', models.DateTimeField(blank=True, default=datetime.date.today, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('department_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('employee_firstname', models.CharField(max_length=20)),
                ('employee_lastname', models.CharField(max_length=20)),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.department')),
            ],
        ),
        migrations.RemoveField(
            model_name='reply',
            name='application',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='id',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='votes',
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_date',
            field=models.DateTimeField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_id',
            field=models.IntegerField(default='1', primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_text',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.AddField(
            model_name='appointment',
            name='department_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.department'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='appointment_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='appointments.appointment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='employee_id',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='appointments.employee'),
            preserve_default=False,
        ),
    ]

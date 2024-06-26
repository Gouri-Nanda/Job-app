# Generated by Django 4.2.10 on 2024-03-07 08:54

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_data',
            fields=[
                ('job_Id', models.AutoField(primary_key=True, serialize=False)),
                ('job_position', models.CharField(max_length=100)),
                ('job_company', models.CharField(max_length=100)),
                ('job_location', models.CharField(max_length=100)),
                ('job_salary', models.IntegerField(max_length=15)),
                ('company_logo', models.FileField(null=True, upload_to=job.models.user_directory_path, verbose_name='')),
            ],
            options={
                'db_table': 'job',
            },
        ),
    ]

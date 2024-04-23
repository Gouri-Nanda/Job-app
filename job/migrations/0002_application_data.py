# Generated by Django 4.2.10 on 2024-03-07 10:19

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='application_data',
            fields=[
                ('cand_Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('resume', models.FileField(null=True, upload_to=job.models.user_directory_path2, verbose_name='')),
            ],
            options={
                'db_table': 'applications',
            },
        ),
    ]

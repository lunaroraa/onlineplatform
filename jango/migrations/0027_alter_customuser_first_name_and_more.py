# Generated by Django 5.1.7 on 2025-03-26 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jango', '0026_alter_attemptedtest_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.IntegerField(),
        ),
    ]

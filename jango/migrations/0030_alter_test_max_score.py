# Generated by Django 5.1.7 on 2025-03-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jango', '0029_customuser_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='max_score',
            field=models.IntegerField(default=0),
        ),
    ]

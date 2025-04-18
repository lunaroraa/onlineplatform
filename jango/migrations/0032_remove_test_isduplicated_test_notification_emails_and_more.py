# Generated by Django 5.1.7 on 2025-04-11 04:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jango', '0031_test_isduplicated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='isDuplicated',
        ),
        migrations.AddField(
            model_name='test',
            name='notification_emails',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='test',
            name='receive_email_notifications',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_token',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.CreateModel(
            name='AllowedParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed_participants', to='jango.test')),
            ],
        ),
    ]

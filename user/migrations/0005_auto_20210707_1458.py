# Generated by Django 3.1.3 on 2021-07-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210707_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_private_account',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('None', 'Prefer not to say.')], max_length=10, null=True),
        ),
    ]

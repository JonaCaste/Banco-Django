# Generated by Django 3.2.8 on 2021-10-23 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_auto_20211022_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='destiny_origin',
            new_name='destiny_account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='account_origin',
            new_name='origin_account',
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-16 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'CustomUser', 'verbose_name_plural': 'CustomUsers'},
        ),
    ]

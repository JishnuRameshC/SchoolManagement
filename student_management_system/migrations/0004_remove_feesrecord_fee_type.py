# Generated by Django 5.1.2 on 2024-10-23 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_system', '0003_feesrecord_libraryrecord_remove_feeshistory_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feesrecord',
            name='fee_type',
        ),
    ]
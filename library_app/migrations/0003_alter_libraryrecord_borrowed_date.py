# Generated by Django 5.1.2 on 2024-10-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_libraryrecord_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryrecord',
            name='borrowed_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]

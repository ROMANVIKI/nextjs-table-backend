# Generated by Django 5.1.4 on 2024-12-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_datatable_priority_alter_datatable_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datatable",
            name="code",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

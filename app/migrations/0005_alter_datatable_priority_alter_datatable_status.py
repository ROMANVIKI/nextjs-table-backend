# Generated by Django 5.1.4 on 2024-12-27 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_datatable_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="datatable",
            name="priority",
            field=models.CharField(
                choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")],
                max_length=7,
            ),
        ),
        migrations.AlterField(
            model_name="datatable",
            name="status",
            field=models.CharField(
                choices=[
                    ("Done", "Done"),
                    ("Todo", "Todo"),
                    ("In-Progress", "In-Progress"),
                    ("Canceled", "Canceled"),
                ],
                max_length=11,
            ),
        ),
    ]
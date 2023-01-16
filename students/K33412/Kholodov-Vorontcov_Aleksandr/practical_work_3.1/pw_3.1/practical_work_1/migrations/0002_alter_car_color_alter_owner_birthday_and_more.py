# Generated by Django 4.1.2 on 2023-01-15 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practical_work_1", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="color",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="owner",
            name="birthday",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ownership",
            name="date_end",
            field=models.DateField(blank=True, null=True),
        ),
    ]

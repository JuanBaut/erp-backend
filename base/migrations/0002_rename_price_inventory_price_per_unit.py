# Generated by Django 4.2.14 on 2024-07-29 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="inventory",
            old_name="price",
            new_name="price_per_unit",
        ),
    ]
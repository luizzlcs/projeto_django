# Generated by Django 5.0.2 on 2024-02-21 15:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("filme", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filme",
            old_name="descricao",
            new_name="descricao",
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-27 16:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("filme", "0002_episodio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filme",
            old_name="desricao",
            new_name="descric",
        ),
    ]

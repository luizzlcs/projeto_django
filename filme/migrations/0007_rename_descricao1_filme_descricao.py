# Generated by Django 5.0.2 on 2024-02-21 16:27

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("filme", "0006_rename_descricao2_filme_descricao1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filme",
            old_name="descricao1",
            new_name="descricao",
        ),
    ]
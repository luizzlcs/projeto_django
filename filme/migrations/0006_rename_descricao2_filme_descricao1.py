# Generated by Django 5.0.2 on 2024-02-21 16:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("filme", "0005_rename_descricao_filme_descricao2"),
    ]

    operations = [
        migrations.RenameField(
            model_name="filme",
            old_name="descricao2",
            new_name="descricao1",
        ),
    ]

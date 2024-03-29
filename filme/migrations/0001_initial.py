# Generated by Django 5.0.2 on 2024-02-15 14:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Filme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100)),
                ("thumb", models.ImageField(upload_to="thumbs_filmes")),
                ("descricao", models.TextField(max_length=1000)),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("ANALISES", "Análises"),
                            ("PROGRAMACAO", "Programação"),
                            ("APRESENTACAO", "Apresentação"),
                            ("OUTROS", "Outros"),
                        ],
                        max_length=15,
                    ),
                ),
                ("visualizacao", models.IntegerField(default=0)),
                (
                    "data_criacao",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]

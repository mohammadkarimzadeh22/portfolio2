# Generated by Django 4.2.4 on 2023-08-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("folioApp", "0002_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=500)),
                ("description", models.TextField(max_length=500)),
            ],
        ),
    ]

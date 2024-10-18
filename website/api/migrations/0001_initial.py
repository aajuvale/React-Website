# Generated by Django 5.1.2 on 2024-10-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("code", models.CharField(default="", max_length=10, unique=True)),
                ("host", models.CharField(max_length=50, unique=True)),
                ("guest_can_pause", models.BooleanField(default=False)),
                ("guest_can_skip", models.IntegerField(default=2)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

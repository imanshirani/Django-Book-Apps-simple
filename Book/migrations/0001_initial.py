# Generated by Django 5.0.6 on 2024-05-22 02:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AddBook",
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
                ("book_name", models.CharField(max_length=255)),
                ("book_image", models.ImageField(max_length=255, upload_to="")),
                ("book_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]

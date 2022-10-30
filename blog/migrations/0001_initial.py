# Generated by Django 4.1.2 on 2022-10-19 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(default="")),
                ("keywords", models.CharField(default="", max_length=400)),
                ("metaDesc", models.CharField(default="", max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
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
                ("full_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("sent_date", models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubscriberEmail",
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
                ("email", models.EmailField(max_length=254)),
                ("subscriptionDate", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="SubCategory",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(default="")),
                ("keywords", models.CharField(default="", max_length=400)),
                ("metaDesc", models.CharField(default="", max_length=400)),
                (
                    "mainCategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.category"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=200, unique=True)),
                ("slug", models.SlugField(default="")),
                (
                    "featuredImage",
                    models.ImageField(
                        default="defaultBG.png", upload_to="uploads/images"
                    ),
                ),
                ("keywords", models.CharField(default="", max_length=400)),
                ("metaDesc", models.CharField(default="", max_length=400)),
                ("body", tinymce.models.HTMLField(blank=True, null=True)),
                ("createdAt", models.DateTimeField(null=True)),
                ("updated", models.BooleanField(default=False)),
                ("postStatus", models.BooleanField(default=False)),
                ("views", models.IntegerField(default=0)),
                ("likes", models.IntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="category",
                        to="blog.category",
                    ),
                ),
                (
                    "subCategory",
                    models.ManyToManyField(blank=True, to="blog.subcategory"),
                ),
            ],
        ),
    ]

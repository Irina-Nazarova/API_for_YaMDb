# Generated by Django 3.0.8 on 2021-01-27 15:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


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
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("slug", models.SlugField(max_length=30, unique=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "db_table": "category",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("slug", models.SlugField(max_length=30, unique=True)),
            ],
            options={
                "verbose_name": "genre",
                "verbose_name_plural": "genres",
                "db_table": "genre",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Title",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "year",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(2021)
                        ],
                        verbose_name="Год выпуска",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("rating", models.IntegerField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        db_column="category",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="titles",
                        to="api.Category",
                    ),
                ),
                (
                    "genre",
                    models.ManyToManyField(
                        blank=True,
                        db_table="genre_title",
                        related_name="titles",
                        to="api.Genre",
                    ),
                ),
            ],
            options={
                "verbose_name": "title",
                "verbose_name_plural": "titles",
                "db_table": "titles",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст отзыва")),
                (
                    "score",
                    models.PositiveSmallIntegerField(
                        blank=True,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(
                                10, message="Максимально возможная оценка - 10"
                            ),
                        ],
                        verbose_name="Оценка произведения",
                    ),
                ),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        db_index=True,
                        verbose_name="Дата публикации отзыва",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        db_column="author",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор отзыва",
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        db_column="title_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="api.Title",
                        verbose_name="Произведение",
                    ),
                ),
            ],
            options={
                "db_table": "review",
                "ordering": ["-pub_date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(verbose_name="Текст комментария")),
                (
                    "pub_date",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="Дата публикации комментария",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        db_column="author",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор комментария",
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        db_column="review_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="api.Review",
                        verbose_name="Отзыв",
                    ),
                ),
            ],
            options={
                "db_table": "comments",
                "ordering": ["-pub_date"],
            },
        ),
    ]

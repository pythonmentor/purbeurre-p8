from django.db import models


class Category(models.Model):
    name = models.CharField('category name', max_length=100)

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["name"]
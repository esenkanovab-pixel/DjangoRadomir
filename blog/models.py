from django.db import models

class Blog(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержание")

    likes = models.PositiveIntegerField("Просмотры", default=0)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    intro = models.TextField()
    text = models.TextField()
    img = models.CharField(max_length=50, default='')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

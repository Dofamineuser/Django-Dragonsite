from django.db import models
from home.models import Team


class File(models.Model):
    title = models.CharField("Назва", max_length=30)
    slug = models.SlugField()
    description = models.CharField("Короткий опис", max_length=150)
    text = models.TextField("Повний опис файлу")
    file = models.FileField(upload_to='downloads')
    organizer = models.ForeignKey(Team, on_delete=models.CASCADE)

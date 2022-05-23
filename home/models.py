from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class OwnerInfo(models.Model):
    image = ProcessedImageField(upload_to="home/images",
                                processors=[ResizeToFill(445, 445)],
                                format="JPEG",
                                options={"quality": 60})
    title = models.CharField("Заголовок про себе", max_length=100)
    text = models.TextField("Опис про себе")
    address = models.CharField("Адреса", max_length=30)
    email = models.EmailField("Імейл власника сайту")
    phone = models.CharField("Номер телефону власника", max_length=13)


class Team(models.Model):
    name = models.CharField(verbose_name="ім'я та прізвище", max_length=50)
    role = models.CharField(verbose_name="посада або роль", max_length=50)
    facebook = models.CharField(max_length=100, default="#")
    instagram = models.CharField(max_length=100, default="#")
    twitter = models.CharField(max_length=100, default="#")
    image = models.ImageField(upload_to='images')
    image_ready = ImageSpecField(source='image',
                                 processors=[ResizeToFill(400, 400)],
                                 format='JPEG',
                                 options={'quality': 60})

    def __str__(self):
        return f'{self.name} - {self.role}'





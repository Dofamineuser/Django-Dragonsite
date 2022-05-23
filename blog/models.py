from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from home.models import Team


class Blog(models.Model):
    title = models.CharField(verbose_name="Опис одим словом", max_length=20, null=True)
    slug = models.SlugField(unique=True)
    day = models.CharField(verbose_name="день", max_length=10, help_text="max 10 символів")
    month = models.CharField(verbose_name="місяць", max_length=30, help_text="Вкажіть Словом")
    description = models.TextField(verbose_name="Опис заходу")
    text = models.TextField(verbose_name="Повний опис заходу", blank=True, help_text="Необов'язкове поле")
    organizer = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="зображення блогу", upload_to='blog_images')
    home_image = ImageSpecField(source="image",
                                processors=[ResizeToFill(540, 304)],
                                format="JPEG",
                                options={"quality": 80})
    blog_image = ImageSpecField(source="image",
                                processors=[ResizeToFill(730, 411)],
                                format="JPEG",
                                options={"quality": 90})
    recent_image = ImageSpecField(source="image",
                                  processors=[ResizeToFill(80, 80)],
                                  format="JPEG",
                                  options={"quality": 50})

    def __str__(self):
        return f'{self.title} ({self.month})'


class BlogCat(models.Model):
    name = models.CharField(max_length=15,
                            unique=True,
                            verbose_name="Назва категорії")
    number = models.IntegerField("кількість записів даної категорії", blank=True)

    def __str__(self):
        return self.name
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from home.models import Team
from managefiles.models import File
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField("Опис одим словом", max_length=20, null=True)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField("Дата", default=now, editable=True)
    description = models.TextField("Опис заходу")
    text = models.TextField(verbose_name="Повний опис заходу", blank=True, help_text="Необов'язкове поле")
    organizer = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Організатор")
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Додавати необов'язково"
    )
    image = models.ImageField("зображення блогу", upload_to='blog_images')
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
        return f'{self.title} ({self.date})'


class BlogCat(models.Model):
    name = models.CharField(max_length=15,
                            unique=True,
                            verbose_name="Назва категорії")
    number = models.IntegerField("кількість записів даної категорії", blank=True)

    def __str__(self):
        return self.name
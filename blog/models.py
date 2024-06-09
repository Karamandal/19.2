from django.db import models
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    slug = models.SlugField(unique=True, null=True, blank=True)
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='изображение', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    views_count = models.PositiveIntegerField(verbose_name='просмотры', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



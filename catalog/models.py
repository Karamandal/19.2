from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=200, verbose_name='Описание')
    image = models.ImageField(max_length=150, verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=150, verbose_name='Цена')
    created_at = models.DateTimeField(verbose_name='Дата создания')
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description} {self.category} {self.price} {self.created_at} {self.updated_at}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов

from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # Удаляем старые данные
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загружаем данные из JSON-файла
        with open('catalog_data.json', 'r', encoding='windows-1251') as file:
            data = json.load(file)

        # Создаем категории
        categories = {}
        for item in data:
            model = item['model']
            fields = item['fields']

            if model == 'catalog.category':
                categories[item['pk']] = Category.objects.create(id=item['pk'], **fields)

        # Создаем продукты, используя экземпляры категорий
        for item in data:
            model = item['model']
            fields = item['fields']

            if model == 'catalog.product':
                category_instance = categories.get(fields['category'])
                if category_instance:
                    del fields['category']  # Удаляем поле category из fields, чтобы не дублировать его
                    Product.objects.create(id=item['pk'], category=category_instance, **fields)

        self.stdout.write(self.style.SUCCESS('Database has been seeded.'))
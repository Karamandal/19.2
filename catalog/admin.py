from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name', 'name',)


@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)





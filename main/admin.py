from django.contrib import admin
from .models import FoodCategory, Food


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'name_en', 'name_ch', 'order_id')
    search_fields = ('name_ru', 'name_en', 'name_ch')


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'category', 'code', 'internal_code', 'is_publish', 'cost')
    list_filter = ('category', 'is_publish', 'is_vegan', 'is_special')
    search_fields = ('name_ru', 'description_ru', 'description_en', 'description_ch')
    raw_id_fields = ('category',)

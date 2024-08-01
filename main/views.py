from rest_framework import generics
from django.db.models import Prefetch
from .models import FoodCategory, Food
from .serializers import FoodListSerializer


class FoodsListView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        # Предварительно выбираем опубликованные блюда
        published_foods = Food.objects.filter(is_publish=True)

        # Выбираем категории, содержащие хотя бы одно опубликованное блюдо
        categories = FoodCategory.objects.filter(
            food__in=published_foods
        ).distinct().prefetch_related(
            Prefetch('food', queryset=published_foods)
        )

        return categories


from django.urls import path
from .views import FoodsListView

urlpatterns = [
    path('api/v1/foods/', FoodsListView.as_view(), name='food-list'),
]

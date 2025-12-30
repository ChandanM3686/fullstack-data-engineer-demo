from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ActivityViewSet, weather_api

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('activities', ActivityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('weather/', weather_api),
]

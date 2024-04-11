from rest_framework import routers
from .views import AnimalsViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'animals/', AnimalsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

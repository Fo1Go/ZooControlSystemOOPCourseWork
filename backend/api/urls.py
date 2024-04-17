from rest_framework import routers
from .views import (AnimalsViewSet, ClientProfileViewSet, EmployerViewSet, FeedingViewSet,
                    TicketViewSet, FeedbackViewSet, SpeciesViewSet, MedicalCheckupViewSet, JobPositionsViewSet)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'client', ClientProfileViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'feedback', FeedbackViewSet)

router.register(r'employer', EmployerViewSet)
router.register(r'positions', JobPositionsViewSet)
router.register(r'feeding', FeedingViewSet)

router.register(r'animals', AnimalsViewSet)
router.register(r'species', SpeciesViewSet)
router.register(r'medical', MedicalCheckupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

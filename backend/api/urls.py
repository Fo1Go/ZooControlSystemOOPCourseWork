from rest_framework import routers
from .views import (AnimalsViewSet, ClientProfileViewSet, EmployerViewSet, FeedingViewSet,
                    TicketViewSet, FeedbackViewSet, SpeciesViewSet, MedicalCheckupViewSet, JobPositionsViewSet,
                    FinanceViewSet, ContactInformationViewSet)
from django.urls import path, include, re_path


router = routers.DefaultRouter()
router.register(r'clients', ClientProfileViewSet)
router.register(r'tickets', TicketViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'finance', FinanceViewSet)
router.register(r'contacts', ContactInformationViewSet)

router.register(r'employers', EmployerViewSet)
router.register(r'positions', JobPositionsViewSet)
router.register(r'feeding', FeedingViewSet)

router.register(r'animals', AnimalsViewSet)
router.register(r'species', SpeciesViewSet)
router.register(r'medical', MedicalCheckupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    re_path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

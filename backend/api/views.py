from django.shortcuts import render
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrIsAdmin, ReadOnly, IsAdminUserOrIsEmployer


class EmployerViewSet(ModelViewSet):
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer
    permission_classes = (IsOwnerOrIsAdmin, )


class JobPositionsViewSet(ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer
    permission_classes = (IsAdminUser, )


class ClientProfileViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsOwnerOrIsAdmin, )


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsOwnerOrIsAdmin, )


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class AnimalsViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class SpeciesViewSet(ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class MedicalCheckupViewSet(ModelViewSet):
    queryset = MedicalCheckup.objects.all()
    serializer_class = MedicalCheckupSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self, pk=None):
        pk = self.request.query_params.get('pk')
        if pk is not None:
            return MedicalCheckup.objects.filter(animal=pk)
        return self.queryset


class FeedingViewSet(ModelViewSet):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer
    permission_classes = (IsAdminUserOrIsEmployer, )


class FinanceViewSet(ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    permission_classes = (IsAdminUser,)


class ContactInformationViewSet(ModelViewSet):
    queryset = ContactInformation
    serializer_class = ContactInformationSerializer
    permission_classes = (IsAdminUserOrReadOnly, )

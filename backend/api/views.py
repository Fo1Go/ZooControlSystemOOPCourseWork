from django.shortcuts import render
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrIsAdmin


class ClientProfileViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsOwnerOrIsAdmin, )


class AnimalsViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = (IsAdminOrReadOnly, )


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = (IsOwnerOrIsAdmin, )


class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated, )


class SpeciesViewSet(ModelViewSet):
    serializer_class = SpeciesSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )

    def get_queryset(self, pk=None):
        pk = self.request.query_params.get('pk')
        if pk is not None:
            return Species.object.filter(pk=pk)
        return Species.objects.all()

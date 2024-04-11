from rest_framework import serializers
from .models import *
from .utils import update_user_information


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "is_staff", "is_superuser", "is_active", "date_joined"]


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    tickets = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ["user", "phone_number", "tickets"]

    def get_tickets(self, obj):
        return TicketSerializer(obj.tickets, many=True, read_only=True).data

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data.pop('user'))
        client = Client(user=user, **validated_data)
        client.save()
        return client

    def update(self, instance, validated_data, *args, **kwargs):
        user_data = validated_data.pop('user', instance.user)
        instance.phone_number = user_data.get('phone_number', instance.phone_number)
        instance.save()
        user = update_user_information(instance, user_data)
        user.save()
        return instance


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    position = serializers.SerializerMethodField()
    base_salary_rate = serializers.FloatField()

    class Meta:
        model = Employer
        fields = ["user", "base_salary_rate", "position"]

    def get_position(self, obj):
        return JobPositionSerializer(obj.position).data

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data.pop('user'))
        employer = Employer(user=user, **validated_data)
        employer.save()
        return employer

    def update(self, instance, validated_data, *args, **kwargs):
        user_data = validated_data.pop('user', instance.user)
        instance.position = user_data.get('position', instance.position)
        instance.base_salary_rate = user_data.get('base_salary_rate', instance.base_salary_rate)
        instance.save()
        user = update_user_information(instance, user_data)
        user.save()
        return instance


class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = ["position", "base_salary_rate"]


class TicketSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ['client', 'type', 'visit_date', 'purchase_date', 'ticket_number', 'price']


class SpeciesSerializer(serializers.ModelSerializer):
    animals = serializers.SerializerMethodField()

    class Meta:
        model = Species
        fields = ['animals', 'title', 'description']

    def get_animals(self, obj):
        return AnimalSerializer(obj.animals, many=True).data

class AnimalSerializer(serializers.ModelSerializer):
    medical_checkups = serializers.SerializerMethodField()
    species = SpeciesSerializer(read_only=True)

    class Meta:
        model = Animal
        fields = ["species", "nickname", "description", "age_in_month", "gender", "medical_checkups"]

    def medical_checkups(self, obj):
        return MedicalCheckupSerializer(obj.medical_checkups, many=True, read_only=True).data


class MedicalCheckupSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)

    class Meta:
        model = MedicalCheckup
        fields = ["animal", "last_date_check", "diagnosis", "recommended_actions"]


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = ["cost_adult_ticket", "cost_child_ticket", "open_time", "close_time"]


class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ["user", "title", "description"]

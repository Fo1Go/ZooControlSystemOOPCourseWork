from rest_framework import serializers
from .models import *
from .utils import update_user_information, create_user_information


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name",
                  "date_joined", "is_staff", "is_superuser", "is_active"]


class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ["user", "phone_number", "tickets", "reviews"]

    def create(self, validated_data, *args, **kwargs):
        user = create_user_information(validated_data.pop("user"))
        client = Client(user=user, phone_number=validated_data.pop('phone_number'))
        client.save()
        user.save()
        return client

    def update(self, instance, validated_data, *args, **kwargs):
        user_json = validated_data.pop('user', instance.user)
        instance.phone_number = validated_data.pop('phone_number', instance.phone_number)
        instance.save()
        user = update_user_information(instance, user_json)
        user.save()
        return instance


class EmployerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    position = serializers.SerializerMethodField("get_position")
    base_salary_rate = serializers.FloatField()

    class Meta:
        model = Employer
        fields = ["user", "base_salary_rate", "position"]

    @property
    def position(self, obj):
        return JobPositionSerializer(obj.position).data

    def create(self, validated_data, *args, **kwargs):
        user = create_user_information(validated_data.pop("user"))
        employer = Employer(user=user, **validated_data)
        user.save()
        employer.save()
        return employer

    def update(self, instance, validated_data, *args, **kwargs):
        instance.position = validated_data.get('position', instance.position)
        instance.base_salary_rate = validated_data.get('base_salary_rate', instance.base_salary_rate)
        instance.save()
        user = update_user_information(instance, validated_data.pop('user', instance.user))
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


class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = ["cost_adult_ticket", "cost_child_ticket", "open_time", "close_time"]


class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = ["user", "title", "description"]


class SpeciesSerializer(serializers.ModelSerializer):
    animals = serializers.SerializerMethodField("get_animals")

    class Meta:
        model = Species
        fields = ['title', 'description', 'animals']

    @property
    def animals(self):
        return AnimalSerializer(obj.animals, many=True).data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def create(self, validated_data, *args, **kwargs):
        species = Species(title=validated_data.pop('title'), description=validated_data.pop('description'))
        species.save()
        return species


class AnimalSerializer(serializers.ModelSerializer):
    species = serializers.SerializerMethodField('get_species')

    class Meta:
        model = Animal
        fields = ["nickname", "description", "age_in_month", "gender", "species"]

    @property
    def species(self, obj):
        return SpeciesSerializer(obj.species).data

    def create(self, validated_data, *args, **kwargs):
        species = validated_data.pop('species', None)
        animal = Animal(species=species, **validated_data)
        animal.save()
        return animal

    def update(self, instance, validated_data, *args, **kwargs):
        instance.description = validated_data.pop('description', instance.description)
        instance.nickname = validated_data.pop('nickname', instance.nickname)
        instance.age_in_month = validated_data.pop('age_in_month', instance.age_in_month)
        instance.gender = validated_data.pop('gender', instance.gender)
        instance.species = validated_data.pop('species', instance.species)
        instance.save()
        return instance


class MedicalCheckupSerializer(serializers.ModelSerializer):
    animal = serializers.SerializerMethodField("get_animal")

    class Meta:
        model = MedicalCheckup
        fields = ["last_date_check", "diagnosis", "recommended_actions", "animal"]

    @property
    def animal(self, obj):
        return AnimalSerializer(obj.animal).data

    def create(self, validated_data, *args, **kwargs):
        animal = validated_data.pop('animal', None)
        medical_checkup = MedicalCheckup(animal=animal, **validated_data)
        medical_checkup.save()
        return medical_checkup

    def update(self, instance, validated_data, *args, **kwargs):
        instance.last_date_check = validated_data.pop('last_date_check', instance.last_date_check)
        instance.diagnosis = validated_data.pop('diagnosis', instance.diagnosis)
        instance.recommended_actions = validated_data.pop('recommended_actions', instance.recommended_actions)
        instance.animal = validated_data.pop('animal', instance.animal)
        instance.save()
        return instance


class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = "__all__"

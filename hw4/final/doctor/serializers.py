from django.contrib.auth.models import User, Group
from doctor.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model
from django.db import transaction
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


UserModel = get_user_model()


class SpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spec
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ("phone", "username", "password", "user_type", "auth_token")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    week_days = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Doctor
        fields = '__all__'

    def create(self, validated_data):
        try:
            with transaction.atomic():
                user_data = validated_data.pop('user')
                user = UserModel.objects.create_user(**user_data)
                doctor = Doctor.objects.create(user=user, **validated_data)
                print(doctor, type(doctor))
                return doctor
        except Exception as e:
            raise e


class PatientSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        try:
            with transaction.atomic():
                user_data = validated_data.pop('user')
                user = UserModel.objects.create_user(**user_data)
                return Patient.objects.create(user=user, **validated_data)
        except Exception as e:
            raise e


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token
    # pass
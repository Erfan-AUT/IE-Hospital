from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions
from doctor.serializers import *
from doctor.models import *
from doctor.permissions import *



class DoctorViewSet(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []


class PatientViewSet(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = []


class SpecViewSet(generics.ListAPIView):
    queryset = Spec.objects.all()
    serializer_class = SpecSerializer
    permission_classes = []


class CommentViewSet(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsPatientOrReadOnly]



from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = ()
    serializer_class = MyTokenObtainPairSerializer

from django.shortcuts import render
from .models import (BloodBankDonor,Donor)
from .serializers import (BloodBankDonorSerializer,DonorSerializer)
from rest_framework import generics,mixins,viewsets,status

# Create your views here.
class BloodBankDonorViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=BloodBankDonor.objects.all()
    serializer_class=BloodBankDonorSerializer

class DonorViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset=Donor.objects.all()
    serializer_class=DonorSerializer